from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['email', 'full_name', 'is_staff']

    def __str__(self):
        return f'{self.username}'
