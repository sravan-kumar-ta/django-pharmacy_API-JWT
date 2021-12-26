from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    user_type_data = ((2, "Admin"), (3, "Customer"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    joined_at = models.DateTimeField(auto_now_add=True, null=True)