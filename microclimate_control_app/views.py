from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from os import environ

from .models import Project, BuildingObject
from .serializers import ProjectSerializer, BuildingObjectSerializer, DataPointSerializer, UserSerializer
from .permissions import (
    CanAccessProject,
    CanUpdateProject,
    CanAccessBuildingObject,
    CanCreateBuildingObject,
    CanUpdateBuildingObject,
    CanDeleteBuildingObject,
    CanAccessBuildingContent,
)

APP_NAME = 'microclimate_control_app'
DEFAULT_CACHE_TIMEOUT = environ.get('DEFAULT_CACHE_TIMEOUT')

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]
    permission_classes_by_action = {
        'create': [IsAdminUser],
        'destroy': [IsAdminUser],
        'update': [IsAdminUser | CanUpdateProject],
        'partial_update': [IsAdminUser | CanUpdateProject],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Project.objects.all()

        project_ids = [
            int(perm.codename.split('_')[-1])
            for perm in user.user_permissions.all()
            if perm.codename.startswith('can_access_project_') and user.has_perm(f'{APP_NAME}.{perm.codename}')
        ]
        return Project.objects.filter(id__in=project_ids)

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class BuildingObjectViewSet(viewsets.ModelViewSet):
    serializer_class = BuildingObjectSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]
    permission_classes_by_action = {
        'retrieve': [IsAdminUser | CanAccessBuildingObject | CanAccessProject],
        'create': [IsAdminUser | CanCreateBuildingObject],
        'update': [IsAdminUser | CanUpdateBuildingObject],
        'partial_update': [IsAdminUser | CanUpdateBuildingObject],
        'destroy': [IsAdminUser | CanDeleteBuildingObject],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        project_id = self.kwargs['project_pk']
        if user.is_staff or user.has_perm(f'{APP_NAME}.can_access_project_{project_id}'):
            return Project.objects.get(id=project_id).buildingobject_set.all()

        building_ids = [
            int(perm.codename.split('_')[-1])
            for perm in user.user_permissions.all()
            if perm.codename.startswith(f'can_access_project_{project_id}_building_') \
               and user.has_perm(f'{APP_NAME}.{perm.codename}')
        ]
        return BuildingObject.objects.filter(id__in=building_ids)

    @method_decorator(cache_page(DEFAULT_CACHE_TIMEOUT))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(DEFAULT_CACHE_TIMEOUT))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class DataPointViewSet(viewsets.ModelViewSet):
    serializer_class = DataPointSerializer
    permission_classes = [IsAdminUser | CanAccessBuildingContent]

    def get_queryset(self):
        building_id = self.kwargs['object_pk']
        return BuildingObject.objects.get(id=building_id).datapoint_set

    def create(self, request, *args, **kwargs):
        request.data['building_object'] = kwargs.get('object_pk')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    permission_classes_by_action = {
        'list': [IsAdminUser | CanAccessBuildingContent],
        'retrieve': [IsAdminUser | CanAccessBuildingContent],
    }

    def get_queryset(self):
        building_id = self.kwargs['object_pk']
        return BuildingObject.objects.get(id=building_id).users

    @method_decorator(cache_page(DEFAULT_CACHE_TIMEOUT))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(DEFAULT_CACHE_TIMEOUT))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)