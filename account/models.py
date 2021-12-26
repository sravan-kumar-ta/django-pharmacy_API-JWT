from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "Customer"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class ShopAdmin(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
