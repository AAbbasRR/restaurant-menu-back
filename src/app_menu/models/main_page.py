from django.db import models
from django.utils.translation import gettext as _
from django.utils.html import mark_safe

from config.settings import DEBUG


def main_page_image_directory_path(instance, filename):
    return 'main_images/{0}'.format(filename)


class MainPage(models.Model):
    class Meta:
        verbose_name = _('Main Page')
        verbose_name_plural = _('Main Page')

    image = models.ImageField(
        upload_to=main_page_image_directory_path,
        verbose_name=_('Image')
    )

    def __str__(self):
        return self.image.url

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     try:
    #         old_obj = MainPage.objects.get(id=self.id)
    #         if old_obj.image != self.image:
    #             old_obj.image.delete()
    #     except:
    #         pass
    #     return super(MainPage, self).save(force_insert, force_update, using, update_fields)

    # def delete(self, using=None, keep_parents=False):
    #     self.image.delete()
    #     super(MainPage, self).delete(using, keep_parents)

    def get_image_tag(self):
        return mark_safe('<img src="/media/%s"  width="150" />' % self.image)

    def get_image_url(self, request):
        if self.image is None or self.image == "":
            return None
        else:
            host = request.get_host()
            protocol = request.build_absolute_uri().split(host)[0]
            protocol = protocol if DEBUG else protocol.replace("http", "https") if protocol.split(":")[0] == "http" else protocol
            website_url = protocol + host
            return website_url + self.image.url
