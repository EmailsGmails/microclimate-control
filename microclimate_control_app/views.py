from rest_framework import viewsets
from .models import Project, BuildingObject, DataPoint, User
from .serializers import ProjectSerializer, BuildingObjectSerializer, DataPointSerializer, UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class BuildingObjectViewSet(viewsets.ModelViewSet):
    queryset = BuildingObject.objects.all()
    serializer_class = BuildingObjectSerializer

class DataPointViewSet(viewsets.ModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
