from django.db import models

# Create your models here.
class Gender(models.TextChoices):
    MALE = "m", ("male")
    FEMALE = "f", ("female")

class StudentProfile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    matric_number = models.CharField(max_length=20)
    sex = models.CharField(choices=Gender.choices, max_length=1)
    age = models.IntegerField()
    image = models.ImageField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    next_of_kin_first_name = models.CharField(max_length=20)
    next_of_kin_last_name = models.CharField(max_length=20)
    next_of_kin_phone = models.CharField(max_length=20)
    year_admitted = models.DateField()
    department = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'