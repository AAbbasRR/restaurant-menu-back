from rest_framework import serializers

from app_menu.models import SettingsModel


class MenuInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsModel
        fields = (
            'id',
            'title',
            'value',
            'get_image_url'
        )
