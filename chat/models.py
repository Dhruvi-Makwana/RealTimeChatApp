from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    mobile_number = models.CharField(max_length=10)
    profile = models.ImageField(
        upload_to="user_profile/",
        height_field=None,
        width_field=None,
        max_length=100,
        blank=True,
        null=True
    )
