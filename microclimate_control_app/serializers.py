from rest_framework import serializers
from .models import Project, BuildingObject, DataPoint, User, DataType, Metric, Device

class BuildingObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingObject
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    BuildingObjectSerializer
    class Meta:
        model = Project
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name']

class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = '__all__'

class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DataPointSerializer(serializers.ModelSerializer):
    metric_name = serializers.SerializerMethodField(read_only=True, required=False)
    data_type_name = serializers.SerializerMethodField(required=False)

    class Meta:
        model = DataPoint
        fields = ['id', 'data_type_name', 'data_type', 'metric_name', 'value', 'metric_name', 'device', 'building_object']

    def get_data_type_name(self, obj):
        return obj.data_type.name

    def get_metric_name(self, obj):
        return obj.data_type.metric.name
