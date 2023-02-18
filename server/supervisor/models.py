from django.contrib.auth.models import User
from django.db import models

from server.student.models import Gender


# Create your models here.
class Supervisor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=Gender.choices)
    department = models.CharField(max_length=30)
    date_employed = models.DateField()
