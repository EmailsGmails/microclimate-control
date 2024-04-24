from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

import pdb

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(help_text="Enter e-mail")
    phone = models.CharField(max_length=20, help_text="Enter phone number", validators=[RegexValidator(r'^\+?\d{1,13}$')])
    user_groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_groups',
        blank=True,
    )

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'auth_user'

class BuildingObject(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Metric(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class DataType(models.Model):
    code = models.CharField(max_length=45, unique=True)
    name = models.CharField(max_length=45)
    metric = models.ForeignKey(Metric, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=45)
    data_collected = models.ManyToManyField(DataType)

    def __str__(self):
        return self.name

class DataPoint(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    data_type = models.ForeignKey(DataType, on_delete=models.PROTECT)
    device = models.ForeignKey(Device, on_delete=models.PROTECT)
    building_object = models.ForeignKey(BuildingObject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.data_type}: {self.value} {self.data_type.metric}"
