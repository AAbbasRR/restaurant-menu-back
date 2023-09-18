from django.contrib import admin

from app_menu.models import CategoryModel


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'is_active',
    )
    search_fields = (
        'name',
    )

    class Meta:
        model = CategoryModel


admin.site.register(CategoryModel, CategoryAdmin)
