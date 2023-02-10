from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Role
from student.models import StudentProfile


@receiver(post_save, sender=StudentProfile)
def create_role(sender, instance, created, **kwargs):
    if created:
        Role.objects.create(
            user=instance.user,
            role='student'
        )


@receiver(post_save, sender=StudentProfile)
def save_role(sender, instance, **kwargs):
    print(instance.first_name)
