from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Role
from student.models import Student
from supervisor.models import Supervisor


@receiver(post_save, sender=Student)
def create_role(sender, instance, created, **kwargs):
    if created:
        Role.objects.create(
            user=instance.user_id,
            role='student'
        )


@receiver(post_save, sender=Student)
def save_role(sender, instance, **kwargs):
    print(instance.first_name)


@receiver(post_save, sender=Supervisor)
def create_role(sender, instance, created, **kwargs):
    if created:
        Role.objects.create(
            user=instance.user,
            role='supervisor'
        )


@receiver(post_save, sender=Supervisor)
def save_role(sender, instance, **kwargs):
    print(instance.first_name)
