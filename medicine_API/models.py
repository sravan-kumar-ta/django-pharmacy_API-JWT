from django.db import models

from medicines.models import Medicine
from account.models import CustomUser


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
