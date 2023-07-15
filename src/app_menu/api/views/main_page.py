from rest_framework import generics

from app_menu.api.serializers.main_page import MainPageSerializer
from app_menu.models import MainPageModel

from utils.versioning import BaseVersioning
from utils.permissions import AllowAnyPermission


class MainPageView(generics.ListAPIView):
    permission_classes = [AllowAnyPermission, ]
    versioning_class = BaseVersioning
    serializer_class = MainPageSerializer
    queryset = MainPageModel.objects.all()
