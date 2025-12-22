from django.contrib import admin
from core.models import SerializeMaster, InspectionMaster, PatchMaster

# Register your models here.
admin.site.register(SerializeMaster)
admin.site.register(InspectionMaster)
admin.site.register(PatchMaster)
