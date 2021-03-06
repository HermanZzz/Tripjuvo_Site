# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-06 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('minor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('poi_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'beacon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoBeacon',
            fields=[
                ('minor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('poi_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'info_beacon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=100)),
                ('marker', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'info_categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoGcmTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_id', models.TextField()),
            ],
            options={
                'db_table': 'info_gcm_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoPois',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('intro', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=120)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=60)),
                ('longtitude', models.DecimalField(decimal_places=8, max_digits=60)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=15, null=True)),
                ('favorite', models.SmallIntegerField()),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'info_pois',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('poi_id', models.IntegerField()),
            ],
            options={
                'db_table': 'info_preference',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoRegion',
            fields=[
                ('city', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=60)),
                ('longtitude', models.DecimalField(decimal_places=8, max_digits=60)),
                ('picture', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'info_region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoSqliteSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('seq', models.TextField()),
            ],
            options={
                'db_table': 'info_sqlite_sequence',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InfoUserT',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('ps', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=4)),
                ('gender', models.CharField(max_length=1)),
                ('p_vehicle', models.CharField(max_length=10)),
                ('e_mail', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'info_user_t',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=100)),
                ('marker', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='GcmTable',
            fields=[
                ('reg_id', models.TextField()),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'gcm_table',
            },
        ),
        migrations.CreateModel(
            name='Pois',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('intro', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=150)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=60)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=60)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=15, null=True)),
                ('favorite', models.SmallIntegerField()),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'pois',
            },
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('poi_id', models.IntegerField()),
            ],
            options={
                'db_table': 'preference',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('city', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=60)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=60)),
                ('picture', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='SqliteSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('seq', models.TextField()),
            ],
            options={
                'db_table': 'sqlite_sequence',
            },
        ),
        migrations.CreateModel(
            name='UserT',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('ps', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=4)),
                ('gender', models.CharField(max_length=1)),
                ('p_vehicle', models.CharField(blank=True, max_length=10, null=True)),
                ('e_mail', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'user_t',
            },
        ),
    ]
