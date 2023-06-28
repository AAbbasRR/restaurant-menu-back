from django.db import models
from django.utils.translation import gettext as _

from config.settings import DEBUG


def category_icon_directory_path(instance, filename):
    return 'category_images/{0}'.format(filename)


class Category(models.Model):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    name = models.CharField(
        max_length=100,
        verbose_name=_('Name')
    )
    icon = models.ImageField(
        upload_to=category_icon_directory_path,
        verbose_name=_('Icon')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is Active')
    )
    location = models.PositiveIntegerField(
        default=1,
        verbose_name=_('Location')
    )

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        try:
            old_obj = Category.objects.get(id=self.id)
            if old_obj.image != self.icon:
                old_obj.image.delete()
        except:
            pass
        return super(Category, self).save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        self.icon.delete()
        super(Category, self).delete(using, keep_parents)

    def get_icon_url(self, request):
        if self.icon is None or self.icon == "":
            return None
        else:
            host = request.get_host()
            protocol = request.build_absolute_uri().split(host)[0]
            protocol = protocol if DEBUG else protocol.replace("http", "https") if protocol.split(":")[0] == "http" else protocol
            website_url = protocol + host
            return website_url + self.icon.url
