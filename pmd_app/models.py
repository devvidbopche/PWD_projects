
from django.db import models


class Asset(models.Model):
    asset_tag = models.CharField(primary_key=True, max_length=5)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    eol = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset'


class AssetLocations(models.Model):
    location_id = models.IntegerField(primary_key=True)
    location_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_locations'


class AssetMovement(models.Model):
    asset_tag = models.CharField(primary_key=True, max_length=5)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    timestamp = models.DateTimeField()
    user = models.CharField(max_length=255, blank=True, null=True)
    moved_from = models.CharField(max_length=255, blank=True, null=True)
    moved_to = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_movement'
        unique_together = (('asset_tag', 'timestamp'),)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'category'


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    sage_supplier_acc_td = models.CharField(max_length=255, blank=True, null=True)
    sage_supplier_acc_ti = models.CharField(max_length=255, blank=True, null=True)
    sage_supplier_acc_tp = models.CharField(max_length=255, blank=True, null=True)
    sage_customer_acc_td = models.CharField(max_length=255, blank=True, null=True)
    sage_customer_acc_ti = models.CharField(max_length=255, blank=True, null=True)
    sage_customer_acc_tp = models.CharField(max_length=255, blank=True, null=True)
    field = models.CharField(db_column='Field', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company'


class CostingSheet(models.Model):
    cs_id = models.AutoField(primary_key=True)
    quote_id = models.IntegerField(blank=True, null=True)
    cs_name = models.CharField(max_length=255, blank=True, null=True)
    date_time_created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    date_time_last_edit = models.DateTimeField(blank=True, null=True)
    last_edit_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'costing_sheet'


class CostingSheetDetails(models.Model):
    cs_element_id = models.AutoField(primary_key=True)
    stage = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    person = models.CharField(max_length=255, blank=True, null=True)
    how_many = models.CharField(max_length=255, blank=True, null=True)
    hours = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    quantity_hotel = models.CharField(max_length=255, blank=True, null=True)
    type_hotel = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'costing_sheet_details'
        unique_together = (('cs_element_id', 'stage', 'detail'),)


class CostingSheetElement(models.Model):
    cs_element_id = models.AutoField(primary_key=True)
    cs_element_name = models.CharField(max_length=255, blank=True, null=True)
    cs_element_type = models.CharField(max_length=255, blank=True, null=True)
    labour_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transport_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    offshore_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fuel_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    consumables_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    expenses_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    other_direct_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    contribution = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'costing_sheet_element'


class EquipmentType(models.Model):
    equipment_type_id = models.IntegerField(primary_key=True)
    section_name = models.CharField(max_length=255, blank=True, null=True)
    section_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment_type'


class ListManager(models.Model):
    lm_id = models.AutoField(primary_key=True)
    lm_name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'list_manager'


class ListManagerElement(models.Model):
    lm_el_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'list_manager_element'


class LoginLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=45)
    login_timestamp = models.DateTimeField()
    success = models.IntegerField()
    message = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'login_log'


