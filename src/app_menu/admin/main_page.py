from django.contrib import admin

from app_menu.models import MainPageModel


class MainPageAdmin(admin.ModelAdmin):
    list_display = (
        'picture',
    )

    def picture(self, obj):
        return obj.get_image_tag()

    picture.short_description = 'عکس شاخص'
    picture.allow_tags = True

    class Meta:
        model = MainPageModel


admin.site.register(MainPageModel, MainPageAdmin)
