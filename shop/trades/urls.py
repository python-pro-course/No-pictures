from django.contrib import admin
from django.urls import path

from trades.views import index, categories, by_category, basket1, basket

urlpatterns = [
    path('', index, name='index'),
    path('trades/', categories, name='categories'),
    path('categories/<int:category_id>/<int:page>', by_category, name='paginator'),
    path('basket/add/<int:product_id>', basket1, name='basket'),
    path('basket/', basket, name='add_product'),

]