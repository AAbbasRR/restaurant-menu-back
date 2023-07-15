from rest_framework import generics

from app_menu.api.serializers.settings import MenuInfoSerializer
from app_menu.models import SettingsModel

from utils.versioning import BaseVersioning
from utils.permissions import AllowAnyPermission


class MenuInfoView(generics.ListAPIView):
    permission_classes = [AllowAnyPermission]
    versioning_class = BaseVersioning
    serializer_class = MenuInfoSerializer
    queryset = SettingsModel.objects.all()
