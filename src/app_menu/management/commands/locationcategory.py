from django.core.management.base import BaseCommand

from app_menu.models import CategoryModel


class Command(BaseCommand):
    help = 'Initiate Category locations'

    def handle(self, *args, **options):
        categories = CategoryModel.objects.all().order_by("location")
        for index, category in enumerate(categories):
            if category.location != index + 1:
                category.location = index + 1
                category.save()
