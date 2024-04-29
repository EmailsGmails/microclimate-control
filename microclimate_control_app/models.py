from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

import pdb


class Project(models.Model):
    """
    Model representing a project.

    This model stores information about a project, including its name and description.

    Attributes:
        name (str): The name of the project.
        description (str): The description of the project.

    Methods:
        __str__: Returns a string representation of the project object.

    """

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
    Model representing a user.

    This model extends the built-in Django User model with additional fields such as full name,
    email, phone number, and user groups.

    Attributes:
        full_name (str): The full name of the user.
        email (str): The email address of the user.
        phone (str): The phone number of the user.
        user_groups (ManyToManyField): The groups associated with the user.

    Methods:
        __str__: Returns a string representation of the user.

    """

    full_name = models.CharField(max_length=100)
    email = models.EmailField(help_text="Enter e-mail")
    phone = models.CharField(max_length=20, help_text="Enter phone number", validators=[
                             RegexValidator(r'^\+?\d{1,13}$')])
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
    """
    Model representing a building object.

    This model stores information about a building object, including its name, location,
    associated project, and users.

    Attributes:
        name (str): The name of the building object.
        location (str): The location of the building object.
        project (Project): The project associated with the building object.
        users (ManyToManyField): The users associated with the building object.

    Methods:
        __str__: Returns a string representation of the building object.

    """

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Metric(models.Model):
    """
    Model representing a metric.

    This model stores information about a metric, including its name.

    Attributes:
        name (str): The name of the metric.

    Methods:
        __str__: Returns a string representation of the metric.

    """

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class DataType(models.Model):
    """
    Model representing a data type.

    This model stores information about a data type, including its code, name, and associated metric.

    Attributes:
        code (str): The code of the data type.
        name (str): The name of the data type.
        metric (Metric): The metric associated with the data type.

    Methods:
        save: Overrides the save method to uppercase the code before saving.
        __str__: Returns a string representation of the data type.

    """

    code = models.CharField(max_length=45, unique=True)
    name = models.CharField(max_length=45)
    metric = models.ForeignKey(Metric, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Device(models.Model):
    """
    Model representing a device.

    This model stores information about a device, including its name and the types of data it collects.

    Attributes:
        name (str): The name of the device.
        data_collected (ManyToManyField): The types of data collected by the device.

    Methods:
        __str__: Returns a string representation of the device.

    """

    name = models.CharField(max_length=45)
    data_collected = models.ManyToManyField(DataType)

    def __str__(self):
        return self.name


class DataPoint(models.Model):
    """
    Model representing a data point.

    This model stores information about a data point, including its timestamp, value, associated data type,
    device, and building object.

    Attributes:
        timestamp (DateTimeField): The timestamp of the data point.
        value (float): The value of the data point.
        data_type (DataType): The data type associated with the data point.
        device (Device): The device associated with the data point.
        building_object (BuildingObject): The building object associated with the data point.

    Methods:
        __str__: Returns a string representation of the data point.

    """

    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    data_type = models.ForeignKey(DataType, on_delete=models.PROTECT)
    device = models.ForeignKey(Device, on_delete=models.PROTECT)
    building_object = models.ForeignKey(
        BuildingObject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.data_type}: {self.value} {self.data_type.metric}"
