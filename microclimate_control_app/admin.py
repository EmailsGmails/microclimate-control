from django.contrib import admin
from .models import Project, BuildingObject, DataPoint, User, DataType, Metric, Device

admin.site.register(Project)
admin.site.register(BuildingObject)
admin.site.register(DataPoint)
admin.site.register(User)
admin.site.register(DataType)
admin.site.register(Metric)
admin.site.register(Device)
