from rest_framework import generics

from app_menu.api.serializers.categories import ListCategoriesSerializer
from app_menu.models import (
    CategoryModel
)

from utils.versioning import BaseVersioning
from utils.permissions import AllowAnyPermission


class ListCategoriesView(generics.ListAPIView):
    permission_classes = [AllowAnyPermission]
    versioning_class = BaseVersioning
    serializer_class = ListCategoriesSerializer
    queryset = CategoryModel.objects.filter(is_active=True).order_by('location')
