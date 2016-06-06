# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class Beacon(models.Model):
    minor_id = models.IntegerField(primary_key=True)
    poi_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beacon'

class InfoBeacon(models.Model):
    minor_id = models.IntegerField(primary_key=True)
    poi_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_beacon'


class InfoCategories(models.Model):
    name = models.CharField(max_length=10)
    image = models.CharField(max_length=100)
    marker = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'info_categories'


class InfoGcmTable(models.Model):
    reg_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'info_gcm_table'


class InfoPois(models.Model):
    category_id = models.BigIntegerField()
    name = models.CharField(max_length=100)
    intro = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=200)
    link = models.CharField(max_length=120)
    latitude = models.DecimalField(max_digits=60, decimal_places=8)
    longtitude = models.DecimalField(max_digits=60, decimal_places=8)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=15, blank=True, null=True)
    favorite = models.SmallIntegerField()
    city = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_pois'


class InfoPreference(models.Model):
    user_id = models.CharField(max_length=15)
    age = models.IntegerField()
    poi_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'info_preference'


class InfoRegion(models.Model):
    city = models.CharField(primary_key=True, max_length=15)
    latitude = models.DecimalField(max_digits=60, decimal_places=8)
    longtitude = models.DecimalField(max_digits=60, decimal_places=8)
    picture = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_region'


class InfoSqliteSequence(models.Model):
    name = models.TextField()
    seq = models.TextField()

    class Meta:
        managed = False
        db_table = 'info_sqlite_sequence'


class InfoUserT(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    ps = models.CharField(max_length=10)
    age = models.CharField(max_length=4)
    gender = models.CharField(max_length=1)
    p_vehicle = models.CharField(max_length=10)
    e_mail = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'info_user_t'


## Models corresponding to DB ##

class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    image = models.CharField(max_length=100)
    marker = models.CharField(max_length=100)

    class Meta:
        #managed = False
        db_table = 'categories'

class GcmTable(models.Model):
    reg_id = models.TextField()
    id = models.IntegerField(primary_key=True, unique=True)

    class Meta:
        #managed = False
        db_table = 'gcm_table'

class Pois(models.Model):
    id = models.IntegerField(primary_key=True)
    category_id = models.BigIntegerField()
    name = models.CharField(max_length=100)
    intro = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=200)
    link = models.CharField(max_length=150)
    latitude = models.DecimalField(max_digits=60, decimal_places=8)
    longitude = models.DecimalField(max_digits=60, decimal_places=8)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=15, blank=True, null=True)
    favorite = models.SmallIntegerField()
    city = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'pois'


class Preference(models.Model):
    user_id = models.CharField(max_length=15)
    age = models.IntegerField()
    poi_id = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'preference'


class Region(models.Model):
    city = models.CharField(primary_key=True, max_length=15)
    latitude = models.DecimalField(max_digits=60, decimal_places=8)
    longitude = models.DecimalField(max_digits=60, decimal_places=8)
    picture = models.TextField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'region'


class SqliteSequence(models.Model):
    name = models.TextField()
    seq = models.TextField()

    class Meta:
        # managed = False
        db_table = 'sqlite_sequence'


class UserT(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    ps = models.CharField(max_length=10)
    age = models.CharField(max_length=4)
    gender = models.CharField(max_length=1)
    p_vehicle = models.CharField(max_length=10, blank=True, null=True)
    e_mail = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'user_t'
