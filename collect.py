import sys, os

project_dir = "/core"
sys.path.append(project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "cores_hub.settings"
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)

import django


django.setup()

import subprocess
import polars as pl

from django.db import transaction
from dateutil import parser
from dateutil import tz
from core.models import (
    CoresMasterDetails,
    PatchMaster,
    SerializeMaster,
    InspectionMaster,
)

models_dict = {
    "serialize": SerializeMaster,
    "sort": InspectionMaster,
    "patch": PatchMaster,
}


def parse_datetime_w_tz(date_str):
    tzinfos = {"EST": tz.gettz("US/Eastern")}
    date = (
        parser.parse(date_str + " EST", tzinfos=tzinfos) if date_str != "NULL" else None
    )
    return date


try:
    subprocess.run(["rm", "db.sqlite3"])
except:
    pass
subprocess.run(["uv", "run", "manage.py", "migrate"])


df = pl.read_csv("test_files/cores_master_details.csv")
records_to_insert = []
for row in df.iter_rows(named=True):
    # print(row)
    # Create the record instance
    record = CoresMasterDetails(
        part_id=row["part_id"],
        configuration_id=row["configuration_id"],
        program_number=row["program_number"],
        die_revision=row["die_revision"],
        process_step_num=row["process_step_num"],
        location=row["location"],
        sub_location=row["sub_location"],
        slurry_batch=row["slurry_batch"],
        job_number=row["job_number"],
        scrap_time=parse_datetime_w_tz(row["scrap_time"]),
        scrap_step=row["scrap_step"],
        scrap_code=row["scrap_code"],
        scrap_operator=row["scrap_operator"],
        scrap_notes=row["scrap_notes"],
        created_datetime=parse_datetime_w_tz(row["created_datetime"]),
        created_by=row["created_by"],
    )
    # to save the current record
    # record.save()
    records_to_insert.append(record)
with transaction.atomic():
    CoresMasterDetails.objects.bulk_create(records_to_insert)

records_to_insert = []
df = pl.read_csv("test_files/patch_master.csv")
# Iterate through the DataFrame and create model instances
for row in df.iter_rows(named=True):
    try:
        cores_instance = CoresMasterDetails.objects.get(part_id=row["part_id"])
    except CoresMasterDetails.DoesNotExist:
        print(
            f"Warning: part_id {row['part_id']} not found in CoresMasterDetails, skipping"
        )
        continue

    # Create the record instance
    record = PatchMaster(
        master_fk=cores_instance,
        # configuration_id=row["configuration_id"],
        process_step_num=row["process_step_num"],
        # job_number=row["job_number"],
        start_operator=row["start_operator"],
        start_datetime=parse_datetime_w_tz(row["start_datetime"]),
        end_operator=row["end_operator"],
        end_datetime=parse_datetime_w_tz(row["end_datetime"]),
        scrapped=row["scrapped"],
        created_by=row["created_by"],
        created_datetime=parse_datetime_w_tz(row["created_datetime"]),
        modified_by=row["modified_by"],
        modified_datetime=parse_datetime_w_tz(row["modified_datetime"]),
    )
    if row.get("sub_process", None):
        record.sub_process = row["sub_process"]
    # to save the current record
    # record.save()
    records_to_insert.append(record)
with transaction.atomic():
    PatchMaster.objects.bulk_create(records_to_insert)


for page_slug, model in dict(
    {"serialize": SerializeMaster, "sort": InspectionMaster}
).items():
    # for page_slug, model in models_dict.items():
    records_to_insert = []
    df = pl.read_csv(f"test_files/{page_slug}_master.csv")
    # Iterate through the DataFrame and create model instances
    for row in df.iter_rows(named=True):
        if page_slug == "patch":
            try:
                cores_instance = CoresMasterDetails.objects.get(part_id=row["part_id"])
            except CoresMasterDetails.DoesNotExist:
                print(
                    f"Warning: part_id {row['part_id']} not found in CoresMasterDetails, skipping"
                )
                continue
        else:
            cores_instance = row["part_id"]

        # Create the record instance
        record = model(
            part_id=cores_instance,
            configuration_id=row["configuration_id"],
            process_step_num=row["process_step_num"],
            job_number=row["job_number"],
            start_operator=row["start_operator"],
            start_datetime=parse_datetime_w_tz(row["start_datetime"]),
            end_operator=row["end_operator"],
            end_datetime=parse_datetime_w_tz(row["end_datetime"]),
            scrapped=row["scrapped"],
            created_by=row["created_by"],
            created_datetime=parse_datetime_w_tz(row["created_datetime"]),
            modified_by=row["modified_by"],
            modified_datetime=parse_datetime_w_tz(row["modified_datetime"]),
        )
        if row.get("sub_process", None):
            record.sub_process = row["sub_process"]
        # to save the current record
        # record.save()
        records_to_insert.append(record)
    with transaction.atomic():
        model.objects.bulk_create(records_to_insert)

print("CSV data has been loaded into the Django database.")
