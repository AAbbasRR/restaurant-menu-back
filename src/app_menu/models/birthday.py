from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator

from config.settings import DEBUG


class Birthday(models.Model):
    class Meta:
        verbose_name = _('Birthday')
        verbose_name_plural = _('Birthdays')

    name = models.CharField(
        max_length=100,
        verbose_name=_('Name')
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
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description')
    )
    location = models.PositiveIntegerField(
        default=1,
        verbose_name=_('Location')
    )

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is not None:
            onother_location = Birthday.objects.filter(location=self.location).first()
            if onother_location is not None:
                old_obj = Birthday.objects.filter(pk=self.pk).first()
                new_obj = super().save(force_insert, force_update, using, update_fields)
                onother_location.location = old_obj.location
                onother_location.save()
                return new_obj
        else:
            onother_location = Birthday.objects.filter(location=self.location).first()
            if onother_location is not None:
                last_obj = Birthday.objects.filter(category=self.category).order_by("location").last()
                self.location = last_obj.location + 1
        return super().save(force_insert, force_update, using, update_fields)


def birthday_images_directory_path(instance, filename):
    return 'birthday_images/{0}'.format(filename)
        

class BirthdayImages(models.Model):
    class Meta:
        verbose_name = _('Birthday Image')
        verbose_name_plural = _('Birthday Images')

    birthday = models.ForeignKey(
        Birthday,
        on_delete=models.CASCADE,
        related_name="birthday_images",
        verbose_name=_('Birthday')
    )
    image = models.FileField(
        upload_to=birthday_images_directory_path,
        null=True,
        blank=True,
        verbose_name=_('Image')
    )


    def __str__(self):
        return self.image.url

    def get_image_url(self, request):
        try:
            if self.image is None or self.image == "":
                return None
            else:
                host = request.get_host()
                protocol = request.build_absolute_uri().split(host)[0]
                protocol = protocol if DEBUG else protocol.replace("http", "https") if protocol.split(":")[0] == "http" else protocol
                website_url = protocol + host
                return website_url + self.image.url
        except:
            return None

