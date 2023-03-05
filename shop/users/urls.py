
import django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from users.views import *
from django.urls import path

urlpatterns = [
    path('authorization/', UserLoginView.as_view(), name='authen'),
    path('registration/', UserRegistrationView.as_view(), name='register'),
    path('profille/<int:pk>', UserProfileView.as_view(), name='profille'),
    path('logout/', LogoutView.as_view(), name='logout'),
]