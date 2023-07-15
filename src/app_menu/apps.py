from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppMenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_menu'
    verbose_name = _('App Menu')
    verbose_name_plural = _('App Menus')
