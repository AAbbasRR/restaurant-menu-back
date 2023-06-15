from django.urls import path

from .views import *

app_name = 'app_menu'
urlpatterns = [
    # list categories
    path('category/list/', ListCategoriesView.as_view(), name='user_list_categories'),
    # list foods
    path('food/list/', ListFoodsView.as_view(), name='user_list_foods'),
]
