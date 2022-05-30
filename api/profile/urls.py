from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.profile.views import UserViewSet, RegionViewSet


router = DefaultRouter()
router.register('user', UserViewSet)
router.register('region', RegionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
    