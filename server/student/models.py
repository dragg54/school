from datetime import date
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Gender(models.TextChoices):
    MALE = "m", ("male")
    FEMALE = "f", ("female")


class Student(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    matric_number = models.CharField(max_length=20, null=True)
    sex = models.CharField(choices=Gender.choices, max_length=1, null=True)
    age = models.IntegerField(null=True)
    image = models.ImageField(upload_to="media", null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    level = models.IntegerField(null=True)
    next_of_kin_first_name = models.CharField(max_length=20, null=True)
    next_of_kin_last_name = models.CharField(max_length=20, null=True)
    next_of_kin_phone = models.CharField(max_length=20, null=True)
    department = models.CharField(max_length=20, null=True)
    date_admitted = models.DateField(null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
