from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    preferred_language = models.CharField(max_length=30, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="uploads/users/", blank=True, null=True)
