from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to="profilepics/", null=True, blank=True)


class CoresMasterDetails(models.Model):
    part_id = models.CharField(max_length=255, db_index=True, unique=True)
    configuration_id = models.IntegerField()
    program_number = models.IntegerField()
    die_revision = models.CharField(max_length=255, db_index=False)
    process_step_num = models.IntegerField()
    location = models.CharField(max_length=255, db_index=False)
    sub_location = models.CharField(null=True, max_length=255, db_index=False)
    slurry_batch = models.CharField(null=True, max_length=255, db_index=False)
    job_number = models.CharField(max_length=255, db_index=False)
    scrap_time = models.DateTimeField(null=True, max_length=255, db_index=False)
    scrap_step = models.CharField(null=True, max_length=255, db_index=False)
    scrap_code = models.CharField(null=True, max_length=255, db_index=False)
    scrap_operator = models.CharField(null=True, max_length=255, db_index=False)
    scrap_notes = models.CharField(null=True, max_length=255, db_index=False)
    created_by = models.CharField(max_length=255, db_index=False)
    created_datetime = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(null=True, max_length=255, db_index=False)
    modified_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.part_id


class CoresMasterChangelog(models.Model):
    pk_id = models.AutoField(primary_key=True)
    part_id = models.CharField(max_length=255, db_index=False, unique=False)
    configuration_id = models.IntegerField()
    from_process_step_num = models.IntegerField()
    to_process_step_num = models.IntegerField()
    job_number = models.CharField(max_length=255, db_index=False)
    run_number = models.IntegerField(null=True, blank=True)
    operator = models.CharField(max_length=255, db_index=False)
    transaction_type = models.CharField(max_length=255, db_index=False)
    transaction_details = models.CharField(max_length=255, db_index=False)
    transaction_time = models.DateTimeField(null=True, blank=True)
    from_location = models.CharField(max_length=255, db_index=False)
    to_location = models.CharField(max_length=255, db_index=False)
    notes = models.CharField(max_length=255, db_index=False)
    app_version = models.CharField(max_length=255, db_index=False)
    created_by = models.CharField(max_length=255, db_index=False)
    created_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.part_id


class SerializeMaster(models.Model):
    part_id = models.CharField(max_length=255, db_index=True, unique=True)
    configuration_id = models.IntegerField()
    process_step_num = models.IntegerField()
    job_number = models.CharField(max_length=255, db_index=False)
    start_operator = models.CharField(max_length=255, db_index=False)
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_operator = models.CharField(max_length=255, db_index=False)
    end_datetime = models.DateTimeField(null=True, blank=True)
    notes = models.CharField(max_length=255, db_index=False)
    scrapped = models.CharField(max_length=255, db_index=False)
    created_by = models.CharField(max_length=255, db_index=False)
    created_datetime = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(max_length=255, db_index=False)
    modified_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.part_id


class InspectionMaster(models.Model):
    part_id = models.CharField(max_length=255, db_index=True, unique=False)
    configuration_id = models.IntegerField()
    process_step_num = models.IntegerField()
    job_number = models.CharField(max_length=255, db_index=False)
    sub_process = models.CharField(max_length=255, db_index=False)
    run_number = models.IntegerField(null=True, blank=True)
    scan_number = models.IntegerField(null=True, blank=True)
    process_state = models.CharField(max_length=255, db_index=False)
    start_operator = models.CharField(max_length=255, db_index=False)
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_operator = models.CharField(max_length=255, db_index=False)
    end_datetime = models.DateTimeField(null=True, blank=True)
    rebatch_operator = models.CharField(max_length=255, db_index=False)
    rebatch_datetime = models.DateTimeField(null=True, blank=True)
    scrapped = models.CharField(max_length=255, db_index=False)
    created_by = models.CharField(max_length=255, db_index=False)
    created_datetime = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(max_length=255, db_index=False)
    modified_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.part_id


class PatchMaster(models.Model):
    master_fk = models.ForeignKey(
        CoresMasterDetails,
        on_delete=models.CASCADE,
        db_column="part_id",
        related_name="patch",
    )
    process_step_num = models.IntegerField()
    sub_process = models.CharField(null=True, max_length=255, db_index=False)
    run_number = models.IntegerField(null=True, blank=True)
    patch_cycle = models.IntegerField(null=True, blank=True)
    location = models.CharField(null=True, max_length=255, db_index=False)
    sub_location = models.CharField(null=True, max_length=255, db_index=False)
    start_operator = models.CharField(null=True, max_length=255, db_index=False)
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_operator = models.CharField(null=True, max_length=255, db_index=False)
    end_datetime = models.DateTimeField(null=True, blank=True)
    scrapped = models.CharField(null=True, max_length=255, db_index=False)
    created_by = models.CharField(max_length=255, db_index=False)
    created_datetime = models.DateTimeField(null=True, blank=True)
    modified_by = models.CharField(null=True, max_length=255, db_index=False)
    modified_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.part_id
