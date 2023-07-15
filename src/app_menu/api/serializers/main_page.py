from rest_framework import serializers

from app_menu.models import MainPageModel


class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageModel
        fields = (
            'id',
            'get_image_url'
        )
