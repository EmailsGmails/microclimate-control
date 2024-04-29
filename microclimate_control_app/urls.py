from django.urls import path, include
from rest_framework_nested import routers

from .views import ProjectViewSet, BuildingObjectViewSet, DataPointViewSet, UserViewSet

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

projects_router = routers.NestedSimpleRouter(
    router, r'projects', lookup='project')
projects_router.register(
    r'objects', BuildingObjectViewSet, basename='building-objects')

objects_router = routers.NestedSimpleRouter(
    projects_router, r'objects', lookup='object')
objects_router.register(r'data-points', DataPointViewSet,
                        basename='object-data-points')
objects_router.register(r'responsibles', UserViewSet,
                        basename='object-responsibles')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('', include(objects_router.urls)),
]
