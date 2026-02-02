from ..models import SerializeMaster, InspectionMaster, PatchMaster
from ..dcap_models import Cores2SerializeMaster, Cores2InspectionMaster, Cores2PatchMaster

from django.db.utils import IntegrityError
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count, Q, Max
from django.db import connection

models_dict = {
    "serialize": Cores2SerializeMaster,
    "sort": Cores2InspectionMaster,
    "patch-finish": Cores2PatchMaster,
    "patch-cure": Cores2PatchMaster,
    "patch-sand": Cores2PatchMaster,
}


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

def sp_MoveSerializeTransact(
    job_number,
    page,
	sub_process,
	eng_toggle,
	mrb_toggle,
	css_toggle,
	current_user
):
    current_locals = locals()
    sproc_args_string = ", ".join(["@"+key+"=%s" for key in current_locals.keys()])
    sproc_values_list = list(current_locals.values())
    
#     print(f'''
# What I would execute:
# EXEC dbo.MoveSerializeTransact "{sproc_args_string}",
# {sproc_values_list}
#     ''')
    
    with connection.cursor() as cursor:
        ### this would be cool but did not work
        # cursor.execute(
        #     f"EXEC dbo.MoveSerializeTransact {sproc_values_list}",
        #     sproc_values_list
        # )
        cursor.execute(
            "EXEC dbo.MoveSerializeTransact @job_number=%s, @page=%s, @sub_process=%s, @eng_toggle=%s, @mrb_toggle=%s, @css_toggle=%s, @current_user=%s",
            [
                job_number,
                page,
                sub_process,
                eng_toggle,
                mrb_toggle,
                css_toggle,
                current_user
            ]
        )
        
        
# '''

# sp_MoveSerializeTransact(
#     job_number="fart",
#     page="butt",
# 	sub_process="tush",
# 	eng_toggle="crud",
# 	mrb_toggle="buttagain",
# 	css_toggle="vomit",
# 	current_user="wtf"
# )

# """