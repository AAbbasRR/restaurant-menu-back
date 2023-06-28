from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator

from config.settings import DEBUG

from app_menu.models import CategoryModel


def food_image_directory_path(instance, filename):
    return 'food_images/{0}'.format(filename)


class Food(models.Model):
    class Meta:
        verbose_name = _('Food')
        verbose_name_plural = _('Foods')

    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.SET_NULL,
        related_name='category_foods',
        null=True,
        verbose_name=_('Category')
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_('Name')
    )
    material = models.TextField(
        verbose_name=_('Material')
    )
    image = models.ImageField(
        upload_to=food_image_directory_path,
        verbose_name=_('Image')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is Active')
    )
    price = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name=_('Price')
    )
    location = models.PositiveIntegerField(
        default=1,
        verbose_name=_('Location')
    )

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        try:
            old_obj = Food.objects.get(id=self.id)
            if old_obj.image != self.image:
                old_obj.image.delete()
        except:
            pass
        return super(Food, self).save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super(Food, self).delete(using, keep_parents)

    def get_image_url(self, request):
        if self.image is None or self.image == "":
            return None
        else:
            host = request.get_host()
            protocol = request.build_absolute_uri().split(host)[0]
            protocol = protocol if DEBUG else protocol.replace("http", "https") if protocol.split(":")[0] == "http" else protocol
            website_url = protocol + host
            return website_url + self.image.url

