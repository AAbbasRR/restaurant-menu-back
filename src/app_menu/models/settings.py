from django.db import models
from django.utils.translation import gettext as _

from utils.data_list import site_settings


class SettingsManager(models.Manager):
    def create_update(self, title, value):
        obj = self.filter(title=title).first()
        if obj is None:
            obj = self.create(
                title=title,
                value=value
            )
        else:
            obj.value = value
            obj.save()
        return obj


class Settings(models.Model):
    class Meta:
        verbose_name = _('Setting')
        verbose_name_plural = _('Settings')

    title = models.CharField(
        max_length=10,
        choices=site_settings,
        verbose_name=_('Title')
    )
    value = models.CharField(
        max_length=100,
        verbose_name=_('Value')
    )

    objects = SettingsManager()
