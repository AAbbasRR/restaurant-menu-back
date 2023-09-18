from django.contrib import admin

from app_menu.models import FoodModel


class FoodsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'location',
        'material',
        'is_active',
        'price',
    )
    search_fields = (
        'name',
        'material',
    )

    class Meta:
        model = FoodModel


admin.site.register(FoodModel, FoodsAdmin)
