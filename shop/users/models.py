from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usery(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

















