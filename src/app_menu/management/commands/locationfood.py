from django.core.management.base import BaseCommand

from app_menu.models import (
    CategoryModel,
    FoodModel
)


class Command(BaseCommand):
    help = 'Initiate Food locations'

    def handle(self, *args, **options):
        categories = CategoryModel.objects.all()
        for category in categories:
            foods = FoodModel.objects.filter(category=category).order_by("location")
            for index, food in enumerate(foods):
                if food.location != index + 1:
                    food.location = index + 1
                    food.save()
