# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Buildversion(models.Model):
    systeminformationid = models.AutoField(db_column='SystemInformationID', primary_key=True)  # Field name made lowercase.
    database_version = models.CharField(db_column='Database Version', max_length=25)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    versiondate = models.DateTimeField(db_column='VersionDate')  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[BuildVersion]'


class CleanzallRundata(models.Model):
    runstarttimeutc = models.DateTimeField(db_column='RunStartTimeUTC', blank=True, null=True)  # Field name made lowercase.
    avgairpressure = models.FloatField(db_column='AvgAirPressure', blank=True, null=True)  # Field name made lowercase.
    avgsolventpressure = models.FloatField(db_column='AvgSolventPressure', blank=True, null=True)  # Field name made lowercase.
    avgtemp1 = models.FloatField(db_column='AvgTemp1', blank=True, null=True)  # Field name made lowercase.
    avgtemp2 = models.FloatField(db_column='AvgTemp2', blank=True, null=True)  # Field name made lowercase.
    avgflowrate = models.FloatField(db_column='AvgFlowRate', blank=True, null=True)  # Field name made lowercase.
    numrecs = models.IntegerField(db_column='NumRecs', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[Cleanzall_Rundata]'


class CleanzallRundataTimes(models.Model):
    runstarttimeutc = models.DateTimeField(db_column='RunStartTimeUTC', blank=True, null=True)  # Field name made lowercase.
    numrecs = models.IntegerField(db_column='NumRecs', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[Cleanzall_Rundata_Times]'


class ConfigurationMaster(models.Model):
    configuration_id = models.IntegerField(blank=True, null=True)
    submitter_name = models.CharField(max_length=50, blank=True, null=True)
    part_number = models.CharField(max_length=20, blank=True, null=True)
    die_revision = models.CharField(max_length=10, blank=True, null=True)
    part_qty = models.IntegerField(blank=True, null=True)
    request_type = models.CharField(max_length=50, blank=True, null=True)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    urgency = models.CharField(max_length=50, blank=True, null=True)
    requested_complete_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    request_notes = models.TextField(blank=True, null=True)
    approval_status = models.CharField(max_length=20, blank=True, null=True)
    completion_status = models.CharField(max_length=20, blank=True, null=True)
    std_routing_revision = models.IntegerField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Configuration.Master]'


class ConfigurationMasterJobMap(models.Model):
    configuration_id = models.IntegerField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    print_number = models.IntegerField(blank=True, null=True)
    qty_parts = models.IntegerField(blank=True, null=True)
    plan_date = models.DateField(blank=True, null=True)
    plan_start_time = models.TimeField(blank=True, null=True)
    assigned_printer = models.CharField(max_length=10, blank=True, null=True)
    print_file_name_cfg = models.CharField(max_length=50, blank=True, null=True)
    material_file_name_cfg = models.CharField(max_length=50, blank=True, null=True)
    estimated_print_time = models.TimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Configuration.Master.Job_Map]'


class ConfigurationMasterJobMapCores(models.Model):
    configuration_id = models.IntegerField(blank=True, null=True)
    from_job_type = models.CharField(max_length=50, blank=True, null=True)
    to_job_type = models.CharField(max_length=50, blank=True, null=True)
    from_job_number = models.CharField(max_length=50, blank=True, null=True)
    to_job_number = models.CharField(max_length=50, blank=True, null=True)
    from_run_id = models.CharField(max_length=50, blank=True, null=True)
    to_run_id = models.CharField(max_length=50, blank=True, null=True)
    qty_parts = models.IntegerField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Configuration.Master.Job_Map_Cores]'


class ConfigurationPlanningDetails(models.Model):
    configuration_id = models.IntegerField(blank=True, null=True)
    qty_jobs = models.IntegerField(blank=True, null=True)
    qty_parts = models.IntegerField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Configuration.Planning.Details]'


class ConfigurationProcessParameters(models.Model):
    configuration_id = models.IntegerField(blank=True, null=True)
    part_number = models.CharField(max_length=20, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    process_state = models.CharField(max_length=50, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    process_step_name = models.CharField(max_length=50, blank=True, null=True)
    attribute = models.CharField(max_length=100, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Configuration.Process_Parameters]'


class ConfigurationRmaPartSelection(models.Model):
    part_id_old = models.CharField(max_length=20, blank=True, null=True)
    part_id_new = models.CharField(max_length=20, blank=True, null=True)
    configuration_id_rma = models.IntegerField(blank=True, null=True)
    die_revision = models.CharField(max_length=10, blank=True, null=True)
    slurry_batch = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Configuration.RMA.Part_Selection]'


class ConfigurationRecurringJobs(models.Model):
    system = models.CharField(max_length=50, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    frequency_days = models.IntegerField(blank=True, null=True)
    active = models.CharField(max_length=50, blank=True, null=True)
    job_name = models.CharField(max_length=50, blank=True, null=True)
    serial_numbers = models.TextField(blank=True, null=True)
    parameter1 = models.CharField(db_column='Parameter1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parameter2 = models.CharField(db_column='Parameter2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parameter3 = models.CharField(db_column='Parameter3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parameter4 = models.CharField(db_column='Parameter4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Configuration.Recurring_Jobs]'


class ConfigurationRefProcessParameters(models.Model):
    part_number = models.CharField(max_length=20, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    process_state = models.CharField(max_length=50, blank=True, null=True)
    process_step_name = models.CharField(max_length=50, blank=True, null=True)
    attribute = models.CharField(max_length=100, blank=True, null=True)
    default_value = models.CharField(max_length=100, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Configuration.Ref.Process_Parameters]'


class ConfigurationRefRoutings(models.Model):
    part_number = models.CharField(max_length=10, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    routing_type = models.CharField(max_length=50, blank=True, null=True)
    template_name = models.CharField(max_length=50, blank=True, null=True)
    template_tag = models.CharField(max_length=50, blank=True, null=True)
    locked = models.CharField(max_length=10, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    process_state = models.CharField(max_length=50, blank=True, null=True)
    process_step_name = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Configuration.Ref.Routings]'


class ConfigurationRefSubRoutings(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    part_number = models.CharField(max_length=20, blank=True, null=True)
    revision = models.SmallIntegerField(blank=True, null=True)
    process_state = models.CharField(max_length=100, blank=True, null=True)
    process_step = models.CharField(max_length=100, blank=True, null=True)
    sequence_number = models.SmallIntegerField(blank=True, null=True)
    sub_process = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Configuration.Ref.Sub_Routings]'


class ConfigurationRoutings(models.Model):
    configuration_id = models.IntegerField(blank=True, null=True)
    part_number = models.CharField(max_length=20, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    locked = models.CharField(max_length=10, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    process_state = models.CharField(max_length=50, blank=True, null=True)
    process_step_name = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Configuration.Routings]'


class CoresCheckpoints(models.Model):
    seq_num = models.FloatField(db_column='Seq_Num')  # Field name made lowercase.
    checkpoint = models.CharField(db_column='Checkpoint', max_length=50)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[Cores.Checkpoints]'


class CoresDimensionalDeviations(models.Model):
    inspection_plan_number = models.CharField(max_length=20, blank=True, null=True)
    part_number = models.CharField(max_length=10, blank=True, null=True)
    characteristic = models.CharField(max_length=250, blank=True, null=True)
    deviation_lower_tolerance = models.FloatField(blank=True, null=True)
    deviation_upper_tolerance = models.FloatField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    deviation_id = models.CharField(max_length=10, blank=True, null=True)
    sub_deviation = models.CharField(max_length=10, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    authorized_by = models.CharField(max_length=50, blank=True, null=True)
    authorized_datetime = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores.Dimensional.Deviations]'


class CoresMaterialsDetails(models.Model):
    specimen_id = models.CharField(max_length=20, blank=True, null=True)
    test_id = models.IntegerField()
    test_key = models.CharField(max_length=50, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Cores.Materials.Details]'


class CoresMaterialsMaster(models.Model):
    metric = models.CharField(max_length=50, blank=True, null=True)
    specimen_id = models.CharField(max_length=20, blank=True, null=True)
    low_fire_run_id = models.CharField(db_column='low_fire.run_id', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    high_fire_run_id = models.CharField(db_column='high_fire.run_id', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sag_run_id = models.CharField(db_column='sag.run_id', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sag_run_profile = models.CharField(max_length=50, blank=True, null=True)
    job_number = models.CharField(max_length=50, blank=True, null=True)
    equipment_id = models.CharField(max_length=10, blank=True, null=True)
    sop_number = models.IntegerField(db_column='SOP_number', blank=True, null=True)  # Field name made lowercase.
    project_id = models.CharField(max_length=20, blank=True, null=True)
    material_part_number = models.CharField(max_length=10, blank=True, null=True)
    slurry_batch_number = models.CharField(max_length=20, blank=True, null=True)
    material_lot_number = models.CharField(max_length=20, blank=True, null=True)
    cartridge_id = models.CharField(max_length=20, blank=True, null=True)
    report_url = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    furnace_location = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    test_id = models.IntegerField()
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores.Materials.Master]'


class CoresRefMaterialsMaster(models.Model):
    metric = models.CharField(max_length=50, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    test_key = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores.Ref.Materials.Master]'


class CoresTeSlotMeasDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_stage = models.CharField(max_length=20, blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    characteristic = models.CharField(max_length=20, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Cores.TE_Slot_Meas.Details]'


class CoresTeSlotMeasMaster(models.Model):
    job_number = models.CharField(max_length=10, blank=True, null=True)
    part_id = models.CharField(max_length=20, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    process_stage = models.CharField(max_length=20, blank=True, null=True)
    monitoring_value = models.FloatField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores.TE_Slot_Meas.Master]'


class Cores2BluelightDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Bluelight.Details]'


class Cores2BluelightMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    scan_number = models.IntegerField(blank=True, null=True)
    inspection_plan = models.CharField(max_length=20, blank=True, null=True)
    inspection_revision = models.IntegerField(blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Bluelight.Master]'


class Cores2CmmDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.CMM.Details]'


class Cores2CmmMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    scan_number = models.IntegerField(blank=True, null=True)
    inspection_plan = models.CharField(max_length=20, blank=True, null=True)
    inspection_revision = models.IntegerField(blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.CMM.Master]'


class Cores2CureDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Cure.Details]'


class Cores2CureMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    sub_location = models.CharField(max_length=50, blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_operator = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Cure.Master]'


class Cores2DimensionalDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Dimensional.Details]'


class Cores2DimensionalMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    scan_number = models.IntegerField(blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_operator = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    rebatch_operator = models.CharField(max_length=50, blank=True, null=True)
    rebatch_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Dimensional.Master]'


class Cores2DimensionalPartEvaluationFilteredCached(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_state = models.CharField(max_length=50, blank=True, null=True)
    scan_number = models.IntegerField(blank=True, null=True)
    scan_date = models.DateField(blank=True, null=True)
    part_number = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=20, blank=True, null=True)
    pk_id = models.IntegerField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    count_pass = models.IntegerField(blank=True, null=True)
    count_deviation = models.IntegerField(blank=True, null=True)
    count_mrb = models.IntegerField(db_column='count_MRB', blank=True, null=True)  # Field name made lowercase.
    count_fail = models.IntegerField(blank=True, null=True)
    pass_status = models.CharField(max_length=10, blank=True, null=True)
    inspection_plan = models.CharField(max_length=50, blank=True, null=True)
    inspection_revision = models.IntegerField(blank=True, null=True)
    deviation_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Dimensional.Part_Evaluation.FILTERED.Cached]'


class Cores2DimensionalPartEvaluationFilteredCachedAudit(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_state = models.CharField(max_length=50, blank=True, null=True)
    scan_number = models.IntegerField(blank=True, null=True)
    scan_date = models.DateField(blank=True, null=True)
    part_number = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=20, blank=True, null=True)
    pk_id = models.IntegerField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    count_pass = models.IntegerField(blank=True, null=True)
    count_mrb = models.IntegerField(db_column='count_MRB', blank=True, null=True)  # Field name made lowercase.
    count_fail = models.IntegerField(blank=True, null=True)
    pass_status = models.CharField(max_length=10, blank=True, null=True)
    inspection_plan = models.CharField(max_length=50, blank=True, null=True)
    inspection_revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Dimensional.Part_Evaluation.FILTERED.Cached.AUDIT]'


class Cores2DissolutionDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Dissolution.Details]'


class Cores2DissolutionMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    sub_location = models.CharField(max_length=50, blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_operator = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    end_dry_operator = models.CharField(max_length=50, blank=True, null=True)
    end_dry_datetime = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Dissolution.Master]'


class Cores2FinalQualityDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Final_Quality.Details]'


class Cores2FinalQualityMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    authorized_by = models.CharField(max_length=50, blank=True, null=True)
    authorized_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Final_Quality.Master]'


class Cores2FinalQualityMasterWPartEvaluationFilteredCached(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    core_id = models.CharField(max_length=10, blank=True, null=True)
    configuration_id = models.SmallIntegerField(blank=True, null=True)
    process_step_num = models.SmallIntegerField(blank=True, null=True)
    part_number = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    job_number = models.CharField(max_length=20, blank=True, null=True)
    slurry_batch = models.CharField(max_length=20, blank=True, null=True)
    cartridge_id = models.CharField(max_length=20, blank=True, null=True)
    result = models.CharField(max_length=20)
    pk_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = '[Cores2.Final_Quality_Master_w_Part_Evaluation_FILTERED.Cached]'


class Cores2FireConfiguration(models.Model):
    firing_configuration_id = models.IntegerField(blank=True, null=True)
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    sub_location = models.CharField(max_length=50, blank=True, null=True)
    setter_id = models.CharField(max_length=50, blank=True, null=True)
    process_pk_id = models.IntegerField(blank=True, null=True)
    firing_order = models.IntegerField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    shelf_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Fire.Configuration]'


class Cores2FireConfigurationByShelf(models.Model):
    firing_configuration_id = models.IntegerField(blank=True, null=True)
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    sub_location = models.CharField(max_length=50, blank=True, null=True)
    setter_id = models.CharField(max_length=50, blank=True, null=True)
    shelf_type = models.CharField(max_length=50, blank=True, null=True)
    process_pk_id = models.IntegerField(blank=True, null=True)
    firing_order = models.IntegerField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Fire.Configuration_by_Shelf]'


class Cores2FireDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Fire.Details]'


class Cores2FireMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    sub_location = models.CharField(max_length=50, blank=True, null=True)
    setter_id = models.CharField(max_length=50, blank=True, null=True)
    run_id = models.CharField(max_length=20, blank=True, null=True)
    furnace_id = models.CharField(max_length=20, blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_operator = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    rebatch_operator = models.CharField(max_length=50, blank=True, null=True)
    rebatch_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Fire.Master]'


