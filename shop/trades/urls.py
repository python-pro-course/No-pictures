from django.contrib import admin
from django.urls import path

from trades.views import index, categories, by_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('trades/', categories, name='categories'),
    path('categories/<int:category_id>/<int:page>', by_category, name='paginator'),

]