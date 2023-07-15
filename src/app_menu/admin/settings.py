from django.contrib import admin

from app_menu.models import SettingsModel


class SettingsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'value',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    class Meta:
        model = SettingsModel


admin.site.register(SettingsModel, SettingsAdmin)
