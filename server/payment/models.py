from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    amount_payable = models.IntegerField()
    stripe_price_id = models.CharField(max_length=100, default=1)
    amount_paid = models.IntegerField(default=0)
