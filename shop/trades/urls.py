from django.contrib import admin
from django.urls import path

from trades.views import index, categories, by_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trades/', index, name='index'),
    path('categories/', categories, name='categories'),
    path('categories/<int:category_id>/<int:page>', by_category, name='by_category'),

]