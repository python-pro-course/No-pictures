
import django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from users.views import auth_user, register
from django.urls import path

urlpatterns = [
    path('authorization/', auth_user, name='auth'),
    path('registration/', register, name='register'),
]