from pprint import pprint
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.response import Response

from apps.profile.models import User, Region
from api.profile.serializers import UserSerializer, RegionSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
