from django.contrib.auth.models import User
from django.db import models


# Create your models here

class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=20)