class Cores2HoldMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    hold_type = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    sub_location = models.CharField(max_length=50, blank=True, null=True)
    next_location = models.CharField(max_length=50, blank=True, null=True)
    next_sub_location = models.CharField(max_length=50, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    program_number = models.IntegerField(blank=True, null=True)
    die_revision = models.CharField(max_length=20, blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    process_pk_id = models.IntegerField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    patch_cycle = models.IntegerField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    process_state = models.CharField(max_length=20, blank=True, null=True)
    operator_notes = models.CharField(max_length=500, blank=True, null=True)
    ncmr_id = models.IntegerField(blank=True, null=True)
    scan_number = models.IntegerField(blank=True, null=True)
    authorized_by = models.CharField(max_length=50, blank=True, null=True)
    authorized_datetime = models.DateTimeField(blank=True, null=True)
    authorized_notes = models.CharField(max_length=500, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Hold.Master]'


class Cores2HoldMasterTestingCrossSiteShipment(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    hold_type = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    sub_location = models.CharField(max_length=50, blank=True, null=True)
    next_location = models.CharField(max_length=50, blank=True, null=True)
    next_sub_location = models.CharField(max_length=50, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    program_number = models.IntegerField(blank=True, null=True)
    die_revision = models.CharField(max_length=20, blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    process_pk_id = models.IntegerField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    patch_cycle = models.IntegerField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    process_state = models.CharField(max_length=20, blank=True, null=True)
    operator_notes = models.CharField(max_length=500, blank=True, null=True)
    ncmr_id = models.IntegerField(blank=True, null=True)
    scan_number = models.IntegerField(blank=True, null=True)
    authorized_by = models.CharField(max_length=50, blank=True, null=True)
    authorized_datetime = models.DateTimeField(blank=True, null=True)
    authorized_notes = models.CharField(max_length=500, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Hold.Master.TESTING.Cross_Site_Shipment]'


class Cores2InjectionDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Injection.Details]'


class Cores2InjectionMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    plan_date = models.DateField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    cartridge_id = models.CharField(max_length=50, blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_operator = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Injection.Master]'


class Cores2InspectionCtTraceability(models.Model):
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    part_id = models.CharField(max_length=20, blank=True, null=True)
    qc_result = models.CharField(max_length=50, blank=True, null=True)
    analysis_result = models.CharField(max_length=50, blank=True, null=True)
    filepath = models.TextField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Inspection.CT_Traceability]'


class Cores2InspectionDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Inspection.Details]'


class Cores2InspectionMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    sub_process = models.CharField(max_length=50, blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    scan_number = models.IntegerField(blank=True, null=True)
    process_state = models.CharField(max_length=20, blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_operator = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    rebatch_operator = models.CharField(max_length=50, blank=True, null=True)
    rebatch_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Inspection.Master]'


class Cores2MasterChangelog(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    from_process_step_num = models.IntegerField(blank=True, null=True)
    to_process_step_num = models.IntegerField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    transaction_type = models.CharField(max_length=50, blank=True, null=True)
    transaction_time = models.DateTimeField(blank=True, null=True)
    from_location = models.CharField(max_length=50, blank=True, null=True)
    to_location = models.CharField(max_length=50, blank=True, null=True)
    transaction_details = models.CharField(max_length=1000, blank=True, null=True)
    notes = models.CharField(max_length=1000, blank=True, null=True)
    app_version = models.CharField(max_length=20, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    attachments = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Master.Changelog]'


class Cores2MasterDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    program_number = models.CharField(max_length=10, blank=True, null=True)
    die_revision = models.CharField(max_length=10, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    sub_location = models.CharField(max_length=50, blank=True, null=True)
    slurry_batch = models.CharField(max_length=50, blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    scrap_step = models.CharField(max_length=50, blank=True, null=True)
    scrap_code = models.CharField(max_length=10, blank=True, null=True)
    scrap_operator = models.CharField(max_length=50, blank=True, null=True)
    scrap_notes = models.CharField(max_length=250, blank=True, null=True)
    scrap_time = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Master.Details]'


class Cores2PatchDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    patch_cycle = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Patch.Details]'


class Cores2PatchMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    sub_process = models.CharField(max_length=50, blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    patch_cycle = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    sub_location = models.CharField(max_length=50, blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_operator = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Patch.Master]'


class Cores2RefInspectionMaster(models.Model):
    part_number = models.CharField(max_length=10, blank=True, null=True)
    process_state = models.CharField(max_length=20, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Ref.Inspection.Master]'


class Cores2RefInspectionSubRoutings(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    part_number = models.CharField(max_length=20, blank=True, null=True)
    revision = models.SmallIntegerField(blank=True, null=True)
    process_state = models.CharField(max_length=100, blank=True, null=True)
    sequence_number = models.SmallIntegerField(blank=True, null=True)
    sub_process = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Ref.Inspection.Sub_Routings]'


class Cores2SerializeDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Serialize.Details]'


class Cores2SerializeMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_operator = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Serialize.Master]'


class Cores2ShipMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    po_number = models.CharField(max_length=50, blank=True, null=True)
    line_item = models.CharField(max_length=50, blank=True, null=True)
    shipped_by = models.CharField(max_length=50, blank=True, null=True)
    shipped_datetime = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Ship.Master]'


class Cores2SiteLocationChangelog(models.Model):
    pk_id = models.IntegerField()
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.SmallIntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    from_site = models.CharField(max_length=50, blank=True, null=True)
    from_process_step_num = models.SmallIntegerField(blank=True, null=True)
    to_site = models.CharField(max_length=50, blank=True, null=True)
    to_process_step_num = models.SmallIntegerField(blank=True, null=True)
    shipped_by = models.CharField(max_length=100, blank=True, null=True)
    shipped_datetime = models.DateTimeField(blank=True, null=True)
    received_by = models.CharField(max_length=100, blank=True, null=True)
    received_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    voided = models.BooleanField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Site_Location.Changelog]'


class Cores2ThroughputCached(models.Model):
    qty = models.IntegerField(blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    transaction_type = models.CharField(max_length=50, blank=True, null=True)
    txn_date = models.DateField(blank=True, null=True)
    from_location = models.CharField(max_length=50, blank=True, null=True)
    oracle_seq_step = models.CharField(db_column='Oracle_Seq_Step', max_length=50, blank=True, null=True)  # Field name made lowercase.
    to_location = models.CharField(max_length=50, blank=True, null=True)
    checkpoint = models.CharField(db_column='Checkpoint', max_length=50, blank=True, null=True)  # Field name made lowercase.
    esh = models.FloatField(db_column='ESH', blank=True, null=True)  # Field name made lowercase.
    part_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Cores2.Throughput_cached]'


class Db11Opclog(models.Model):
    id = models.IntegerField(primary_key=True)
    field_name = models.CharField(db_column='_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_numericid = models.IntegerField(db_column='_NUMERICID', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_value = models.CharField(db_column='_VALUE', max_length=64, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_timestamp = models.DateTimeField(db_column='_TIMESTAMP', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_quality = models.IntegerField(db_column='_QUALITY', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = '[DB11OPCLog]'


class DiesCleanDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Clean.Details]'


class DiesCleanMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    print_number = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_clean_operator = models.CharField(max_length=50, blank=True, null=True)
    end_clean_datetime = models.DateTimeField(blank=True, null=True)
    end_dry_operator = models.CharField(max_length=50, blank=True, null=True)
    end_dry_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Clean.Master]'
        unique_together = (('part_id', 'process_step_num'),)


class DiesDimensionalDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Dimensional.Details]'


class DiesDimensionalMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    print_number = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    sub_process = models.CharField(max_length=50, blank=True, null=True)
    plan_date = models.DateField(blank=True, null=True)
    scan_number = models.IntegerField(blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_operator = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    rebatch_operator = models.CharField(max_length=50, blank=True, null=True)
    rebatch_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Dimensional.Master]'
        unique_together = (('part_id', 'process_step_num'),)


class DiesHoldMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    hold_type = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    sub_location = models.CharField(max_length=50, blank=True, null=True)
    next_location = models.CharField(max_length=50, blank=True, null=True)
    next_sub_location = models.CharField(max_length=50, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    program_number = models.IntegerField(blank=True, null=True)
    die_revision = models.CharField(max_length=20, blank=True, null=True)
    print_number = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    process_pk_id = models.IntegerField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    process_state = models.CharField(max_length=20, blank=True, null=True)
    operator_notes = models.CharField(max_length=500, blank=True, null=True)
    ncmr_id = models.IntegerField(blank=True, null=True)
    scan_number = models.IntegerField(blank=True, null=True)
    authorized_by = models.CharField(max_length=50, blank=True, null=True)
    authorized_datetime = models.DateTimeField(blank=True, null=True)
    authorized_notes = models.CharField(max_length=500, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Hold.Master]'


class DiesInjectionMasterMapTemp(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    print_number = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Injection.Master_Map_Temp]'


class DiesInspectionMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    print_number = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    sub_process = models.CharField(max_length=50, blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_operator = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Inspection.Master]'


class DiesInspectionUsonSampleDetails(models.Model):
    serial_num = models.CharField(max_length=20, blank=True, null=True)
    measurement_type = models.CharField(max_length=50, blank=True, null=True)
    sample_index = models.SmallIntegerField(blank=True, null=True)
    data_1 = models.FloatField(blank=True, null=True)
    data_2 = models.FloatField(blank=True, null=True)
    port_num = models.SmallIntegerField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Inspection.Uson_Sample_Details]'


class DiesMasterChangelog(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    from_process_step_num = models.IntegerField(blank=True, null=True)
    to_process_step_num = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    transaction_type = models.CharField(max_length=50, blank=True, null=True)
    transaction_time = models.DateTimeField(blank=True, null=True)
    from_location = models.CharField(max_length=50, blank=True, null=True)
    to_location = models.CharField(max_length=50, blank=True, null=True)
    transaction_details = models.CharField(max_length=1000, blank=True, null=True)
    notes = models.CharField(max_length=1000, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    attachments = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Master.Changelog]'


class DiesMasterDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    program_number = models.CharField(max_length=10, blank=True, null=True)
    die_revision = models.CharField(max_length=10, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    sub_location = models.CharField(max_length=50, blank=True, null=True)
    print_number = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    scrap_step = models.CharField(max_length=50, blank=True, null=True)
    scrap_code = models.CharField(max_length=10, blank=True, null=True)
    scrap_operator = models.CharField(max_length=50, blank=True, null=True)
    scrap_notes = models.CharField(max_length=250, blank=True, null=True)
    scrap_time = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Master.Details]'


class DiesPostCureDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Post-cure.Details]'


class DiesPostCureMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    print_number = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    equipment_id = models.CharField(max_length=10, blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_operator = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Post-cure.Master]'
        unique_together = (('part_id', 'process_step_num'),)


class DiesPrintDetails(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Print.Details]'


class DiesPrintMaster(models.Model):
    part_id = models.CharField(unique=True, max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    print_number = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    plan_date = models.DateField(blank=True, null=True)
    plan_start_time = models.TimeField(blank=True, null=True)
    assigned_printer = models.CharField(max_length=10, blank=True, null=True)
    print_file_name_cfg = models.CharField(max_length=50, blank=True, null=True)
    material_file_name_cfg = models.CharField(max_length=50, blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_operator = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Print.Master]'


class DiesRefDieRevisions(models.Model):
    program_number = models.CharField(max_length=10, blank=True, null=True)
    die_part_number = models.CharField(max_length=10, blank=True, null=True)
    die_revision = models.CharField(max_length=20, blank=True, null=True)
    active = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    estimated_print_time = models.TimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Ref.Die_Revisions]'


class DiesRefInspectionMaster(models.Model):
    part_number = models.CharField(max_length=10, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Ref.Inspection.Master]'


class DiesStorageMaster(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    print_number = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    storage_box_id = models.CharField(max_length=10, blank=True, null=True)
    start_operator = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    scrapped = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Dies.Storage.Master]'


class EquipmentAuxiliaryDetails(models.Model):
    equipment_type = models.CharField(max_length=20, blank=True, null=True)
    equipment_id = models.CharField(max_length=10, blank=True, null=True)
    equipment_id_tag = models.CharField(max_length=10, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    condition = models.CharField(max_length=50, blank=True, null=True)
    details = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Equipment.Auxiliary.Details]'


class EquipmentAuxiliaryMaster(models.Model):
    equipment_type = models.CharField(max_length=20, blank=True, null=True)
    equipment_id = models.CharField(max_length=10, blank=True, null=True)
    serial_number = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Equipment.Auxiliary.Master]'


class EquipmentInspectionDetails(models.Model):
    category = models.CharField(max_length=200, blank=True, null=True)
    equip_id = models.CharField(max_length=200, blank=True, null=True)
    inspection_datetime = models.DateTimeField(blank=True, null=True)
    attribute = models.CharField(max_length=200, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    attribute_2 = models.CharField(max_length=200, blank=True, null=True)
    value_2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Equipment.Inspection.Details]'


class EquipmentMaterialSettingsDetails(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    parameter = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    units = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Equipment.Material_Settings.Details]'


class EquipmentMaterialSettingsMaster(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    equipment_id = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Equipment.Material_Settings.Master]'


class EquipmentPrintersChangelog(models.Model):
    equipment_id = models.CharField(max_length=10, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    condition = models.CharField(max_length=50, blank=True, null=True)
    details = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    printer_hood = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Equipment.Printers.Changelog]'


class EquipmentPrintersMaster(models.Model):
    equipment_id = models.CharField(max_length=10, blank=True, null=True)
    common_name = models.CharField(max_length=50, blank=True, null=True)
    model_number = models.CharField(max_length=20, blank=True, null=True)
    serial_number = models.CharField(max_length=20, blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    firmware_version = models.IntegerField(blank=True, null=True)
    captivate_version = models.CharField(max_length=20, blank=True, null=True)
    captivate_key = models.CharField(max_length=20, blank=True, null=True)
    factory_tuned_light_intensity = models.FloatField(blank=True, null=True)
    target_light_exposure = models.FloatField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Equipment.Printers.Master]'


class EquipmentRefMaterialSettings(models.Model):
    revision = models.IntegerField(blank=True, null=True)
    parameter = models.CharField(max_length=100, blank=True, null=True)
    units = models.CharField(max_length=50, blank=True, null=True)
    field_type = models.CharField(max_length=50, blank=True, null=True)
    default_value = models.CharField(max_length=50, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Equipment.Ref.Material_Settings]'


class EquipmentSensorpushClean(models.Model):
    observed_time = models.DateTimeField(blank=True, null=True)
    sensor_id = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    deviceid = models.IntegerField(db_column='deviceId', blank=True, null=True)  # Field name made lowercase.
    run_time = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Equipment.Sensorpush.Clean]'


