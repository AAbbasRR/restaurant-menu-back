from rest_framework import generics

from app_menu.api.serializers.foods import ListFoodSerializer
from app_menu.models import (
    FoodModel
)

from utils.versioning import BaseVersioning
from utils.permissions import AllowAnyPermission


class ListFoodsView(generics.ListAPIView):
    permission_classes = [AllowAnyPermission]
    versioning_class = BaseVersioning
    serializer_class = ListFoodSerializer
    queryset = FoodModel.objects.filter(is_active=True).order_by('location')
