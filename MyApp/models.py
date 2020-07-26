# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Userstable(models.Model):
    firstname = models.CharField(db_column='firstName', max_length=15)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=15)  # Field name made lowercase.
    phone = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=9)
    housenumber = models.SmallIntegerField(db_column='houseNumber')  # Field name made lowercase.
    email = models.CharField(max_length=256, blank=True, null=True)
    location = models.TextField(blank=True, null=True)  # This field type is a guess.
    photo = models.BinaryField(blank=True, null=True)
    apartmentnumber = models.SmallIntegerField(db_column='apartmentNumber', blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'usersTable'


class Businesscategorytable(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    icon = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'businessCategoryTable'


class Businessestable(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    phone = models.IntegerField()
    category = models.ForeignKey(Businesscategorytable, models.DO_NOTHING, db_column='category')
    details = models.TextField(blank=True, null=True) # i change it to text
    address = models.TextField()  # This field type is a guess.
    photo = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'businessesTable'


class Itemtable(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    type = models.CharField(max_length=6)
    price = models.TextField(blank=True, null=True)  # This field type is a guess.
    publishdate = models.DateField(db_column='publishDate')  # Field name made lowercase.
    publisher = models.ForeignKey('Userstable', models.DO_NOTHING, db_column='publisher')

    class Meta:
        managed = False
        db_table = 'itemTable'


class Interestitemtable(models.Model):
    interest_item_table_id = models.AutoField(primary_key=True) # extra field to force the composite pk 
    # id = models.OneToOneField('Itemtable', models.DO_NOTHING, db_column='id', primary_key=True) dellete it 
    item_id = models.ForeignKey('Itemtable', models.DO_NOTHING, db_column='id') # i changed the name 
    interestuser = models.ForeignKey('Userstable', models.DO_NOTHING, db_column='interestUser')  # Field name made lowercase.
    state = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'interestItemTable'
        unique_together = (('item_id', 'interestuser'),)




class Managertable(models.Model):
    phone = models.OneToOneField('Userstable', models.DO_NOTHING, db_column='phone', primary_key=True)

    class Meta:
        managed = False
        db_table = 'managerTable'


class Messagestable(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    cont = models.CharField(max_length=4000) # i changed it to charfield
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    publisher = models.ForeignKey(Managertable, models.DO_NOTHING, db_column='publisher')

    class Meta:
        managed = False
        db_table = 'messagesTable'



class Typeoftreatmenttable(models.Model):
    type = models.CharField(primary_key=True, max_length=20)
    manager = models.ForeignKey(Managertable, models.DO_NOTHING, db_column='manager')

    class Meta:
        managed = False
        db_table = 'typeOfTreatmentTable'



class Requesttable(models.Model):
    typeoftreatment = models.ForeignKey('Typeoftreatmenttable', models.DO_NOTHING, db_column='typeOfTreatment')  # Field name made lowercase.
    publisher = models.ForeignKey('Userstable', models.DO_NOTHING, db_column='publisher')
    id = models.SmallIntegerField(primary_key=True)
    state = models.BooleanField(blank=True, null=True)
    cont = models.CharField(max_length=4000) # i changed it to charfield  
    publishdate = models.DateField(db_column='publishDate', blank=True, null=True)  # Field name made lowercase.
    publishtime = models.TimeField(db_column='publishTime', blank=True, null=True)  # Field name made lowercase.
    finishdate = models.DateField(db_column='finishDate', blank=True, null=True)  # Field name made lowercase.
    finishtime = models.TimeField(db_column='finishTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'requestTable'


class Ridetable(models.Model):
    ride_table_id = models.AutoField(primary_key=True) # extra field to force the composite pk 
    # passenger = models.OneToOneField('Userstable', models.DO_NOTHING, db_column='passenger', primary_key=True) dellete it 
    passenger = models.ForeignKey('Userstable',  models.DO_NOTHING, related_name='passengers', db_column='passenger')
    optionaldriver = models.ForeignKey('Userstable', models.DO_NOTHING, related_name='driver', db_column='optionalDriver')  # Field name made lowercase.
    radius = models.SmallIntegerField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'rideTable'
        unique_together = (('passenger', 'optionaldriver'),)


