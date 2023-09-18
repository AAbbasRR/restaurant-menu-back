from rest_framework import generics

from app_menu.api.serializers.birthday import ListBirthdaySerializer
from app_menu.models import (
    BirthdayModel
)

from utils.versioning import BaseVersioning
from utils.permissions import AllowAnyPermission


class ListBirthdaysView(generics.ListAPIView):
    permission_classes = [AllowAnyPermission]
    versioning_class = BaseVersioning
    serializer_class = ListBirthdaySerializer
    queryset = BirthdayModel.objects.filter(is_active=True).order_by('location')