class Errorlog(models.Model):
    errorlogid = models.AutoField(db_column='ErrorLogID', primary_key=True)  # Field name made lowercase.
    errortime = models.DateTimeField(db_column='ErrorTime')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=128)  # Field name made lowercase.
    errornumber = models.IntegerField(db_column='ErrorNumber')  # Field name made lowercase.
    errorseverity = models.IntegerField(db_column='ErrorSeverity', blank=True, null=True)  # Field name made lowercase.
    errorstate = models.IntegerField(db_column='ErrorState', blank=True, null=True)  # Field name made lowercase.
    errorprocedure = models.CharField(db_column='ErrorProcedure', max_length=126, blank=True, null=True)  # Field name made lowercase.
    errorline = models.IntegerField(db_column='ErrorLine', blank=True, null=True)  # Field name made lowercase.
    errormessage = models.CharField(db_column='ErrorMessage', max_length=4000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[ErrorLog]'


class ExternalEquipmentHobolinkSamplesRaw(models.Model):
    logger_sn = models.CharField(max_length=50, blank=True, null=True)
    sensor_sn = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    data_type_id = models.IntegerField(blank=True, null=True)
    si_value = models.FloatField(blank=True, null=True)
    si_unit = models.CharField(max_length=50, blank=True, null=True)
    us_value = models.FloatField(blank=True, null=True)
    us_unit = models.CharField(max_length=50, blank=True, null=True)
    scaled_value = models.FloatField(blank=True, null=True)
    scaled_unit = models.CharField(max_length=50, blank=True, null=True)
    sensor_key = models.IntegerField(blank=True, null=True)
    sensor_measurement_type = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[External.Equipment.Hobolink.Samples.Raw]'


class FillpumpaRawdata(models.Model):
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.
    dieid = models.CharField(db_column='DieID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cartridgeid = models.CharField(db_column='CartridgeID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    injectionprogram = models.CharField(db_column='InjectionProgram', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pressure = models.CharField(db_column='Pressure', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pressurelimit = models.CharField(db_column='PressureLimit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accumulatedseconds = models.CharField(db_column='AccumulatedSeconds', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accumulatedminutes = models.CharField(db_column='AccumulatedMinutes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accumulatedhours = models.CharField(db_column='AccumulatedHours', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ceramictemperature = models.CharField(db_column='CeramicTemperature', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accelerometerx = models.CharField(db_column='AccelerometerX', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accelerometery = models.CharField(db_column='AccelerometerY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accelerometerz = models.CharField(db_column='AccelerometerZ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vacuum = models.CharField(db_column='Vacuum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    programelapsedtime = models.CharField(db_column='ProgramElapsedTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cartridgeelapsedtime = models.CharField(db_column='CartridgeElapsedTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dailycyclecount = models.CharField(db_column='DailyCycleCount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_0 = models.CharField(db_column='RunMenu_0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    purgevelocity = models.CharField(db_column='PurgeVelocity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cyclestartdelay = models.CharField(db_column='CyclestartDelay', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage0cycledispensedistance = models.CharField(db_column='Stage0CycleDispenseDistance', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage0cyclevelocity = models.CharField(db_column='Stage0CycleVelocity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage0cycleacceleration = models.CharField(db_column='Stage0CycleAcceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage0cycledeceleration = models.CharField(db_column='Stage0CycleDeceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage0cyclepressurelimit = models.CharField(db_column='Stage0CyclePressureLimit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage0endofcyclesettletime = models.CharField(db_column='Stage0EndOfCycleSettleTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage1dispensedistance = models.CharField(db_column='Stage1DispenseDistance', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage1velocity = models.CharField(db_column='Stage1Velocity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage1acceleration = models.CharField(db_column='Stage1Acceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage1deceleration = models.CharField(db_column='Stage1Deceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage1endofcyclesettletime = models.CharField(db_column='Stage1EndOfCycleSettleTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage1cyclepressurelimit = models.CharField(db_column='Stage1CyclePressureLimit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage2dispensedistance = models.CharField(db_column='Stage2DispenseDistance', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage2velocity = models.CharField(db_column='Stage2Velocity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage2acceleration = models.CharField(db_column='Stage2Acceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage2deceleration = models.CharField(db_column='Stage2Deceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage2endofcyclesettletime = models.CharField(db_column='Stage2EndOfCycleSettleTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage2cyclepressurelimit = models.CharField(db_column='Stage2CyclePressureLimit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage3dispensedistance = models.CharField(db_column='Stage3DispenseDistance', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage3velocity = models.CharField(db_column='Stage3Velocity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage3acceleration = models.CharField(db_column='Stage3Acceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage3deceleration = models.CharField(db_column='Stage3Deceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage3endofcyclesettletime = models.CharField(db_column='Stage3EndOfCycleSettleTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage3cyclepressurelimit = models.CharField(db_column='Stage3CyclePressureLimit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cyclecompletehomedelay = models.CharField(db_column='CycleCompleteHomeDelay', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_28 = models.CharField(db_column='RunMenu_28', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_29 = models.CharField(db_column='RunMenu_29', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_30 = models.CharField(db_column='RunMenu_30', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_31 = models.CharField(db_column='RunMenu_31', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_32 = models.CharField(db_column='RunMenu_32', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_33 = models.CharField(db_column='RunMenu_33', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_34 = models.CharField(db_column='RunMenu_34', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_35 = models.CharField(db_column='RunMenu_35', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_36 = models.CharField(db_column='RunMenu_36', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_37 = models.CharField(db_column='RunMenu_37', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_38 = models.CharField(db_column='RunMenu_38', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_39 = models.CharField(db_column='RunMenu_39', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[FillPumpA_RawData]'


class FillpumpbRawdata(models.Model):
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    time = models.TimeField(db_column='Time')  # Field name made lowercase.
    dieid = models.CharField(db_column='DieID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cartridgeid = models.CharField(db_column='CartridgeID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    injectionprogram = models.CharField(db_column='InjectionProgram', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pressure = models.CharField(db_column='Pressure', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pressurelimit = models.CharField(db_column='PressureLimit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accumulatedseconds = models.CharField(db_column='AccumulatedSeconds', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accumulatedminutes = models.CharField(db_column='AccumulatedMinutes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accumulatedhours = models.CharField(db_column='AccumulatedHours', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ceramictemperature = models.CharField(db_column='CeramicTemperature', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accelerometerx = models.CharField(db_column='AccelerometerX', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accelerometery = models.CharField(db_column='AccelerometerY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accelerometerz = models.CharField(db_column='AccelerometerZ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vacuum = models.CharField(db_column='Vacuum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    programelapsedtime = models.CharField(db_column='ProgramElapsedTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cartridgeelapsedtime = models.CharField(db_column='CartridgeElapsedTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dailycyclecount = models.CharField(db_column='DailyCycleCount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_0 = models.CharField(db_column='RunMenu_0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    purgevelocity = models.CharField(db_column='PurgeVelocity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cyclestartdelay = models.CharField(db_column='CyclestartDelay', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage0cycledispensedistance = models.CharField(db_column='Stage0CycleDispenseDistance', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage0cyclevelocity = models.CharField(db_column='Stage0CycleVelocity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage0cycleacceleration = models.CharField(db_column='Stage0CycleAcceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage0cycledeceleration = models.CharField(db_column='Stage0CycleDeceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage0cyclepressurelimit = models.CharField(db_column='Stage0CyclePressureLimit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage0endofcyclesettletime = models.CharField(db_column='Stage0EndOfCycleSettleTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage1dispensedistance = models.CharField(db_column='Stage1DispenseDistance', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage1velocity = models.CharField(db_column='Stage1Velocity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage1acceleration = models.CharField(db_column='Stage1Acceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage1deceleration = models.CharField(db_column='Stage1Deceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage1endofcyclesettletime = models.CharField(db_column='Stage1EndOfCycleSettleTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage1cyclepressurelimit = models.CharField(db_column='Stage1CyclePressureLimit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage2dispensedistance = models.CharField(db_column='Stage2DispenseDistance', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage2velocity = models.CharField(db_column='Stage2Velocity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage2acceleration = models.CharField(db_column='Stage2Acceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage2deceleration = models.CharField(db_column='Stage2Deceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage2endofcyclesettletime = models.CharField(db_column='Stage2EndOfCycleSettleTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage2cyclepressurelimit = models.CharField(db_column='Stage2CyclePressureLimit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage3dispensedistance = models.CharField(db_column='Stage3DispenseDistance', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage3velocity = models.CharField(db_column='Stage3Velocity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage3acceleration = models.CharField(db_column='Stage3Acceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage3deceleration = models.CharField(db_column='Stage3Deceleration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage3endofcyclesettletime = models.CharField(db_column='Stage3EndOfCycleSettleTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage3cyclepressurelimit = models.CharField(db_column='Stage3CyclePressureLimit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cyclecompletehomedelay = models.CharField(db_column='CycleCompleteHomeDelay', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_28 = models.CharField(db_column='RunMenu_28', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_29 = models.CharField(db_column='RunMenu_29', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_30 = models.CharField(db_column='RunMenu_30', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_31 = models.CharField(db_column='RunMenu_31', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_32 = models.CharField(db_column='RunMenu_32', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_33 = models.CharField(db_column='RunMenu_33', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_34 = models.CharField(db_column='RunMenu_34', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_35 = models.CharField(db_column='RunMenu_35', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_36 = models.CharField(db_column='RunMenu_36', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_37 = models.CharField(db_column='RunMenu_37', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_38 = models.CharField(db_column='RunMenu_38', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runmenu_39 = models.CharField(db_column='RunMenu_39', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[FillPumpB_RawData]'


class InsMaster(models.Model):
    ins_plan_number = models.CharField(db_column='INS_Plan_Number', max_length=24, blank=True, null=True)  # Field name made lowercase.
    ins_description = models.CharField(db_column='INS_Description', max_length=250, blank=True, null=True)  # Field name made lowercase.
    pt_number = models.IntegerField(db_column='PT_Number', blank=True, null=True)  # Field name made lowercase.
    ins_requirement_type = models.CharField(db_column='INS_Requirement_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    feature_group = models.CharField(max_length=50, blank=True, null=True)
    ins_characteristic = models.CharField(db_column='INS_Characteristic', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ins_nominal = models.DecimalField(db_column='INS_Nominal', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    ins_nominalabs = models.FloatField(db_column='INS_NominalAbs', blank=True, null=True)  # Field name made lowercase.
    ins_utol = models.DecimalField(db_column='INS_Utol', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    ins_ltol = models.DecimalField(db_column='INS_Ltol', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    ins_upper_bound = models.DecimalField(db_column='INS_Upper_Bound', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    ins_lower_bound = models.DecimalField(db_column='INS_Lower_Bound', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    eng_upper_tol = models.FloatField(db_column='ENG_Upper_Tol', blank=True, null=True)  # Field name made lowercase.
    eng_lower_tol = models.FloatField(db_column='ENG_Lower_Tol', blank=True, null=True)  # Field name made lowercase.
    ins_measure_units = models.CharField(db_column='INS_Measure_Units', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ins_include_in_yield = models.CharField(db_column='INS_Include_In_Yield', max_length=24, blank=True, null=True)  # Field name made lowercase.
    ins_revision = models.IntegerField(db_column='INS_Revision', blank=True, null=True)  # Field name made lowercase.
    ins_method = models.CharField(db_column='INS_Method', max_length=34, blank=True, null=True)  # Field name made lowercase.
    ins_submethod = models.CharField(db_column='INS_SubMethod', max_length=34, blank=True, null=True)  # Field name made lowercase.
    ins_datumref = models.CharField(db_column='INS_Datumref', max_length=34, blank=True, null=True)  # Field name made lowercase.
    ins_samplefreq = models.DecimalField(db_column='INS_SampleFreq', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ins_reportvalue = models.CharField(db_column='INS_ReportValue', max_length=74, blank=True, null=True)  # Field name made lowercase.
    ins_status = models.CharField(db_column='INS_Status', max_length=24, blank=True, null=True)  # Field name made lowercase.
    pk_id = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    guard_upper_tol = models.FloatField(db_column='Guard_Upper_Tol', blank=True, null=True)  # Field name made lowercase.
    guard_lower_tol = models.FloatField(db_column='Guard_Lower_Tol', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[INS_Master]'


class InspectionProcessPlanDetails(models.Model):
    ipp_number = models.CharField(db_column='IPP_number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipp_revision = models.IntegerField(db_column='IPP_revision', blank=True, null=True)  # Field name made lowercase.
    module_revision = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    step_number = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=100, blank=True, null=True)
    required_license = models.CharField(max_length=50, blank=True, null=True)
    instance_type = models.CharField(max_length=100, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Inspection.Process_Plan.Details]'


class InspectionProcessPlanDevelopment(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    ipp_number = models.CharField(db_column='IPP_Number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    part_number = models.CharField(db_column='Part_Number', max_length=15, blank=True, null=True)  # Field name made lowercase.
    process_state = models.CharField(db_column='Process_State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    step_number = models.SmallIntegerField(db_column='Step_Number', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    module = models.CharField(db_column='Module', max_length=100, blank=True, null=True)  # Field name made lowercase.
    required_license = models.CharField(db_column='Required_License', max_length=50, blank=True, null=True)  # Field name made lowercase.
    instance_type = models.CharField(db_column='Instance_Type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    environment = models.CharField(db_column='Environment', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[Inspection.Process_Plan.Development]'


class InspectionProcessPlanMaster(models.Model):
    ipp_id = models.IntegerField(db_column='IPP_id', blank=True, null=True)  # Field name made lowercase.
    ipp_number = models.CharField(db_column='IPP_number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ipp_revision = models.IntegerField(db_column='IPP_revision', blank=True, null=True)  # Field name made lowercase.
    part_number = models.CharField(max_length=50, blank=True, null=True)
    process_state = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Inspection.Process_Plan.Master]'


class MspCoreBom(models.Model):
    pk_id = models.AutoField(primary_key=True)
    bom_id = models.IntegerField(blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    core_id = models.CharField(max_length=50, blank=True, null=True)
    core_qty = models.IntegerField(blank=True, null=True)
    additive = models.CharField(max_length=50, blank=True, null=True)
    machine = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    customer_pn = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[MSP_Core_BOM]'


class MspCoreInventory(models.Model):
    pk_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    core_id = models.CharField(max_length=50, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    tx_type = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    depleted = models.IntegerField(blank=True, null=True)
    inv_week = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[MSP_Core_Inventory]'


class MspCorePart(models.Model):
    pk_id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    core_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[MSP_Core_Part]'


class MspCoreRef(models.Model):
    pk_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[MSP_Core_REF]'


class MspCoreSchedule(models.Model):
    pk_id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    item = models.CharField(max_length=50, blank=True, null=True)
    core_id = models.CharField(max_length=50, blank=True, null=True)
    sch_qty = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    sch_week = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[MSP_Core_Schedule]'


class MtDetails(models.Model):
    mt_metric = models.CharField(db_column='MT_Metric', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mt_test_date = models.DateField(db_column='MT_Test_Date', blank=True, null=True)  # Field name made lowercase.
    mt_test_time = models.TimeField(db_column='MT_Test_Time', blank=True, null=True)  # Field name made lowercase.
    mt_operator = models.CharField(db_column='MT_Operator', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_equipment_id = models.CharField(db_column='MT_Equipment_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wo_project = models.CharField(db_column='WO_Project', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_part_number = models.IntegerField(db_column='MT_Part_Number')  # Field name made lowercase.
    mt_lot_number = models.CharField(db_column='MT_Lot_Number', max_length=50)  # Field name made lowercase.
    mt_container_number = models.IntegerField(db_column='MT_Container_Number', blank=True, null=True)  # Field name made lowercase.
    pr_number = models.IntegerField(db_column='PR_Number', blank=True, null=True)  # Field name made lowercase.
    mt_method = models.CharField(db_column='MT_Method', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mt_sop = models.IntegerField(db_column='MT_SOP', blank=True, null=True)  # Field name made lowercase.
    mt_test_number = models.IntegerField(db_column='MT_Test_Number', blank=True, null=True)  # Field name made lowercase.
    mt_run_number = models.IntegerField(db_column='MT_Run_Number', blank=True, null=True)  # Field name made lowercase.
    mt_value = models.CharField(db_column='MT_Value', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mt_unit = models.CharField(db_column='MT_Unit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_temperature = models.FloatField(db_column='MT_Temperature', blank=True, null=True)  # Field name made lowercase.
    mt_test_comments = models.CharField(db_column='MT_Test_Comments', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    mtiddet = models.AutoField(db_column='MTIDDET', primary_key=True)  # Field name made lowercase.
    mt_temp_ambient = models.FloatField(db_column='MT_Temp_Ambient', blank=True, null=True)  # Field name made lowercase.
    mt_humidity_ambient = models.FloatField(db_column='MT_Humidity_Ambient', blank=True, null=True)  # Field name made lowercase.
    mt_aq_sample_conc = models.FloatField(db_column='MT_Aq_Sample_Conc', blank=True, null=True)  # Field name made lowercase.
    mt_sample_dissolved = models.CharField(db_column='MT_Sample_Dissolved', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_created_by = models.CharField(db_column='MT_Created_By', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_created_date = models.DateField(db_column='MT_Created_Date', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    firing_trial = models.CharField(max_length=50, blank=True, null=True)
    furnace_program = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[MT_Details]'


class MtIfMaster(models.Model):
    mt_part_number = models.IntegerField(db_column='MT_Part_Number')  # Field name made lowercase.
    mt_spec_number = models.CharField(db_column='MT_Spec_Number', max_length=50)  # Field name made lowercase.
    mt_spec_revision = models.IntegerField(db_column='MT_Spec_Revision')  # Field name made lowercase.
    mt_metric = models.CharField(db_column='MT_Metric', max_length=100)  # Field name made lowercase.
    mt_reqd_test = models.CharField(db_column='MT_Reqd_Test', max_length=50)  # Field name made lowercase.
    mt_lower_bound = models.FloatField(db_column='MT_Lower_Bound', blank=True, null=True)  # Field name made lowercase.
    mt_upper_bound = models.FloatField(db_column='MT_Upper_Bound', blank=True, null=True)  # Field name made lowercase.
    mt_text_bound = models.CharField(db_column='MT_Text_Bound', max_length=250, blank=True, null=True)  # Field name made lowercase.
    mt_created_by = models.CharField(db_column='MT_Created_By', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_created_date = models.DateField(db_column='MT_Created_Date', blank=True, null=True)  # Field name made lowercase.
    mt_if_idmas = models.AutoField(db_column='MT_IF_IDMAS', primary_key=True)  # Field name made lowercase.
    mt_unit = models.CharField(db_column='MT_Unit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_sampling_notes = models.CharField(db_column='MT_Sampling_Notes', max_length=250, blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[MT_IF_Master]'


class MtInspectionForms(models.Model):
    mt_part_number = models.IntegerField(db_column='MT_Part_Number')  # Field name made lowercase.
    mt_lot_number = models.CharField(db_column='MT_Lot_Number', max_length=50)  # Field name made lowercase.
    mt_if_category = models.CharField(db_column='MT_IF_Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_inspection_id = models.CharField(db_column='MT_Inspection_ID', max_length=50)  # Field name made lowercase.
    mt_spec_number = models.CharField(db_column='MT_Spec_Number', max_length=50)  # Field name made lowercase.
    mt_spec_revision = models.IntegerField(db_column='MT_Spec_Revision')  # Field name made lowercase.
    mt_if_open_datetime = models.DateTimeField(db_column='MT_IF_Open_Datetime', blank=True, null=True)  # Field name made lowercase.
    mt_created_by = models.CharField(db_column='MT_Created_By', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_if_pass_status = models.CharField(db_column='MT_IF_Pass_Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_if_signature = models.CharField(db_column='MT_IF_Signature', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_if_close_datetime = models.DateTimeField(db_column='MT_IF_Close_Datetime', blank=True, null=True)  # Field name made lowercase.
    mt_if_comments = models.CharField(db_column='MT_IF_Comments', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    mt_if_idform = models.AutoField(db_column='MT_IF_IDFORM', primary_key=True)  # Field name made lowercase.
    mt_expiration_date = models.DateField(db_column='MT_Expiration_Date', blank=True, null=True)  # Field name made lowercase.
    mt_if_due_date = models.DateField(db_column='MT_IF_Due_Date', blank=True, null=True)  # Field name made lowercase.
    ncmr_id = models.IntegerField(db_column='NCMR_ID', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[MT_Inspection_Forms]'


class MtMfgLog(models.Model):
    mt_part_number = models.IntegerField(db_column='MT_Part_Number')  # Field name made lowercase.
    mt_lot_number = models.CharField(db_column='MT_Lot_Number', max_length=50)  # Field name made lowercase.
    mt_mfg_date = models.DateField(db_column='MT_MFG_Date', blank=True, null=True)  # Field name made lowercase.
    mt_operator_1 = models.TextField(db_column='MT_Operator_1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mt_operator_2 = models.TextField(db_column='MT_Operator_2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mt_batch_size_kg = models.FloatField(db_column='MT_Batch_Size_kg', blank=True, null=True)  # Field name made lowercase.
    mt_container_size_gal = models.FloatField(db_column='MT_Container_Size_gal', blank=True, null=True)  # Field name made lowercase.
    mt_container_qty = models.IntegerField(db_column='MT_Container_Qty', blank=True, null=True)  # Field name made lowercase.
    mt_sop = models.IntegerField(db_column='MT_SOP', blank=True, null=True)  # Field name made lowercase.
    rm_part_number = models.IntegerField(db_column='RM_Part_Number')  # Field name made lowercase.
    rm_lot_number = models.CharField(db_column='RM_Lot_Number', max_length=50)  # Field name made lowercase.
    mt_start_date_time = models.DateTimeField(db_column='MT_Start_Date_Time', blank=True, null=True)  # Field name made lowercase.
    mt_end_date_time = models.DateTimeField(db_column='MT_End_Date_Time', blank=True, null=True)  # Field name made lowercase.
    mt_mfg_comments = models.CharField(db_column='MT_MFG_Comments', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    mtidmfg = models.AutoField(db_column='MTIDMFG', primary_key=True)  # Field name made lowercase.
    mt_created_by = models.CharField(db_column='MT_Created_By', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_created_date = models.DateField(db_column='MT_Created_Date', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[MT_MFG_Log]'


class MtMaster(models.Model):
    mt_part_number = models.IntegerField(db_column='MT_Part_Number')  # Field name made lowercase.
    mt_lot_number = models.CharField(db_column='MT_Lot_Number', max_length=50)  # Field name made lowercase.
    mt_lot_notes = models.CharField(db_column='MT_Lot_Notes', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    has_inventory = models.BooleanField(blank=True, null=True)
    mt_created_date = models.DateField(db_column='MT_Created_Date', blank=True, null=True)  # Field name made lowercase.
    mt_created_by = models.CharField(db_column='MT_Created_By', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mtidmas = models.AutoField(db_column='MTIDMAS', primary_key=True)  # Field name made lowercase.
    modified_date = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    link_to_coa = models.CharField(db_column='link_to_COA', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[MT_Master]'


class MtMetricRelationships(models.Model):
    mt_metric = models.CharField(db_column='MT_Metric', max_length=100)  # Field name made lowercase.
    mt_equipment_id = models.CharField(db_column='MT_Equipment_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mt_sop = models.CharField(db_column='MT_SOP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mt_test_method = models.CharField(db_column='MT_Test_Method', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_rel_id = models.IntegerField(db_column='MT_Rel_ID', primary_key=True)  # Field name made lowercase.
    mt_max_value = models.FloatField(db_column='MT_Max_Value', blank=True, null=True)  # Field name made lowercase.
    mt_units = models.CharField(db_column='MT_Units', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[MT_Metric_Relationships]'


class MaterialsSlurryChangelog(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    cartridge_id = models.CharField(max_length=50, blank=True, null=True)
    change_type = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    attribute = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=500, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Materials.Slurry.Changelog]'


class MaterialsSlurryMixMap(models.Model):
    slurry_batch_id = models.CharField(max_length=50, blank=True, null=True)
    formulation_id = models.CharField(max_length=50, blank=True, null=True)
    mix_id = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Materials.Slurry.Mix_Map]'


class PaErrorLog(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    http_response = models.TextField(blank=True, null=True)
    error_kind = models.SmallIntegerField(blank=True, null=True)
    error_message = models.CharField(max_length=500, blank=True, null=True)
    error_loc = models.CharField(max_length=100, blank=True, null=True)
    error_datasource = models.CharField(max_length=100, blank=True, null=True)
    error_procedure = models.CharField(max_length=250, blank=True, null=True)
    relevant_items = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[PA.Error_Log]'


class PaGalleryImagesIndex(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    folder_name = models.CharField(max_length=200, blank=True, null=True)
    qty_imgs = models.SmallIntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=200, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[PA.Gallery_Images_Index]'


class PaRefTimeClockByProcessArea(models.Model):
    system = models.CharField(max_length=100, blank=True, null=True)
    process_state = models.CharField(max_length=100, blank=True, null=True)
    process_step_name = models.CharField(max_length=100, blank=True, null=True)
    clocked_in_max_duration_minutes = models.SmallIntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=100, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[PA.Ref.Time_Clock_by_Process_Area]'


class PaTimeClockByProcessArea(models.Model):
    system = models.CharField(max_length=100, blank=True, null=True)
    process_state = models.CharField(max_length=100, blank=True, null=True)
    process_step_name = models.CharField(max_length=100, blank=True, null=True)
    clock_in_datetime = models.DateTimeField(blank=True, null=True)
    clock_out_datetime = models.DateTimeField(blank=True, null=True)
    self_logout = models.BooleanField(blank=True, null=True)
    employee_id = models.SmallIntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=20, blank=True, null=True)
    part_id = models.CharField(max_length=20, blank=True, null=True)
    attribute = models.CharField(max_length=100, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[PA.Time_Clock_by_Process_Area]'


class PlyAgedInventory(models.Model):
    transaction_id = models.FloatField(db_column='TRANSACTION_ID')  # Field name made lowercase.
    organization_code = models.CharField(db_column='ORGANIZATION_CODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    segment1 = models.CharField(db_column='SEGMENT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    planner_code = models.CharField(db_column='PLANNER_CODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subinventory_code = models.CharField(db_column='SUBINVENTORY_CODE', max_length=255)  # Field name made lowercase.
    locator = models.CharField(db_column='LOCATOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lot_number = models.CharField(db_column='LOT_NUMBER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    expiration_date = models.DateTimeField(db_column='EXPIRATION_DATE', blank=True, null=True)  # Field name made lowercase.
    uom = models.CharField(db_column='UOM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unit_cost = models.FloatField(db_column='UNIT_COST', blank=True, null=True)  # Field name made lowercase.
    received_on = models.DateTimeField(db_column='RECEIVED_ON', blank=True, null=True)  # Field name made lowercase.
    age = models.FloatField(db_column='AGE', blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    net_value = models.FloatField(db_column='NET_VALUE', blank=True, null=True)  # Field name made lowercase.
    open_orders = models.CharField(db_column='OPEN_ORDERS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    material_acct = models.CharField(db_column='MATERIAL_ACCT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    data_transfer_time = models.DateTimeField(db_column='DATA_TRANSFER_TIME', blank=True, null=True)  # Field name made lowercase.
    pk_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = '[PLY_Aged_Inventory]'


class PlyExportItemCost(models.Model):
    item_num = models.CharField(db_column='ITEM_NUM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uom = models.CharField(db_column='UOM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descrip = models.CharField(db_column='DESCRIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shrinkage = models.FloatField(db_column='SHRINKAGE', blank=True, null=True)  # Field name made lowercase.
    op_seq = models.CharField(db_column='OP_SEQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    op_level = models.CharField(db_column='OP_LEVEL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cst_elem = models.CharField(db_column='CST_ELEM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cst_code = models.CharField(db_column='CST_CODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uom2 = models.CharField(db_column='UOM2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    basis = models.CharField(db_column='BASIS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source_type = models.CharField(db_column='SOURCE_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lot_size = models.FloatField(db_column='LOT_SIZE', blank=True, null=True)  # Field name made lowercase.
    bas_factor = models.FloatField(db_column='BAS_FACTOR', blank=True, null=True)  # Field name made lowercase.
    res_cst = models.FloatField(db_column='RES_CST', blank=True, null=True)  # Field name made lowercase.
    rate = models.CharField(db_column='RATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    matl_ovhd = models.FloatField(db_column='MATL_OVHD', blank=True, null=True)  # Field name made lowercase.
    unit_cst = models.FloatField(db_column='UNIT_CST', blank=True, null=True)  # Field name made lowercase.
    activity = models.CharField(db_column='ACTIVITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    output_meas = models.CharField(db_column='OUTPUT_MEAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    num_items = models.CharField(db_column='NUM_ITEMS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    act_per_item = models.CharField(db_column='ACT_PER_ITEM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    c_matl = models.FloatField(db_column='C_MATL', blank=True, null=True)  # Field name made lowercase.
    c_matl_ovhd = models.FloatField(db_column='C_MATL_OVHD', blank=True, null=True)  # Field name made lowercase.
    c_resource = models.FloatField(db_column='C_RESOURCE', blank=True, null=True)  # Field name made lowercase.
    c_outside = models.FloatField(db_column='C_OUTSIDE', blank=True, null=True)  # Field name made lowercase.
    c_ovhd = models.FloatField(db_column='C_OVHD', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TIMESTAMP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[PLY_Export_Item_Cost]'


class PlyLastWipActivity(models.Model):
    transaction_id = models.FloatField(db_column='TRANSACTION_ID', blank=True, null=True)  # Field name made lowercase.
    item = models.CharField(db_column='ITEM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    inventory_item_id = models.FloatField(db_column='INVENTORY_ITEM_ID', blank=True, null=True)  # Field name made lowercase.
    organization_id = models.FloatField(db_column='ORGANIZATION_ID', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PARTNO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    trial_lot_number = models.CharField(db_column='TRIAL_LOT_NUMBER', max_length=150, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=240, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=240, blank=True, null=True)  # Field name made lowercase.
    wip_entity_id = models.FloatField(db_column='WIP_ENTITY_ID', blank=True, null=True)  # Field name made lowercase.
    wip_lot_number = models.CharField(db_column='WIP_LOT_NUMBER', max_length=80, blank=True, null=True)  # Field name made lowercase.
    job_description = models.CharField(db_column='JOB_DESCRIPTION', max_length=240, blank=True, null=True)  # Field name made lowercase.
    job_type = models.CharField(db_column='JOB_TYPE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    class_code = models.CharField(db_column='CLASS_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    job_status = models.CharField(db_column='JOB_STATUS', max_length=80, blank=True, null=True)  # Field name made lowercase.
    hold_reason = models.CharField(db_column='HOLD_REASON', max_length=240, blank=True, null=True)  # Field name made lowercase.
    job_created = models.DateField(db_column='JOB_CREATED', blank=True, null=True)  # Field name made lowercase.
    job_released = models.DateField(db_column='JOB_RELEASED', blank=True, null=True)  # Field name made lowercase.
    job_last_updated = models.DateField(db_column='JOB_LAST_UPDATED', blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='DEPARTMENT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    operation_sequence_id = models.FloatField(db_column='OPERATION_SEQUENCE_ID', blank=True, null=True)  # Field name made lowercase.
    operation_sequence_num = models.FloatField(db_column='OPERATION_SEQUENCE_NUM', blank=True, null=True)  # Field name made lowercase.
    job_last_moved = models.DateField(db_column='JOB_LAST_MOVED', blank=True, null=True)  # Field name made lowercase.
    last_activity_date = models.DateField(db_column='LAST_ACTIVITY_DATE', blank=True, null=True)  # Field name made lowercase.
    last_touch = models.FloatField(db_column='LAST_TOUCH', blank=True, null=True)  # Field name made lowercase.
    qty_start = models.FloatField(db_column='QTY_START', blank=True, null=True)  # Field name made lowercase.
    qty_wip = models.FloatField(db_column='QTY__WIP', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    qty_shipped = models.CharField(db_column='QTY_SHIPPED', max_length=40, blank=True, null=True)  # Field name made lowercase.
    qty_scrap = models.CharField(db_column='QTY_SCRAP', max_length=40, blank=True, null=True)  # Field name made lowercase.
    prod_family = models.CharField(db_column='PROD_FAMILY', max_length=40, blank=True, null=True)  # Field name made lowercase.
    prod_code = models.CharField(db_column='PROD_CODE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    business_unit = models.CharField(db_column='BUSINESS_UNIT', max_length=40, blank=True, null=True)  # Field name made lowercase.
    open_sales_orders = models.CharField(db_column='OPEN_SALES_ORDERS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    wipvalue = models.FloatField(db_column='WIPVALUE', blank=True, null=True)  # Field name made lowercase.
    serial_number = models.CharField(db_column='SERIAL_NUMBER', max_length=240, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    data_transfer_time = models.DateTimeField(db_column='DATA_TRANSFER_TIME', blank=True, null=True)  # Field name made lowercase.
    pk_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = '[PLY_Last_WIP_Activity]'


class ProdDocCurrentrevLog(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.
    currentrev = models.IntegerField(db_column='CurrentRev', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[PROD_Doc_CurrentRev_Log]'


class ProdTrainingattendees(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectID', blank=True, null=True)  # Field name made lowercase.
    sessionid = models.IntegerField(db_column='SessionID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    required = models.CharField(db_column='Required', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trainsubject = models.CharField(db_column='TrainSubject', max_length=50, blank=True, null=True)  # Field name made lowercase.
    attendee = models.CharField(db_column='Attendee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=50, blank=True, null=True)  # Field name made lowercase.
    traindate = models.DateField(db_column='TrainDate', blank=True, null=True)  # Field name made lowercase.
    competence = models.CharField(db_column='Competence', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modified = models.DateTimeField(db_column='Modified', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    employee_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[PROD_TrainingAttendees]'


class ProdTrainingrecords(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectID', blank=True, null=True)  # Field name made lowercase.
    sessionid = models.IntegerField(db_column='SessionID', blank=True, null=True)  # Field name made lowercase.
    completed = models.CharField(db_column='Completed', max_length=10, blank=True, null=True)  # Field name made lowercase.
    completedate = models.DateField(db_column='CompleteDate', blank=True, null=True)  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    competencelevel = models.IntegerField(db_column='CompetenceLevel', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sop = models.CharField(db_column='SOP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    soprev = models.IntegerField(db_column='SOPRev', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=250, blank=True, null=True)  # Field name made lowercase.
    title = models.IntegerField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    employee_id = models.IntegerField(blank=True, null=True)
    conditional_signoff = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[PROD_TrainingRecords]'


class ProdTrainingrecordsDocuments(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recordid = models.IntegerField(db_column='RecordID')  # Field name made lowercase.
    subjectid = models.SmallIntegerField(db_column='SubjectID', blank=True, null=True)  # Field name made lowercase.
    document = models.CharField(db_column='Document', max_length=50, blank=True, null=True)  # Field name made lowercase.
    docrev = models.SmallIntegerField(db_column='DocRev', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[PROD_TrainingRecords_Documents]'


class ProdTrainingsession(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=100, blank=True, null=True)  # Field name made lowercase.
    subjectid = models.SmallIntegerField(db_column='SubjectID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    trainer = models.CharField(db_column='Trainer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    traineracknowledge = models.CharField(db_column='TrainerAcknowledge', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trainmaterial = models.CharField(db_column='TrainMaterial', max_length=250, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=250, blank=True, null=True)  # Field name made lowercase.
    effectiveness = models.CharField(db_column='Effectiveness', max_length=250, blank=True, null=True)  # Field name made lowercase.
    competencelevel = models.SmallIntegerField(db_column='CompetenceLevel', blank=True, null=True)  # Field name made lowercase.
    trainer_id = models.SmallIntegerField(blank=True, null=True)
    req_conditional_signoff = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[PROD_TrainingSession]'


class PtoMaster(models.Model):
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    employee_email = models.CharField(db_column='Employee_Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    approver_email = models.CharField(db_column='Approver_Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    employee_name = models.CharField(db_column='Employee_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pto_start_date = models.DateTimeField(db_column='PTO_Start_Date', blank=True, null=True)  # Field name made lowercase.
    pto_end_date = models.DateTimeField(db_column='PTO_End_Date', blank=True, null=True)  # Field name made lowercase.
    pto_notes = models.CharField(db_column='PTO_Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    approval_status = models.CharField(db_column='Approval_Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    approver = models.CharField(db_column='Approver', max_length=255, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    ptoid = models.AutoField(db_column='PTOID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[PTO_Master]'


class Poly6ApprovalsMaster(models.Model):
    system = models.CharField(max_length=50, blank=True, null=True)
    approval_type = models.CharField(max_length=50, blank=True, null=True)
    sub_type = models.CharField(max_length=50, blank=True, null=True)
    unique_id = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    assigned_approver = models.CharField(max_length=50, blank=True, null=True)
    approval_status = models.CharField(max_length=50, blank=True, null=True)
    approval_datetime = models.DateTimeField(blank=True, null=True)
    approval_auth = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.Approvals.Master]'


class Poly6AutomationPrintingJobs(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    automation_name = models.CharField(max_length=50, blank=True, null=True)
    automation_description = models.TextField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    destination = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    printed = models.BooleanField(blank=True, null=True)
    created_datatime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.Automation.Printing_Jobs]'


class Poly6AutomationTasks(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    automation_name = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    completed = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.Automation.Tasks]'


class Poly6B9ActivePrinterStatusChangelog(models.Model):
    printer_name = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    query_name = models.CharField(max_length=100, blank=True, null=True)
    query_datetime = models.DateTimeField(blank=True, null=True)
    status_code = models.CharField(max_length=20, blank=True, null=True)
    reason_phrase = models.CharField(max_length=100, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Poly6.B9.Active_Printer.Status.Changelog]'


class Poly6B9ActivePrinterDataRaw(models.Model):
    printer_name = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    print_file = models.CharField(max_length=50, blank=True, null=True)
    material_package = models.CharField(max_length=50, blank=True, null=True)
    print_start_datetime = models.DateTimeField(blank=True, null=True)
    print_end_datetime = models.DateTimeField(blank=True, null=True)
    quality_name = models.CharField(max_length=50, blank=True, null=True)
    current_layer = models.IntegerField(blank=True, null=True)
    paused = models.BooleanField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Poly6.B9.Active_Printer_Data.Raw]'


class Poly6B9EspDataDetails(models.Model):
    testkeyvalue = models.CharField(db_column='TestKeyValue', max_length=50)  # Field name made lowercase.
    square = models.IntegerField(db_column='Square', blank=True, null=True)  # Field name made lowercase.
    ln_dose = models.CharField(db_column='ln_Dose', max_length=50, blank=True, null=True)  # Field name made lowercase.
    measured = models.CharField(db_column='Measured', max_length=50, blank=True, null=True)  # Field name made lowercase.
    esp_a = models.CharField(db_column='ESP_A', max_length=50, blank=True, null=True)  # Field name made lowercase.
    esp_b = models.CharField(db_column='ESP_B', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_datetime = models.DateTimeField(db_column='Created_Datetime', blank=True, null=True)  # Field name made lowercase.
    pk_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Poly6.B9.ESP_Data.Details]'


class Poly6B9EspDataMaster(models.Model):
    testkeyvalue = models.CharField(db_column='TestKeyValue', max_length=50)  # Field name made lowercase.
    test_date = models.CharField(db_column='Test_Date', max_length=50)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=50, blank=True, null=True)  # Field name made lowercase.
    printer_type = models.CharField(db_column='Printer_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    printer_id = models.CharField(db_column='Printer_ID', max_length=50)  # Field name made lowercase.
    resin_type = models.CharField(db_column='Resin_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resin_lot = models.CharField(db_column='Resin_Lot', max_length=50)  # Field name made lowercase.
    resin_bottle = models.CharField(db_column='Resin_Bottle', max_length=50)  # Field name made lowercase.
    date_produced = models.CharField(db_column='Date_Produced', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date_expire = models.CharField(db_column='Date_Expire', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vat_type = models.CharField(db_column='Vat_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vat_num = models.CharField(db_column='Vat_Num', max_length=50)  # Field name made lowercase.
    single_exposure = models.CharField(db_column='Single_Exposure', max_length=50)  # Field name made lowercase.
    temperature = models.CharField(db_column='Temperature', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dp = models.CharField(db_column='Dp', max_length=50)  # Field name made lowercase.
    iy = models.CharField(db_column='Iy', max_length=50)  # Field name made lowercase.
    ec = models.CharField(db_column='Ec', max_length=50)  # Field name made lowercase.
    rsq = models.CharField(db_column='RSQ', max_length=50)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=200, blank=True, null=True)  # Field name made lowercase.
    created_datetime = models.DateTimeField(db_column='Created_Datetime')  # Field name made lowercase.
    pk_id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Poly6.B9.ESP_Data.Master]'


class Poly6B9MaterialSettingChangelog(models.Model):
    printer_name = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    material_setting = models.CharField(max_length=50, blank=True, null=True)
    change_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Poly6.B9.Material_Setting.Changelog]'


class Poly6B9PrintDataRaw(models.Model):
    printer_name = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    print_file = models.CharField(max_length=50, blank=True, null=True)
    material_settings = models.CharField(max_length=50, blank=True, null=True)
    print_start_datetime = models.DateTimeField(blank=True, null=True)
    print_end_datetime = models.DateTimeField(blank=True, null=True)
    outcome = models.CharField(max_length=25, blank=True, null=True)
    layers_printed = models.IntegerField(blank=True, null=True)
    total_layers = models.IntegerField(blank=True, null=True)
    quality_name = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Poly6.B9.Print_Data.Raw]'


class Poly6B9PrintFileChangelog(models.Model):
    printer_name = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    print_file = models.CharField(max_length=50, blank=True, null=True)
    change_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Poly6.B9.Print_File.Changelog]'


class Poly6B9PrinterStatsChangelog(models.Model):
    printer_name = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    print_time = models.BigIntegerField(blank=True, null=True)
    disk_usage = models.CharField(max_length=20, blank=True, null=True)
    finished_prints = models.IntegerField(blank=True, null=True)
    attempted_prints = models.IntegerField(blank=True, null=True)
    aborted_prints = models.IntegerField(blank=True, null=True)
    change_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Poly6.B9.Printer_Stats.Changelog]'


class Poly6DuravatInspection(models.Model):
    equip_id = models.CharField(max_length=10, blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.Duravat_Inspection]'


class Poly6MaintenanceMaster(models.Model):
    system = models.CharField(max_length=50, blank=True, null=True)
    maint_type = models.CharField(max_length=50, blank=True, null=True)
    value_type = models.CharField(max_length=50, blank=True, null=True)
    filter_1 = models.CharField(max_length=50, blank=True, null=True)
    filter_2 = models.CharField(max_length=50, blank=True, null=True)
    filter_3 = models.CharField(max_length=50, blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    notes = models.CharField(max_length=250, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.Maintenance.Master]'


class Poly6PartSelectionRef(models.Model):
    system = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    part_id = models.CharField(max_length=50, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    job_number = models.CharField(max_length=50, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    patch_cycle = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    process_pk_id = models.IntegerField(blank=True, null=True)
    master_pk_id = models.IntegerField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.Part_Selection_Ref]'


class Poly6RefApprovalsMaster(models.Model):
    system = models.CharField(max_length=50, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    approval_type = models.CharField(max_length=50, blank=True, null=True)
    sub_type = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    assigned_approver = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.Ref.Approvals.Master]'


class Poly6RefAutomationProfileMap(models.Model):
    automation_profile = models.CharField(max_length=50, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    approved_scanners = models.CharField(max_length=100, blank=True, null=True)
    approved_fixtures = models.CharField(max_length=100, blank=True, null=True)
    fixture_max_qty = models.IntegerField(blank=True, null=True)
    feature_groups = models.TextField(blank=True, null=True)
    required_filter = models.CharField(max_length=10, blank=True, null=True)
    validated = models.BooleanField(blank=True, null=True)
    automated = models.BooleanField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    ins_requirement_type = models.CharField(db_column='INS_Requirement_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[Poly6.Ref.Automation_Profile_Map]'


class Poly6RefAutomationProfileMapDetails(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    automation_profile = models.CharField(max_length=50, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.Ref.Automation_Profile_Map.Details]'


class Poly6RefDailythroughputtargets(models.Model):
    seq_num = models.IntegerField(db_column='Seq_Num')  # Field name made lowercase.
    daily_target = models.IntegerField(db_column='Daily_Target')  # Field name made lowercase.
    weekly_target = models.IntegerField(db_column='Weekly_Target')  # Field name made lowercase.
    effective_date = models.DateTimeField(db_column='Effective_Date', blank=True, null=True)  # Field name made lowercase.
    rev = models.IntegerField(db_column='Rev')  # Field name made lowercase.
    created_date = models.DateTimeField()
    pk_id = models.BigIntegerField(primary_key=True)
    part_number = models.CharField(db_column='Part_Number', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[Poly6.Ref.DailyThroughputTargets]'


class Poly6RefDepartments(models.Model):
    deptid = models.CharField(db_column='DeptID', max_length=20)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=50)  # Field name made lowercase.
    depttype = models.CharField(db_column='DeptType', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[Poly6.Ref.Departments]'


class Poly6RefFiringFixturesMap(models.Model):
    part_number = models.CharField(max_length=50, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    process_state = models.CharField(max_length=20, blank=True, null=True)
    approved_fixture = models.CharField(max_length=50, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.Ref.Firing_Fixtures_Map]'


class Poly6RefMaster(models.Model):
    system = models.CharField(max_length=50, blank=True, null=True)
    filter_1 = models.CharField(max_length=50, blank=True, null=True)
    filter_2 = models.CharField(max_length=50, blank=True, null=True)
    filter_3 = models.CharField(max_length=50, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    attribute = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.Ref.Master]'
        db_table_comment = 'Master table for storing small]'


class Poly6RefPartNumberDescriptions(models.Model):
    internal_part_number = models.CharField(max_length=50, blank=True, null=True)
    customer_part_number = models.CharField(max_length=50, blank=True, null=True)
    customer_program = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    oracle_description = models.CharField(max_length=100, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Poly6.Ref.Part_Number_Descriptions]'


class Poly6SprocHistoryMaster(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    sproc_name = models.CharField(max_length=100, blank=True, null=True)
    query_body = models.TextField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.SProc_History.Master]'


class Poly6StateChange(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    filter_1 = models.TextField(blank=True, null=True)
    filter_2 = models.CharField(max_length=50, blank=True, null=True)
    filter_3 = models.CharField(max_length=50, blank=True, null=True)
    attribute = models.CharField(max_length=100, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    operator = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    resolved_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.State_Change]'


class Poly6StateChangeDuplicates(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=50, blank=True, null=True)
    duplicates = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    created_by = models.TextField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    resolved_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.State_Change.Duplicates]'


class Poly6StateChangePartQtyMismatches(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    job_number = models.CharField(max_length=20, blank=True, null=True)
    master_table_name = models.CharField(max_length=100, blank=True, null=True)
    master_table_qty = models.IntegerField(blank=True, null=True)
    process_table_name = models.CharField(max_length=100, blank=True, null=True)
    process_table_qty = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    operator = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    resolved_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.State_Change.Part_QTY_Mismatches]'


class Poly6Users(models.Model):
    employee_id = models.IntegerField()
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    useremail = models.CharField(db_column='UserEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(max_length=50, blank=True, null=True)
    active = models.CharField(db_column='Active', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pin = models.CharField(db_column='Pin', max_length=4, blank=True, null=True)  # Field name made lowercase.
    pk_id = models.IntegerField(primary_key=True)
    default_site = models.CharField(db_column='Default_Site', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[Poly6.Users]'


class Poly6UsersPermissions(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)
    system = models.CharField(max_length=50, blank=True, null=True)
    permission_type = models.CharField(max_length=50, blank=True, null=True)
    permission_level = models.CharField(max_length=50, blank=True, null=True)
    permission_expiration_date = models.DateField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Poly6.Users.Permissions]'


class QmsApprovedSuppliers(models.Model):
    supplier_id = models.SmallIntegerField()
    title = models.CharField(max_length=100)
    rev = models.SmallIntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    step = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50)
    category = models.CharField(max_length=50, blank=True, null=True)
    supplier_level = models.SmallIntegerField(blank=True, null=True)
    scope = models.CharField(max_length=100, blank=True, null=True)
    denied_party_screening = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    qual_method = models.CharField(max_length=50, blank=True, null=True)
    qual_by = models.CharField(max_length=50, blank=True, null=True)
    eval_details = models.CharField(max_length=200, blank=True, null=True)
    qual_date = models.DateTimeField(blank=True, null=True)
    qual_expires = models.DateTimeField(blank=True, null=True)
    website = models.CharField(max_length=150, blank=True, null=True)
    contact_name = models.CharField(max_length=50, blank=True, null=True)
    contact_email = models.CharField(max_length=50, blank=True, null=True)
    contact_phone = models.CharField(max_length=50, blank=True, null=True)
    previous_name = models.CharField(max_length=100, blank=True, null=True)
    approval_qa = models.CharField(db_column='approval_QA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approval_datetime = models.DateTimeField(blank=True, null=True)
    preferred = models.BooleanField(blank=True, null=True)
    sole_source = models.BooleanField(blank=True, null=True)
    primary_supplier = models.BooleanField(blank=True, null=True)
    mil_spec = models.BooleanField(blank=True, null=True)
    small_business = models.BooleanField(blank=True, null=True)
    capacity_risk = models.CharField(max_length=50, blank=True, null=True)
    capability_risk = models.CharField(max_length=50, blank=True, null=True)
    quality_risk = models.CharField(max_length=50, blank=True, null=True)
    risk_mitigation = models.TextField(blank=True, null=True)
    customers_specific_to_supplier = models.TextField(blank=True, null=True)
    customers_unavailable_to_supplier = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=50)
    created_datetime = models.DateTimeField()
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[QMS.Approved_Suppliers]'


class QmsCar(models.Model):
    car_id = models.SmallIntegerField(db_column='CAR_ID', blank=True, null=True)  # Field name made lowercase.
    report_link = models.TextField(db_column='Report_Link', blank=True, null=True)  # Field name made lowercase.
    car_type = models.CharField(db_column='CAR_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    problem = models.TextField(db_column='Problem', blank=True, null=True)  # Field name made lowercase.
    containduedate = models.DateTimeField(db_column='ContainDueDate', blank=True, null=True)  # Field name made lowercase.
    containment = models.TextField(db_column='Containment', blank=True, null=True)  # Field name made lowercase.
    containapprovedate = models.DateTimeField(db_column='containApproveDate', blank=True, null=True)  # Field name made lowercase.
    rcduedate = models.DateTimeField(db_column='RCDueDate', blank=True, null=True)  # Field name made lowercase.
    root_cause = models.TextField(db_column='Root_Cause', blank=True, null=True)  # Field name made lowercase.
    rcapprovedate = models.DateTimeField(db_column='RCApproveDate', blank=True, null=True)  # Field name made lowercase.
    caduedate = models.DateTimeField(db_column='CADueDate', blank=True, null=True)  # Field name made lowercase.
    corrective_action = models.TextField(db_column='Corrective_Action', blank=True, null=True)  # Field name made lowercase.
    caapprovedate = models.DateTimeField(db_column='CAApproveDate', blank=True, null=True)  # Field name made lowercase.
    implementduedate = models.DateTimeField(db_column='ImplementDueDate', blank=True, null=True)  # Field name made lowercase.
    implementation = models.TextField(db_column='Implementation', blank=True, null=True)  # Field name made lowercase.
    implementapprovedate = models.DateTimeField(db_column='implementApproveDate', blank=True, null=True)  # Field name made lowercase.
    due_date = models.DateTimeField(db_column='Due_Date', blank=True, null=True)  # Field name made lowercase.
    verify_effectiveness = models.TextField(db_column='Verify_Effectiveness', blank=True, null=True)  # Field name made lowercase.
    closedate = models.DateTimeField(db_column='CloseDate', blank=True, null=True)  # Field name made lowercase.
    assigned_to = models.TextField(db_column='Assigned_to', blank=True, null=True)  # Field name made lowercase.
    assigned_to2 = models.TextField(blank=True, null=True)
    attachments = models.CharField(db_column='Attachments', max_length=5, blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='Created_By', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modified = models.DateTimeField(db_column='Modified', blank=True, null=True)  # Field name made lowercase.
    approve_qa = models.CharField(db_column='Approve_QA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approve_qadate = models.DateTimeField(db_column='Approve_QADate', blank=True, null=True)  # Field name made lowercase.
    approve_eng = models.CharField(db_column='Approve_Eng', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approve_engdate = models.DateTimeField(db_column='Approve_EngDate', blank=True, null=True)  # Field name made lowercase.
    approve_prod = models.CharField(db_column='Approve_Prod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approve_proddate = models.DateTimeField(db_column='Approve_ProdDate', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    pk_id = models.IntegerField(primary_key=True)
    site = models.CharField(db_column='Site', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[QMS.CAR]'


class QmsChangeReviewBoardDetails(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    crb_master_fk_id = models.IntegerField(blank=True, null=True)
    revision = models.SmallIntegerField(blank=True, null=True)
    form_section = models.CharField(max_length=50, blank=True, null=True)
    key = models.SmallIntegerField(blank=True, null=True)
    voided = models.BooleanField(blank=True, null=True)
    attributes = models.CharField(max_length=200, blank=True, null=True)
    value_1 = models.TextField(blank=True, null=True)
    value_2 = models.TextField(blank=True, null=True)
    value_3 = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=250, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[QMS.Change_Review_Board.Details]'


class QmsChangeReviewBoardMaster(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)
    step = models.CharField(max_length=25, blank=True, null=True)
    revision = models.SmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    scope = models.CharField(max_length=100, blank=True, null=True)
    site_locations = models.CharField(max_length=200, blank=True, null=True)
    authorization_datetime = models.DateTimeField(blank=True, null=True)
    authorization_route = models.CharField(max_length=50, blank=True, null=True)
    implementation_datetime = models.DateTimeField(blank=True, null=True)
    closeout_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=250, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=250, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[QMS.Change_Review_Board.Master]'


class QmsDocchangeitems(models.Model):
    changeid = models.IntegerField(db_column='ChangeID', blank=True, null=True)  # Field name made lowercase.
    id = models.SmallIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    documentid = models.CharField(db_column='DocumentID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    documenttitle = models.CharField(db_column='DocumentTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    revfrom = models.CharField(db_column='RevFrom', max_length=3, blank=True, null=True)  # Field name made lowercase.
    revto = models.CharField(db_column='RevTo', max_length=3, blank=True, null=True)  # Field name made lowercase.
    reason = models.TextField(db_column='Reason', blank=True, null=True)  # Field name made lowercase.
    matldispo = models.CharField(db_column='MatlDispo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    draftlink = models.TextField(db_column='DraftLink', blank=True, null=True)  # Field name made lowercase.
    implemented = models.CharField(db_column='Implemented', max_length=1, blank=True, null=True)  # Field name made lowercase.
    modified_datetime = models.DateTimeField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    modified_by = models.CharField(db_column='Modified_By', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[QMS.DocChangeItems]'


class QmsDocumentChange(models.Model):
    change_id = models.SmallIntegerField(db_column='Change_ID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(blank=True, null=True)
    change_type = models.CharField(db_column='Change_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description_of_change = models.TextField(db_column='Description_of_Change', blank=True, null=True)  # Field name made lowercase.
    customer_approval = models.CharField(db_column='Customer_Approval', max_length=10, blank=True, null=True)  # Field name made lowercase.
    risk_capability = models.CharField(db_column='Risk_Capability', max_length=50, blank=True, null=True)  # Field name made lowercase.
    risk_capacity = models.CharField(db_column='Risk_Capacity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    risk_mitigation = models.TextField(db_column='Risk_Mitigation', blank=True, null=True)  # Field name made lowercase.
    approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
    closeddate = models.DateTimeField(db_column='ClosedDate', blank=True, null=True)  # Field name made lowercase.
    bomchange = models.CharField(db_column='BOMChange', max_length=5, blank=True, null=True)  # Field name made lowercase.
    validationrequired = models.CharField(db_column='ValidationRequired', max_length=5, blank=True, null=True)  # Field name made lowercase.
    gm_approval = models.CharField(db_column='GM_Approval', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gm_date = models.DateTimeField(db_column='GM_Date', blank=True, null=True)  # Field name made lowercase.
    qa_approval = models.CharField(db_column='QA_Approval', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qa_date = models.DateTimeField(db_column='QA_Date', blank=True, null=True)  # Field name made lowercase.
    eng_approval = models.CharField(db_column='Eng_Approval', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eng_date = models.DateTimeField(db_column='Eng_Date', blank=True, null=True)  # Field name made lowercase.
    prod_approval = models.CharField(db_column='Prod_Approval', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prod_date = models.DateTimeField(db_column='Prod_Date', blank=True, null=True)  # Field name made lowercase.
    pln_approval = models.CharField(db_column='Pln_Approval', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pln_date = models.DateTimeField(db_column='Pln_date', blank=True, null=True)  # Field name made lowercase.
    owner_approval = models.CharField(db_column='Owner_Approval', max_length=50, blank=True, null=True)  # Field name made lowercase.
    owner_date = models.DateTimeField(db_column='Owner_Date', blank=True, null=True)  # Field name made lowercase.
    it_approval = models.CharField(db_column='IT_Approval', max_length=50, blank=True, null=True)  # Field name made lowercase.
    it_date = models.DateTimeField(db_column='IT_Date', blank=True, null=True)  # Field name made lowercase.
    finance_approval = models.CharField(db_column='Finance_Approval', max_length=50, blank=True, null=True)  # Field name made lowercase.
    finance_date = models.DateTimeField(db_column='Finance_Date', blank=True, null=True)  # Field name made lowercase.
    gm_reqd = models.CharField(db_column='GM_reqd', max_length=5, blank=True, null=True)  # Field name made lowercase.
    qa_reqd = models.CharField(db_column='QA_reqd', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eng_reqd = models.CharField(db_column='Eng_Reqd', max_length=5, blank=True, null=True)  # Field name made lowercase.
    prod_reqd = models.CharField(db_column='Prod_reqd', max_length=5, blank=True, null=True)  # Field name made lowercase.
    pln_reqd = models.CharField(db_column='Pln_reqd', max_length=5, blank=True, null=True)  # Field name made lowercase.
    owner_reqd = models.CharField(db_column='Owner_Reqd', max_length=5, blank=True, null=True)  # Field name made lowercase.
    it_reqd = models.CharField(db_column='IT_reqd', max_length=5, blank=True, null=True)  # Field name made lowercase.
    finance_reqd = models.CharField(db_column='Finance_reqd', max_length=5, blank=True, null=True)  # Field name made lowercase.
    qa_assignee = models.CharField(db_column='QA_Assignee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eng_assignee = models.CharField(db_column='Eng_Assignee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prod_assignee = models.CharField(db_column='Prod_Assignee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pln_assignee = models.CharField(db_column='Pln_Assignee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    own_assignee = models.CharField(db_column='Own_Assignee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    it_assignee = models.CharField(db_column='IT_Assignee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    finance_assignee = models.CharField(db_column='Finance_Assignee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gm_assignee = models.CharField(db_column='GM_Assignee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inspplanupdate = models.CharField(db_column='InspPlanUpdate', max_length=5, blank=True, null=True)  # Field name made lowercase.
    rejected = models.CharField(db_column='Rejected', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rejectedby = models.CharField(db_column='RejectedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rejecteddate = models.DateTimeField(db_column='RejectedDate', blank=True, null=True)  # Field name made lowercase.
    rejectcomment = models.CharField(db_column='RejectComment', max_length=1050, blank=True, null=True)  # Field name made lowercase.
    jsa_required = models.CharField(db_column='JSA_Required', max_length=50, blank=True, null=True)  # Field name made lowercase.
    requested_by = models.TextField(db_column='Requested_By', blank=True, null=True)  # Field name made lowercase.
    requested_by1 = models.CharField(max_length=50, blank=True, null=True)
    id = models.SmallIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    eng_prod_approval = models.CharField(db_column='Eng_Prod_Approval', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eng_prod_date = models.DateTimeField(db_column='Eng_Prod_Date', blank=True, null=True)  # Field name made lowercase.
    eng_prod_assignee = models.CharField(db_column='Eng_Prod_Assignee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eng_prod_reqd = models.CharField(db_column='Eng_Prod_reqd', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[QMS.Document_Change]'


class QmsDocumentLocalLinks(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    doc_id = models.CharField(max_length=50, blank=True, null=True)
    rev_num = models.SmallIntegerField(blank=True, null=True)
    doc_name = models.CharField(max_length=1000, blank=True, null=True)
    doc_ext = models.CharField(max_length=50, blank=True, null=True)
    doc_filepath = models.CharField(max_length=2000, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[QMS.Document_Local_Links]'


class QmsDocumentNumberLog(models.Model):
    id = models.SmallIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.
    currentrev = models.CharField(db_column='CurrentRev', max_length=5, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    doc_type = models.CharField(db_column='Doc_type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastreview = models.DateTimeField(db_column='LastReview', blank=True, null=True)  # Field name made lowercase.
    lastreviewby = models.CharField(db_column='LastReviewBy', max_length=25, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customerpn = models.CharField(db_column='CustomerPN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trade_secret = models.BooleanField(db_column='Trade_Secret', blank=True, null=True)  # Field name made lowercase.
    iswoh = models.CharField(db_column='isWOH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=10, blank=True, null=True)  # Field name made lowercase.
    docowner = models.CharField(db_column='DocOwner', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cpp_pn = models.CharField(db_column='CPP_PN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    corecadfile = models.TextField(db_column='CoreCADFile', blank=True, null=True)  # Field name made lowercase.
    favorite = models.CharField(db_column='Favorite', max_length=5, blank=True, null=True)  # Field name made lowercase.
    operationid = models.CharField(db_column='OperationID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    productionpart = models.BooleanField(db_column='ProductionPart', blank=True, null=True)  # Field name made lowercase.
    site = models.CharField(db_column='Site', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[QMS.Document_Number_Log]'


class QmsDocumentNumberLogPartDetails(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    doc_number_log_id = models.IntegerField(blank=True, null=True)
    part_number = models.CharField(max_length=20, blank=True, null=True)
    part_type = models.CharField(max_length=20, blank=True, null=True)
    add_to_oracle = models.BooleanField(blank=True, null=True)
    supplier_id_key = models.SmallIntegerField(blank=True, null=True)
    supplier_item_num = models.CharField(max_length=20, blank=True, null=True)
    equip_id = models.CharField(max_length=20, blank=True, null=True)
    poc_engr_email = models.TextField(blank=True, null=True)
    poc_supply_chain_email = models.TextField(blank=True, null=True)
    created_by = models.TextField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.TextField(blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[QMS.Document_Number_Log.Part_Details]'


class QmsEquipment(models.Model):
    equipid = models.CharField(db_column='EquipID', max_length=50)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equipno = models.SmallIntegerField(db_column='EquipNo', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sitelocation = models.CharField(db_column='SiteLocation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serial_number = models.CharField(db_column='Serial_Number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    servicesupplier = models.CharField(db_column='ServiceSupplier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    in_service = models.BooleanField(db_column='In_Service', blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equiptype = models.CharField(db_column='EquipType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equipowner = models.CharField(db_column='EquipOwner', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    site = models.CharField(db_column='Site', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[QMS.Equipment]'


class QmsEquipmentChangelog(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    equip_id = models.CharField(max_length=50, blank=True, null=True)
    type_of_change = models.CharField(max_length=50, blank=True, null=True)
    maint_name = models.CharField(max_length=50, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[QMS.Equipment_Changelog]'


class QmsEquipmentMaintenance(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    equip_id = models.CharField(max_length=50)
    maint_type = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    status = models.CharField(max_length=50, blank=True, null=True)
    method = models.TextField(blank=True, null=True)
    service_supplier = models.CharField(max_length=50, blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    document_link = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[QMS.Equipment_Maintenance]'


class QmsEquipmentMaintenanceOwners(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    maint_id_key = models.IntegerField(blank=True, null=True)
    employee_id = models.SmallIntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    permission_lvl = models.SmallIntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[QMS.Equipment_Maintenance.Owners]'


class QmsEquipmentRecords(models.Model):
    equipmentid = models.CharField(db_column='EquipmentID', max_length=50)  # Field name made lowercase.
    txtype = models.CharField(db_column='TxType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    action_performed = models.TextField(db_column='Action_performed', blank=True, null=True)  # Field name made lowercase.
    date_completed = models.DateTimeField(db_column='Date_Completed', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    completed = models.BooleanField(db_column='Completed', blank=True, null=True)  # Field name made lowercase.
    interval = models.IntegerField(db_column='Interval', blank=True, null=True)  # Field name made lowercase.
    completedby = models.CharField(db_column='CompletedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[QMS.Equipment_Records]'


class QmsEquipmentUpdatesTemp(models.Model):
    column1 = models.SmallIntegerField(blank=True, null=True)
    equipid = models.CharField(db_column='EquipID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equipno = models.SmallIntegerField(db_column='EquipNo', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serial_number = models.CharField(db_column='Serial_Number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    servicesupplier = models.CharField(db_column='ServiceSupplier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    in_service = models.CharField(db_column='In_Service', max_length=50, blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equiptype = models.CharField(db_column='EquipType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equipowner = models.CharField(db_column='EquipOwner', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pk_id = models.SmallIntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.CharField(max_length=50, blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[QMS.Equipment_UPDATES_temp]'


class QmsFqiScanQueue(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    job_number = models.CharField(max_length=25, blank=True, null=True)
    scan_complete = models.BooleanField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    scan_datetime = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[QMS.FQI.Scan_Queue]'


class QmsNcmr(models.Model):
    ncmr_id = models.IntegerField(db_column='NCMR_ID', unique=True, blank=True, null=True)  # Field name made lowercase.
    partid = models.CharField(db_column='PartID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    partrev = models.CharField(db_column='PartRev', max_length=50, blank=True, null=True)  # Field name made lowercase.
    partdescription = models.CharField(db_column='PartDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lot_serno = models.CharField(db_column='Lot_SerNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    uom = models.CharField(db_column='UOM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier = models.CharField(db_column='Supplier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    job_po = models.CharField(db_column='Job_PO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rejectedby = models.CharField(db_column='RejectedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rejectedbyname = models.CharField(db_column='RejectedByName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rejecteddate = models.DateTimeField(db_column='RejectedDate', blank=True, null=True)  # Field name made lowercase.
    rejectloc = models.CharField(db_column='RejectLoc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rejection_source = models.CharField(db_column='Rejection_Source', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rejectcat = models.CharField(db_column='RejectCat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    requirement = models.CharField(db_column='Requirement', max_length=850, blank=True, null=True)  # Field name made lowercase.
    nonconformance = models.CharField(db_column='Nonconformance', max_length=2300, blank=True, null=True)  # Field name made lowercase.
    otheraffected = models.BooleanField(db_column='OtherAffected', blank=True, null=True)  # Field name made lowercase.
    car_id = models.CharField(db_column='CAR_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dispo = models.CharField(db_column='Dispo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dispo_detail = models.CharField(db_column='Dispo_Detail', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    approve_qa = models.CharField(db_column='Approve_QA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approve_qadate = models.DateTimeField(db_column='Approve_QADate', blank=True, null=True)  # Field name made lowercase.
    approve_prod = models.CharField(db_column='Approve_Prod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approve_proddate = models.DateTimeField(db_column='Approve_ProdDate', blank=True, null=True)  # Field name made lowercase.
    approve_eng = models.CharField(db_column='Approve_Eng', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approve_engdate = models.DateTimeField(db_column='Approve_EngDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nctype = models.CharField(db_column='NCType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_inspection_id = models.CharField(db_column='MT_Inspection_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customerapprovalreqd = models.CharField(db_column='CustomerApprovalReqd', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    pk_id = models.IntegerField(primary_key=True)
    site = models.CharField(db_column='Site', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[QMS.NCMR]'


class QmsNcmrLines(models.Model):
    ncmr_id = models.IntegerField(db_column='NCMR_ID', blank=True, null=True)  # Field name made lowercase.
    ncmr_line = models.IntegerField(db_column='NCMR_Line', blank=True, null=True)  # Field name made lowercase.
    serialno = models.CharField(db_column='SerialNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    linenote = models.TextField(db_column='LineNote', blank=True, null=True)  # Field name made lowercase.
    linedisposition = models.CharField(db_column='LineDisposition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modified_datetime = models.DateTimeField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    # pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[QMS.NCMR_Lines]'


class QmsNcmrLinesCopy(models.Model):
    ncmr_id = models.SmallIntegerField(db_column='NCMR_ID')  # Field name made lowercase.
    ncmr_line = models.SmallIntegerField(db_column='NCMR_Line')  # Field name made lowercase.
    serialno = models.CharField(db_column='SerialNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    linenote = models.TextField(db_column='LineNote', blank=True, null=True)  # Field name made lowercase.
    linedisposition = models.CharField(db_column='LineDisposition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modified_datetime = models.DateTimeField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
    # pk_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = '[QMS.NCMR_Lines_Copy]'


class QmsProcessDataVsOperatorTrainingData(models.Model):
    process_table = models.CharField(max_length=100, blank=True, null=True)
    part_id = models.CharField(max_length=20, blank=True, null=True)
    process_state = models.CharField(max_length=50, blank=True, null=True)
    training_doc = models.CharField(max_length=50, blank=True, null=True)
    start_operator = models.CharField(max_length=100, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_operator = models.CharField(max_length=100, blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    start_operator_trained = models.CharField(max_length=20, blank=True, null=True)
    end_operator_trained = models.CharField(max_length=20, blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[QMS.Process_Data_vs_Operator_Training_Data]'


class QmsRefPartNumberToMaintenanceLogs(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    part_number = models.CharField(max_length=20, blank=True, null=True)
    part_num_id = models.IntegerField(blank=True, null=True)
    maint_log_id = models.IntegerField(blank=True, null=True)
    qty = models.SmallIntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[QMS.Ref.Part_Number_to_Maintenance_Logs]'


class RefErrorKinds(models.Model):
    errorkind_enum = models.CharField(db_column='ErrorKind_enum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    value = models.SmallIntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[REF.Error_Kinds]'


class RefMtMetrics(models.Model):
    mt_metric = models.CharField(db_column='MT_Metric', max_length=100)  # Field name made lowercase.
    mt_equipment_id = models.CharField(db_column='MT_Equipment_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mt_sop = models.CharField(db_column='MT_SOP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mt_test_method = models.CharField(db_column='MT_Test_Method', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mt_rel_id = models.AutoField(db_column='MT_Rel_ID', primary_key=True)  # Field name made lowercase.
    mt_max_value = models.FloatField(db_column='MT_Max_Value', blank=True, null=True)  # Field name made lowercase.
    mt_units = models.CharField(db_column='MT_Units', max_length=100, blank=True, null=True)  # Field name made lowercase.
    num_decimal_pts = models.IntegerField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[REF_MT_Metrics]'


class RefMasterDetailsNullId(models.Model):
    part_id = models.CharField(max_length=20, blank=True, null=True)
    configuration_id = models.IntegerField(blank=True, null=True)
    program_number = models.CharField(max_length=10, blank=True, null=True)
    die_revision = models.CharField(max_length=10, blank=True, null=True)
    process_step_num = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    sub_location = models.CharField(max_length=50, blank=True, null=True)
    slurry_batch = models.CharField(max_length=50, blank=True, null=True)
    job_number = models.CharField(max_length=10, blank=True, null=True)
    scrap_step = models.CharField(max_length=50, blank=True, null=True)
    scrap_code = models.CharField(max_length=10, blank=True, null=True)
    scrap_operator = models.CharField(max_length=50, blank=True, null=True)
    scrap_notes = models.CharField(max_length=250, blank=True, null=True)
    scrap_time = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[REF_Master_Details_NULL_ID]'


class RefOracleRouteSteps2(models.Model):
    partnum = models.CharField(db_column='PartNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    process_state_num = models.IntegerField(db_column='Process_State_Num', blank=True, null=True)  # Field name made lowercase.
    process_state = models.CharField(db_column='Process_State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    process_step_name = models.CharField(db_column='Process_Step_Name', max_length=50)  # Field name made lowercase.
    oracle_op_seq_num = models.IntegerField(db_column='Oracle_Op_Seq_Num', blank=True, null=True)  # Field name made lowercase.
    oracle_cost_seq_num = models.IntegerField(db_column='Oracle_Cost_Seq_Num', blank=True, null=True)  # Field name made lowercase.
    oracle_esh_seq_num = models.IntegerField(db_column='Oracle_ESH_Seq_Num', blank=True, null=True)  # Field name made lowercase.
    oracle_op_seq = models.CharField(db_column='Oracle_Op_Seq', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oracle_seq_num = models.FloatField(db_column='Oracle_Seq_Num', blank=True, null=True)  # Field name made lowercase.
    oracle_seq_step = models.CharField(db_column='Oracle_Seq_Step', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pk_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[REF_Oracle_Route_Steps2]'


class RefScriptArchive(models.Model):
    timestamp = models.DateTimeField()
    object_type = models.CharField(max_length=4)
    object_name = models.CharField(max_length=128)
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    def_length = models.BigIntegerField()
    definition = models.TextField()
    pk_id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[REF_Script_Archive]'


class RefSensorpushSensors(models.Model):
    deviceid = models.BigIntegerField(db_column='deviceId')  # Field name made lowercase.
    name = models.CharField(max_length=250, blank=True, null=True)
    sensor_id = models.CharField(max_length=10, blank=True, null=True)
    sensor_location = models.CharField(max_length=100, blank=True, null=True)
    equipment_id = models.CharField(max_length=10, blank=True, null=True)
    pk_id = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[REF_Sensorpush_Sensors]'


class RefTrainroles(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleID', blank=True, null=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectID', blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[REF_TrainRoles]'


class RefTrainEmployeeroles(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleID', blank=True, null=True)  # Field name made lowercase.
    employee_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[REF_Train_EmployeeRoles]'


class RefTrainEmployeesubjects(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectID', blank=True, null=True)  # Field name made lowercase.
    employee_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[REF_Train_EmployeeSubjects]'


class RefTrainRolesSubjects(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    trainroleid = models.IntegerField(db_column='TrainRoleID', blank=True, null=True)  # Field name made lowercase.
    trainsubjectid = models.IntegerField(db_column='TrainSubjectID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[REF_Train_Roles_Subjects]'


class RefTrainSubjectsDocuments(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectID')  # Field name made lowercase.
    document = models.CharField(db_column='Document', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[REF_Train_Subjects_Documents]'


class RefTrainingsubjects(models.Model):
    subjectid = models.IntegerField(db_column='SubjectID')  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=250, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, blank=True, null=True)  # Field name made lowercase.
    document = models.CharField(db_column='Document', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trainingtype = models.CharField(db_column='TrainingType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recurring = models.CharField(db_column='Recurring', max_length=10, blank=True, null=True)  # Field name made lowercase.
    frequency = models.IntegerField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    assessmentmethod = models.CharField(db_column='AssessmentMethod', max_length=250, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=10, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    process_owner = models.IntegerField(blank=True, null=True)
    req_conditional_signoff = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[REF_TrainingSubjects]'


class RefTravelerMap(models.Model):
    part_number = models.CharField(max_length=20, blank=True, null=True)
    process_state = models.CharField(max_length=50, blank=True, null=True)
    process_step_name = models.CharField(max_length=50, blank=True, null=True)
    seq_num = models.CharField(db_column='Seq_Num', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sop = models.CharField(db_column='SOP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pk_id = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[REF_Traveler_Map]'


class RefMapTrainingSubjectToProcess(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    process_table = models.CharField(max_length=50, blank=True, null=True)
    training_doc = models.CharField(max_length=20, blank=True, null=True)
    process_state = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    modified_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Ref.Map.Training_Subject_to_Process]'


class Rheodataraw(models.Model):
    testname = models.CharField(db_column='TestName', max_length=50)  # Field name made lowercase.
    testdate = models.DateTimeField(db_column='TestDate')  # Field name made lowercase.
    testresult = models.CharField(db_column='TestResult', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[RheoDataRaw]'


class ScCtDiagnosticsMaster(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    filename = models.CharField(max_length=100, blank=True, null=True)
    time_started = models.DateTimeField(blank=True, null=True)
    daily_index = models.SmallIntegerField(blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    serial_number = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    head = models.CharField(max_length=20, blank=True, null=True)
    target = models.CharField(max_length=20, blank=True, null=True)
    plc_version = models.CharField(max_length=20, blank=True, null=True)
    base_dll_version = models.CharField(max_length=20, blank=True, null=True)
    date_of_manufacture = models.DateTimeField(blank=True, null=True)
    date_of_installation = models.DateTimeField(blank=True, null=True)
    total_runtime = models.IntegerField(blank=True, null=True)
    total_xray_on_time = models.IntegerField(blank=True, null=True)
    refresh_status = models.CharField(max_length=20, blank=True, null=True)
    filament_adjust_status = models.CharField(max_length=20, blank=True, null=True)
    centering_status = models.CharField(max_length=20, blank=True, null=True)
    filament_value = models.FloatField(blank=True, null=True)
    leakage_current = models.FloatField(blank=True, null=True)
    leakage_current_voltage = models.FloatField(blank=True, null=True)
    leakage_current_status = models.CharField(max_length=20, blank=True, null=True)
    flashovers = models.IntegerField(blank=True, null=True)
    vacuum_start = models.FloatField(blank=True, null=True)
    vacuum_end = models.FloatField(blank=True, null=True)
    filament_correction_factor = models.FloatField(blank=True, null=True)
    centering1_x = models.FloatField(blank=True, null=True)
    centering1_y = models.FloatField(blank=True, null=True)
    centering2_x = models.FloatField(blank=True, null=True)
    centering2_y = models.FloatField(blank=True, null=True)
    centering1_x_status = models.CharField(max_length=20, blank=True, null=True)
    centering1_y_status = models.CharField(max_length=20, blank=True, null=True)
    centering2_x_status = models.CharField(max_length=20, blank=True, null=True)
    centering2_y_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[SC.CT_Diagnostics.Master]'


class ScDetails(models.Model):
    sc_number = models.IntegerField(db_column='SC_Number', blank=True, null=True)  # Field name made lowercase.
    sc_fixture_location = models.IntegerField(db_column='SC_Fixture_Location', blank=True, null=True)  # Field name made lowercase.
    pt_id = models.CharField(db_column='PT_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    process_state = models.CharField(max_length=50, blank=True, null=True)
    pt_mass = models.DecimalField(db_column='PT_Mass', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pt_visual_inspect = models.CharField(db_column='PT_Visual_Inspect', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ptid = models.AutoField(db_column='PTID', primary_key=True)  # Field name made lowercase.
    pr_number = models.IntegerField(db_column='PR_Number', blank=True, null=True)  # Field name made lowercase.
    key_scancav = models.CharField(db_column='KEY_ScanCav', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pt_dimensional_result = models.CharField(db_column='PT_Dimensional_Result', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pt_dimensional_notes = models.CharField(db_column='PT_Dimensional_Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pt_qualify_date = models.DateTimeField(db_column='PT_Qualify_Date', blank=True, null=True)  # Field name made lowercase.
    co_number = models.CharField(db_column='CO_Number', max_length=24, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='Created_By', max_length=88, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.CharField(db_column='Modified_By', max_length=88, blank=True, null=True)  # Field name made lowercase.
    modified = models.DateTimeField(db_column='Modified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[SC_Details]'


class ScDimensional(models.Model):
    sc_number = models.IntegerField(db_column='SC_Number', blank=True, null=True)  # Field name made lowercase.
    pr_cavity_number = models.CharField(db_column='PR_Cavity_Number', max_length=14, blank=True, null=True)  # Field name made lowercase.
    dim_feature = models.CharField(db_column='DIM_Feature', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dim_measured = models.FloatField(db_column='DIM_Measured', blank=True, null=True)  # Field name made lowercase.
    image_index = models.CharField(db_column='Image_Index', max_length=10, blank=True, null=True)  # Field name made lowercase.
    map_scan_cav = models.CharField(db_column='MAP_Scan_Cav', max_length=14, blank=True, null=True)  # Field name made lowercase.
    dimid = models.AutoField(db_column='DimID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[SC_Dimensional]'


class ScDimensionalCleaned(models.Model):
    sc_number = models.IntegerField(db_column='SC_Number', blank=True, null=True)  # Field name made lowercase.
    pr_cavity_number = models.CharField(db_column='PR_Cavity_Number', max_length=14, blank=True, null=True)  # Field name made lowercase.
    dim_feature = models.CharField(db_column='DIM_Feature', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dim_measured = models.FloatField(db_column='DIM_Measured', blank=True, null=True)  # Field name made lowercase.
    image_index = models.CharField(db_column='Image_Index', max_length=10, blank=True, null=True)  # Field name made lowercase.
    map_scan_cav = models.CharField(db_column='MAP_Scan_Cav', max_length=14, blank=True, null=True)  # Field name made lowercase.
    dimid1 = models.IntegerField(db_column='DimID1')  # Field name made lowercase.
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[SC_Dimensional.Cleaned]'


class ScFileindex(models.Model):
    filename = models.CharField(db_column='FileName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=300, blank=True, null=True)  # Field name made lowercase.
    directoryname = models.CharField(db_column='DirectoryName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    directorypath = models.CharField(db_column='DirectoryPath', max_length=300, blank=True, null=True)  # Field name made lowercase.
    extension = models.CharField(db_column='Extension', max_length=20, blank=True, null=True)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime', blank=True, null=True)  # Field name made lowercase.
    lastwritetime = models.DateTimeField(db_column='LastWriteTime', blank=True, null=True)  # Field name made lowercase.
    length = models.CharField(db_column='Length', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[SC_FileIndex]'


class ScFilesizes(models.Model):
    date_time = models.DateTimeField(db_column='Date_Time')  # Field name made lowercase.
    storage_area = models.CharField(db_column='Storage_Area', max_length=50)  # Field name made lowercase.
    totalsizegb = models.FloatField(db_column='TotalSizeGB')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[SC_FileSizes]'


class ScMaster(models.Model):
    sc_number = models.IntegerField(db_column='SC_Number', blank=True, null=True)  # Field name made lowercase.
    sc_part_number = models.IntegerField(db_column='SC_Part_Number', blank=True, null=True)  # Field name made lowercase.
    sc_production_type = models.CharField(db_column='SC_Production_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sc_date = models.DateTimeField(db_column='SC_Date', blank=True, null=True)  # Field name made lowercase.
    sc_scan_operator = models.CharField(db_column='SC_Scan_Operator', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sc_scanner = models.CharField(db_column='SC_Scanner', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sc_fixture = models.CharField(db_column='SC_Fixture', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sc_automation_profile = models.CharField(db_column='SC_Automation_Profile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sc_notes = models.CharField(db_column='SC_Notes', max_length=214, blank=True, null=True)  # Field name made lowercase.
    sc_sop = models.IntegerField(db_column='SC_SOP', blank=True, null=True)  # Field name made lowercase.
    sc_analysis_date = models.DateTimeField(db_column='SC_Analysis_Date', blank=True, null=True)  # Field name made lowercase.
    sc_analysis_notes = models.CharField(db_column='SC_Analysis_Notes', max_length=214, blank=True, null=True)  # Field name made lowercase.
    sc_analysis_operator = models.CharField(db_column='SC_Analysis_Operator', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sc_analysis_sop = models.IntegerField(db_column='SC_Analysis_SOP', blank=True, null=True)  # Field name made lowercase.
    sc_qa_date = models.DateTimeField(db_column='SC_QA_Date', blank=True, null=True)  # Field name made lowercase.
    sc_qa_notes = models.CharField(db_column='SC_QA_Notes', max_length=214, blank=True, null=True)  # Field name made lowercase.
    sc_qa_operator = models.CharField(db_column='SC_QA_Operator', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sc_qa_status = models.CharField(db_column='SC_QA_Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    scid = models.AutoField(db_column='SCID', primary_key=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='Created_By', max_length=88, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.CharField(db_column='Modified_By', max_length=88, blank=True, null=True)  # Field name made lowercase.
    modified = models.DateTimeField(db_column='Modified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[SC_Master]'


class ScTimelog(models.Model):
    machine = models.CharField(max_length=50, blank=True, null=True)
    instance = models.CharField(max_length=50, blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    process_step = models.CharField(max_length=50, blank=True, null=True)
    scan_number = models.IntegerField(blank=True, null=True)
    part_id = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    pk_id = models.BigAutoField(db_column='PK_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[SC_TimeLog]'


class ScanAnalysisErrors(models.Model):
    machine_type = models.CharField(max_length=20, blank=True, null=True)
    machine_name = models.CharField(max_length=50, blank=True, null=True)
    error_type = models.CharField(max_length=50, blank=True, null=True)
    error_description = models.TextField(blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    part_id = models.CharField(max_length=20, blank=True, null=True)
    scan_number = models.IntegerField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Scan.Analysis_Errors]'


class ScanAnalysisQuarantine(models.Model):
    ipp_num = models.CharField(db_column='IPP_Num', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fail_step = models.SmallIntegerField(db_column='Fail_Step', blank=True, null=True)  # Field name made lowercase.
    scan_record = models.CharField(db_column='Scan_Record', max_length=10, blank=True, null=True)  # Field name made lowercase.
    part_number = models.CharField(db_column='Part_Number', max_length=20, blank=True, null=True)  # Field name made lowercase.
    serial_number = models.CharField(db_column='Serial_Number', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fixture_position = models.CharField(db_column='Fixture_Position', max_length=10, blank=True, null=True)  # Field name made lowercase.
    resolution = models.CharField(db_column='Resolution', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[Scan.Analysis_Quarantine]'


class TestJsonToStoredProcPatchAlternative(models.Model):
    source = models.CharField(max_length=100, blank=True, null=True)
    table_name = models.CharField(max_length=200, blank=True, null=True)
    json_body = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    pk_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[TEST.JSON_to_Stored_Proc_Patch_Alternative]'


class WoDetails(models.Model):
    wo_number = models.IntegerField(db_column='WO_Number', blank=True, null=True)  # Field name made lowercase.
    wo_project = models.CharField(db_column='WO_Project', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pr_number = models.IntegerField(db_column='PR_Number', blank=True, null=True)  # Field name made lowercase.
    cl_cycle = models.CharField(db_column='CL_Cycle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cl_notes = models.CharField(db_column='CL_Notes', max_length=214, blank=True, null=True)  # Field name made lowercase.
    cl_operator = models.CharField(db_column='CL_Operator', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cl_solvent_bottle1 = models.IntegerField(db_column='CL_Solvent_Bottle1', blank=True, null=True)  # Field name made lowercase.
    cl_solvent_bottle2 = models.IntegerField(db_column='CL_Solvent_Bottle2', blank=True, null=True)  # Field name made lowercase.
    cl_solvent_lot = models.CharField(db_column='CL_Solvent_Lot', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cl_sop = models.IntegerField(db_column='CL_SOP', blank=True, null=True)  # Field name made lowercase.
    cl_start_time = models.DateTimeField(db_column='CL_Start_Time', blank=True, null=True)  # Field name made lowercase.
    cu_cure_box_1 = models.IntegerField(db_column='CU_Cure_Box_1', blank=True, null=True)  # Field name made lowercase.
    cu_cure_box_2 = models.IntegerField(db_column='CU_Cure_Box_2', blank=True, null=True)  # Field name made lowercase.
    cu_cure_box_3 = models.IntegerField(db_column='CU_Cure_Box_3', blank=True, null=True)  # Field name made lowercase.
    cu_cure_box_4 = models.IntegerField(db_column='CU_Cure_Box_4', blank=True, null=True)  # Field name made lowercase.
    cu_cycle = models.CharField(db_column='CU_Cycle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cu_notes = models.CharField(db_column='CU_Notes', max_length=214, blank=True, null=True)  # Field name made lowercase.
    cu_operator = models.CharField(db_column='CU_Operator', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cu_sop = models.IntegerField(db_column='CU_SOP', blank=True, null=True)  # Field name made lowercase.
    cu_start_time = models.DateTimeField(db_column='CU_Start_Time', blank=True, null=True)  # Field name made lowercase.
    ismassed = models.BooleanField(db_column='isMassed', blank=True, null=True)  # Field name made lowercase.
    isncmr = models.BooleanField(db_column='isNCMR', blank=True, null=True)  # Field name made lowercase.
    pr_airflow_cfm = models.DecimalField(db_column='PR_Airflow_cfm', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pr_buildhead_number = models.IntegerField(db_column='PR_Buildhead_Number', blank=True, null=True)  # Field name made lowercase.
    pr_file = models.CharField(db_column='PR_File', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pr_material_settings = models.CharField(db_column='PR_Material_Settings', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pr_mold_iteration = models.CharField(db_column='PR_Mold_Iteration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pr_notes = models.CharField(db_column='PR_Notes', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pr_operator = models.CharField(db_column='PR_Operator', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pr_part_number = models.CharField(db_column='PR_Part_Number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pr_plan_notes = models.CharField(db_column='PR_Plan_Notes', max_length=214, blank=True, null=True)  # Field name made lowercase.
    pr_plan_time = models.DateTimeField(db_column='PR_Plan_Time', blank=True, null=True)  # Field name made lowercase.
    pr_platform = models.CharField(db_column='PR_Platform', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pr_print_duration_hr = models.DecimalField(db_column='PR_Print_Duration_hr', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pr_printer = models.CharField(db_column='PR_Printer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pr_resin_amount_g = models.DecimalField(db_column='PR_Resin_Amount_g', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pr_resin_lot = models.CharField(db_column='PR_Resin_Lot', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pr_resin_remaining_g = models.DecimalField(db_column='PR_Resin_Remaining_g', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pr_resin_start_g = models.DecimalField(db_column='PR_Resin_Start_g', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pr_slice_thickness = models.DecimalField(db_column='PR_Slice_Thickness', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pr_sop = models.IntegerField(db_column='PR_SOP', blank=True, null=True)  # Field name made lowercase.
    pr_speed_mmh = models.DecimalField(db_column='PR_Speed_mmh', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pr_start_time = models.DateTimeField(db_column='PR_Start_Time', blank=True, null=True)  # Field name made lowercase.
    pr_tray_number = models.IntegerField(db_column='PR_Tray_Number', blank=True, null=True)  # Field name made lowercase.
    sc_iteration_1 = models.IntegerField(db_column='SC_Iteration_1', blank=True, null=True)  # Field name made lowercase.
    sc_iteration_2 = models.IntegerField(db_column='SC_Iteration_2', blank=True, null=True)  # Field name made lowercase.
    sc_iteration_3 = models.IntegerField(db_column='SC_Iteration_3', blank=True, null=True)  # Field name made lowercase.
    sc_iteration_4 = models.IntegerField(db_column='SC_Iteration_4', blank=True, null=True)  # Field name made lowercase.
    sc_iteration_5 = models.IntegerField(db_column='SC_Iteration_5', blank=True, null=True)  # Field name made lowercase.
    sc_plan_date_1 = models.DateTimeField(db_column='SC_Plan_Date_1', blank=True, null=True)  # Field name made lowercase.
    sc_plan_date_2 = models.DateTimeField(db_column='SC_Plan_Date_2', blank=True, null=True)  # Field name made lowercase.
    sc_plan_date_3 = models.DateTimeField(db_column='SC_Plan_Date_3', blank=True, null=True)  # Field name made lowercase.
    sc_plan_date_4 = models.DateTimeField(db_column='SC_Plan_Date_4', blank=True, null=True)  # Field name made lowercase.
    sc_plan_date_5 = models.DateTimeField(db_column='SC_Plan_Date_5', blank=True, null=True)  # Field name made lowercase.
    st_location = models.CharField(db_column='ST_Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    st_notes = models.CharField(db_column='ST_Notes', max_length=214, blank=True, null=True)  # Field name made lowercase.
    st_start_time = models.DateTimeField(db_column='ST_Start_Time', blank=True, null=True)  # Field name made lowercase.
    prid = models.IntegerField(db_column='PRID')  # Field name made lowercase.
    wo_oracle_job_number = models.IntegerField(db_column='WO_Oracle_Job_Number', blank=True, null=True)  # Field name made lowercase.
    ncmr_note = models.CharField(db_column='NCMR_Note', max_length=214, blank=True, null=True)  # Field name made lowercase.
    dy_pressure_start_psi = models.DecimalField(db_column='DY_Pressure_Start_psi', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dy_pressure_end_psi = models.DecimalField(db_column='DY_Pressure_End_psi', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dy_total_flow_cfm = models.DecimalField(db_column='DY_Total_Flow_cfm', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='Created_By', max_length=88, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.CharField(db_column='Modified_By', max_length=88, blank=True, null=True)  # Field name made lowercase.
    modified = models.DateTimeField(db_column='Modified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[WO_Details]'


class WasteInventory(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    waste_code = models.CharField(max_length=50, blank=True, null=True)
    waste_name = models.CharField(max_length=50, blank=True, null=True)
    waste_type = models.CharField(max_length=50, blank=True, null=True)
    qty_oh = models.IntegerField(blank=True, null=True)
    uom = models.CharField(max_length=50, blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    inv_by = models.CharField(max_length=50, blank=True, null=True)
    container = models.CharField(max_length=50, blank=True, null=True)
    site = models.CharField(max_length=50, blank=True, null=True)
    shipped = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    accum_start_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Waste.Inventory]'


class WasteProfile(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    waste_id = models.CharField(max_length=50, blank=True, null=True)
    waste_name = models.CharField(max_length=50, blank=True, null=True)
    waste_code = models.CharField(max_length=50, blank=True, null=True)
    waste_type = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Waste.Profile]'


class WasteRefChoices(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    choice_sort = models.IntegerField(blank=True, null=True)
    choice_type = models.CharField(max_length=50, blank=True, null=True)
    choice_description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Waste.Ref.Choices]'


class WasteShipment(models.Model):
    pk_id = models.IntegerField(primary_key=True)
    ship_id = models.IntegerField(blank=True, null=True)
    waste_id = models.CharField(max_length=50, blank=True, null=True)
    ship_date = models.DateField(blank=True, null=True)
    ship_qty = models.CharField(max_length=50, blank=True, null=True)
    ship_status = models.CharField(max_length=50, blank=True, null=True)
    site = models.CharField(max_length=50, blank=True, null=True)
    source_pk_id = models.IntegerField(blank=True, null=True)
    waste_type = models.CharField(max_length=50, blank=True, null=True)
    waste_name = models.CharField(max_length=50, blank=True, null=True)
    container = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Waste.Shipment]'


class DimPartsEvalArtifactTemp(models.Model):
    scan_number = models.SmallIntegerField(primary_key=True)
    scan_datetime = models.DateTimeField(blank=True, null=True)
    job_number = models.CharField(max_length=50, blank=True, null=True)
    run_number_inclusive = models.SmallIntegerField(blank=True, null=True)
    pass_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[dim_parts_eval_artifact_temp]'


class ScrapCodes(models.Model):
    scrap_code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    active = models.CharField(max_length=10, blank=True, null=True)
    process = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    pk_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = '[scrap_codes]'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[sysdiagrams]'
        unique_together = (('principal_id', 'name'),)


class TestJsonChangelog(models.Model):
    json_body = models.TextField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    pk_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[test_json_changelog]'


class TestTableForVcs(models.Model):
    new_col = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[test_table_for_vcs]'
