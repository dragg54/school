from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Student

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(
            user_id=instance,
            first_name=instance.first_name,
            last_name=instance.last_name
        )
