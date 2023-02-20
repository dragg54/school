from django.conf import settings
from django.db import models

from student.models import Student

from supervisor.models import Supervisor

User = settings.AUTH_USER_MODEL


# Create your models here.
class SemesterChoice(models.TextChoices):
    rainy = "ra", ("rainy")
    harmattan = "ha", ("harmattan")


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    # supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=20)
    course_code = models.CharField(max_length=6)
    course_unit = models.IntegerField()
    level = models.CharField(max_length=3)
    department = models.CharField(max_length=30)
    semester = models.CharField(max_length=10, choices=SemesterChoice.choices)
    session = models.IntegerField()


class CourseChoice(models.TextChoices):
    pass
#     user = User.objects.all()
#     student = Student.objects.get(user=user)
#     courses = Course.objects.filter(student=user, level=student.level)
#     for i in range(len(courses)):
#         course = courses[i], courses[i]


class StudentCourse(models.Model):
    pass
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, choices=CourseChoice.choices,  on_delete=models.CASCADE)

#
class SupervisorCourse(models.Model):
    pass
#     student = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, choices=CourseChoice.choices,  on_delete=models.CASCADE)
