from django.db import models
from django.contrib.auth.models import User
from apps.common.models import CoreModel

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(CoreModel):
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name="profile"
    )
    bio = models.TextField(blank=True, null=True, max_length=500)
    birth_date = models.DateField(blank=True, null=True, max_length=50)
    location = models.CharField(blank=True, null=True, max_length=100)

    # Social Accounts
    # Link Model


    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.user.username}'s Profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return
    Profile.objects.create(user=instance)
    instance.profile.save()