from django.urls import path, include
from rest_framework.routers import DefaultRouter
from microclimate_control_app.views import ProjectViewSet, BuildingObjectViewSet, DataPointViewSet, UserViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'objects', BuildingObjectViewSet)
router.register(r'data-points', DataPointViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
