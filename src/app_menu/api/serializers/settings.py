from rest_framework import serializers

from app_menu.models import SettingsModel


class MenuInfoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(
        'get_image'
    )
    
    class Meta:
        model = SettingsModel
        fields = (
            'id',
            'title',
            'value',
            'image'
        )

    def __init__(self, *args, **kwargs):
        super(MenuInfoSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')

    def get_image(self, obj):
        return obj.get_image_url(self.request)
