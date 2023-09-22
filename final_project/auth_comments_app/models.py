from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=100)
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
    )

