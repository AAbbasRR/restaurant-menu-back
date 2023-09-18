from rest_framework import serializers

from app_menu.models import (
    BirthdayModel,
    BirthdayImagesModel
)


class BirthdayImagesSerializer(serializers.ModelSerializer):
    image_link = serializers.SerializerMethodField(
        'get_image_link',
    )

    class Meta:
        model = BirthdayImagesModel
        fields = (
            'id',
            'image_link',
        )

    def __init__(self, *args, **kwargs):
        super(BirthdayImagesSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')

    def get_image_link(self, obj):
        return obj.get_image_url(self.request)


class ListBirthdaySerializer(serializers.ModelSerializer):
    birthday_images = serializers.SerializerMethodField(
        'get_birthday_images'
    )

    class Meta:
        model = BirthdayModel
        fields = (
            'id',
            'name',
            'is_active',
            'price',
            'description',
            'location',

            'birthday_images',
        )

    def get_birthday_images(self, obj):
        return BirthdayImagesSerializer(obj.birthday_images.all(), many=True, read_only=True, context=self.context).data
