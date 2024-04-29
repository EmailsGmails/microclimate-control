from rest_framework import serializers
from .models import Project, BuildingObject, DataPoint, User, DataType, Metric, Device


class BuildingObjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the BuildingObject model.

    This serializer serializes BuildingObject instances, converting them to JSON representations.

    Attributes:
        Meta: Metadata class specifying the model and fields for serialization.

    """

    class Meta:
        model = BuildingObject
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.

    This serializer serializes Project instances, converting them to JSON representations.

    Attributes:
        Meta: Metadata class specifying the model and fields for serialization.

    """

    class Meta:
        model = Project
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer serializes User instances, converting them to JSON representations.

    Attributes:
        Meta: Metadata class specifying the model and fields for serialization.

    """

    class Meta:
        model = User
        fields = ['id', 'full_name']


class DataTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for the DataType model.

    This serializer serializes DataType instances, converting them to JSON representations.

    Attributes:
        Meta: Metadata class specifying the model and fields for serialization.

    """

    class Meta:
        model = DataType
        fields = '__all__'


class MetricSerializer(serializers.ModelSerializer):
    """
    Serializer for the Metric model.

    This serializer serializes Metric instances, converting them to JSON representations.

    Attributes:
        Meta: Metadata class specifying the model and fields for serialization.

    """

    class Meta:
        model = Metric
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Device model.

    This serializer serializes Device instances, converting them to JSON representations.

    Attributes:
        Meta: Metadata class specifying the model and fields for serialization.

    """

    class Meta:
        model = Device
        fields = '__all__'


class DataPointSerializer(serializers.ModelSerializer):
    """
    Serializer for the DataPoint model.

    This serializer serializes DataPoint instances, converting them to JSON representations.

    Attributes:
        metric_name: Serializer method field to retrieve the name of the associated metric.
        data_type_name: Serializer method field to retrieve the name of the associated data type.

    """

    metric_name = serializers.SerializerMethodField(
        read_only=True, required=False)
    data_type_name = serializers.SerializerMethodField(required=False)

    class Meta:
        """
        Metadata class specifying the model and fields for serialization.

        Attributes:
            model: The model class to be serialized.
            fields: The fields to include in the serialized representation.
                   Here, 'id', 'data_type_name', 'data_type', 'metric_name', 'value', 'device', and 'building_object'
                   fields are included.

        """

        model = DataPoint
        fields = ['id', 'data_type_name', 'data_type', 'metric_name',
                  'value', 'metric_name', 'device', 'building_object']

    def get_data_type_name(self, obj):
        return obj.data_type.name

    def get_metric_name(self, obj):
        return obj.data_type.metric.name
