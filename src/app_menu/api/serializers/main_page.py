from rest_framework import serializers

from app_menu.models import MainPageModel


class MainPageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(
        'get_image_url',
        read_only=True
    )

    class Meta:
        model = MainPageModel
        fields = (
            'id',
            'image_url'
        )

    def __init__(self, *args, **kwargs):
        super(MainPageSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')

    def get_image_url(self, obj):
        return obj.get_image_url(self.request)
