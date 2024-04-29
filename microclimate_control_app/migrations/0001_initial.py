# Generated by Django 4.2 on 2024-04-23 11:01

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                 help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                 max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True,
                 max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True,
                 max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False,
                 help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(
                    default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='date joined')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(help_text='Enter e-mail', max_length=254)),
                ('phone', models.CharField(help_text='Enter phone number', max_length=20,
                 validators=[django.core.validators.RegexValidator('^\\+?\\d{1,13}$')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                 related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_groups', models.ManyToManyField(
                    blank=True, related_name='user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                 related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BuildingObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45, unique=True)),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('data_collected', models.ManyToManyField(
                    to='microclimate_control_app.datatype')),
            ],
        ),
        migrations.AddField(
            model_name='datatype',
            name='metric',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to='microclimate_control_app.metric'),
        ),
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('value', models.FloatField()),
                ('building_object', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='microclimate_control_app.buildingobject')),
                ('data_type', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='microclimate_control_app.datatype')),
                ('device', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='microclimate_control_app.device')),
            ],
        ),
        migrations.AddField(
            model_name='buildingobject',
            name='project',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to='microclimate_control_app.project'),
        ),
        migrations.AddField(
            model_name='buildingobject',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
