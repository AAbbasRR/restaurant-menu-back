from rest_framework import serializers

from app_menu.models import (
    CategoryModel,
    FoodModel
)


class FoodSerializer(serializers.ModelSerializer):
    image_link = serializers.SerializerMethodField(
        'get_image_link',
    )

    class Meta:
        model = FoodModel
        fields = (
            'id',
            'name',
            'material',
            'price',

            'image_link',
        )

    def __init__(self, *args, **kwargs):
        super(FoodSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')

    def get_image_link(self, obj):
        return obj.get_image_url(self.request)


class ListCategoriesSerializer(serializers.ModelSerializer):
    category_foods = serializers.SerializerMethodField(
        'get_category_foods'
    )
    icon_link = serializers.SerializerMethodField(
        'get_icon_link'
    )

    class Meta:
        model = CategoryModel
        fields = (
            'id',
            'name',
            'description',

            'category_foods',
            'icon_link',
        )

    def __init__(self, *args, **kwargs):
        super(ListCategoriesSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')

    def get_category_foods(self, obj):
        return FoodSerializer(obj.category_foods.filter(is_active=True).order_by('location'), many=True, read_only=True, context=self.context).data

    def get_icon_link(self, obj):
        return obj.get_icon_url(self.request)
