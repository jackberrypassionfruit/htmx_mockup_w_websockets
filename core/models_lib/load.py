from ..models import SerializeMaster, InspectionMaster

from django.db.utils import IntegrityError
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count, Q, Max

models_dict = {"serialize": SerializeMaster, "sort": InspectionMaster}


def update_end_job(model, job_number, user_name):
    now = timezone.now()
    try:
        model.objects.filter(Q(job_number=job_number)).update(
            start_operator=user_name,
            start_datetime=now,
            end_operator=user_name,
            end_datetime=now,
            scrapped="No",
        )
    except IntegrityError as e:
        messages.info(f"errored at {e}")
