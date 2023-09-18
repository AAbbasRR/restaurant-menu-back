from django.contrib import admin

from app_menu.models import (
    BirthdayModel,
    BirthdayImagesModel
)


class BirthdayImagesAdmin(admin.TabularInline):
    model = BirthdayImagesModel
    extra = 0
    min_num = 1
    max_num = 5


class BirthdayAdmin(admin.ModelAdmin):
    inlines = [BirthdayImagesAdmin, ]
    list_display = (
        'name',
        'location',
        'is_active',
        'price',
    )
    search_fields = (
        'name',
    )

    class Meta:
        model = BirthdayModel


admin.site.register(BirthdayModel, BirthdayAdmin)