class PasswordResets(models.Model):
    reset_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    token = models.CharField(max_length=64)
    expiry_time = models.DateTimeField()
    systemcreateddt = models.DateTimeField(db_column='systemCreatedDT')  # Field name made lowercase.
    systemupdateddt = models.DateTimeField(db_column='systemUpdatedDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'password_resets'


class Permissions(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'permissions'


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    equipment_type = models.ForeignKey(EquipmentType, models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_title = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    stock_check = models.IntegerField(blank=True, null=True)
    install_time = models.CharField(max_length=255, blank=True, null=True)
    check_time = models.CharField(max_length=255, blank=True, null=True)
    removal_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Project(models.Model):
    quote_id = models.AutoField(primary_key=True)
    project_status = models.CharField(max_length=255, blank=True, null=True)
    project_manager = models.CharField(max_length=255, blank=True, null=True)
    analyst = models.CharField(max_length=255, blank=True, null=True)
    project_director = models.CharField(max_length=255, blank=True, null=True)
    project_stage = models.CharField(max_length=255, blank=True, null=True)
    final_data_sent = models.DateField(blank=True, null=True)
    date_prepped = models.DateField(blank=True, null=True)
    survey_description = models.CharField(max_length=255, blank=True, null=True)
    council_contact = models.CharField(max_length=255, blank=True, null=True)
    perm_email_sent = models.DateField(blank=True, null=True)
    highways_contact = models.CharField(max_length=255, blank=True, null=True)
    perm_highway_email = models.CharField(max_length=255, blank=True, null=True)
    perm_contact = models.CharField(max_length=255, blank=True, null=True)
    perm_received = models.DateField(blank=True, null=True)
    perm_paid = models.DateField(blank=True, null=True)
    into_to_client = models.DateField(blank=True, null=True)
    perms_needed = models.CharField(max_length=255, blank=True, null=True)
    roadworks_check = models.DateField(blank=True, null=True)
    dates_confirmed = models.DateField(blank=True, null=True)
    hotel_booked = models.DateField(blank=True, null=True)
    ps_to_analyst = models.DateField(blank=True, null=True)
    tm_required = models.IntegerField(blank=True, null=True)
    tm_contact_name = models.CharField(max_length=255, blank=True, null=True)
    tm_contact = models.CharField(max_length=255, blank=True, null=True)
    tm_email = models.CharField(max_length=255, blank=True, null=True)
    rams_required = models.IntegerField(blank=True, null=True)
    rams_sent = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProposedParking(models.Model):
    resource_id = models.IntegerField(primary_key=True)
    site = models.ForeignKey('Sites', models.DO_NOTHING, blank=True, null=True)
    resource_no = models.CharField(max_length=255, blank=True, null=True)
    resource_name = models.CharField(max_length=255, blank=True, null=True)
    nearest_postcode = models.CharField(max_length=255, blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    screenshot = models.CharField(max_length=255, blank=True, null=True)
    annotation = models.CharField(max_length=255, blank=True, null=True)
    zoom_level = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proposed_parking'


class Recording(models.Model):
    site = models.ForeignKey('Sites', models.DO_NOTHING, blank=True, null=True)
    rec_start = models.DateTimeField(blank=True, null=True)
    rec_end = models.DateTimeField(blank=True, null=True)
    recording_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recording'


class RecordingDatetime(models.Model):
    site = models.ForeignKey('Sites', models.DO_NOTHING, blank=True, null=True)
    rec_start = models.DateTimeField(blank=True, null=True)
    rec_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recording_datetime'


class Resources(models.Model):
    resource_id = models.IntegerField(primary_key=True)
    site = models.ForeignKey('Sites', models.DO_NOTHING, blank=True, null=True)
    resource_no = models.CharField(max_length=255, blank=True, null=True)
    resource_name = models.CharField(max_length=255, blank=True, null=True)
    nearest_postcode = models.CharField(max_length=255, blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    pin_orientation = models.CharField(max_length=255, blank=True, null=True)
    screenshot = models.CharField(max_length=255, blank=True, null=True)
    annotation = models.CharField(max_length=255, blank=True, null=True)
    zoom_level = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resources'


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    createddt = models.DateTimeField(db_column='createdDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roles'


class Sites(models.Model):
    site_id = models.IntegerField(primary_key=True)
    cs = models.ForeignKey(CostingSheet, models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)
    site_no = models.CharField(max_length=255, blank=True, null=True)
    shape = models.CharField(max_length=255, blank=True, null=True)
    site_name = models.CharField(max_length=255, blank=True, null=True)
    equipment_type = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=255, blank=True, null=True)
    mast = models.CharField(max_length=255, blank=True, null=True)
    tm_type = models.CharField(max_length=255, blank=True, null=True)
    dna = models.CharField(max_length=255, blank=True, null=True)
    annotated = models.IntegerField(blank=True, null=True)
    pin_colour = models.CharField(max_length=255, blank=True, null=True)
    group = models.CharField(max_length=255, blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    lon = models.CharField(max_length=255, blank=True, null=True)
    lanes = models.CharField(max_length=255, blank=True, null=True)
    overview_req = models.CharField(max_length=255, blank=True, null=True)
    speed_limit = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sites'


class UserCategoryRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    role = models.ForeignKey(Roles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_category_role'


class UserHasRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    role = models.ForeignKey(Roles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_has_role'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(db_column='Username', unique=True, max_length=100)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=255)
    azure_ad_id = models.CharField(max_length=255, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    refresh_token = models.CharField(max_length=255, blank=True, null=True)
    access_token_expiry = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=64)
    salt = models.CharField(max_length=32)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    active = models.IntegerField()
    initials = models.CharField(max_length=4)
    system_created_dt = models.DateTimeField()
    system_created_by = models.IntegerField()
    system_updated_dt = models.DateTimeField(blank=True, null=True)
    system_updated_by = models.IntegerField(blank=True, null=True)
    user_team = models.IntegerField(blank=True, null=True)
    user_site = models.IntegerField(blank=True, null=True)
    user_position = models.IntegerField(blank=True, null=True)
    user_class = models.IntegerField(blank=True, null=True)
    login_valid_from = models.DateField()
    login_valid_to = models.DateField(blank=True, null=True)
    reporting_to = models.IntegerField(blank=True, null=True)
    pmd_access = models.IntegerField()
    eng_app_access = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class Workorder(models.Model):
    workorder_id = models.IntegerField(primary_key=True)
    quote_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    technician = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workorder'
