# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import AgenceImmo

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    agence = models.ForeignKey(
        AgenceImmo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='utilisateurs'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email