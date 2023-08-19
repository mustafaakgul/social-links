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
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    instagram = models.URLField(blank=True)
    tiktok = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    # github = models.URLField(blank=True)
    # youtube = models.URLField(blank=True)
    # medium = models.URLField(blank=True)
    # reddit = models.URLField(blank=True)
    # stackoverflow = models.URLField(blank=True)
    # discord = models.URLField(blank=True)
    # twitch = models.URLField(blank=True)
    # steam = models.URLField(blank=True)
    # spotify = models.URLField(blank=True)
    # pinterest = models.URLField(blank=True)
    # snapchat = models.URLField(blank=True)
    # tumblr = models.URLField(blank=True)
    # vimeo = models.URLField(blank=True)
    # whatsapp = models.URLField(blank=True)
    # telegram = models.URLField(blank=True)
    # skype = models.URLField(blank=True)
    # quora = models.URLField(blank=True)
    # soundcloud = models.URLField(blank=True)
    # github_gist = models.URLField(blank=True)
    # dribbble = models.URLField(blank=True)
    # behance = models.URLField(blank=True)
    # devto = models.URLField(blank=True)
    # codepen = models.URLField(blank=True)
    # foursquare = models.URLField(blank=True)
    # goodreads = models.URLField(blank=True)
    # hackernews = models.URLField(blank=True)
    # keybase = models.URLField(blank=True)
    # kaggle = models.URLField(blank=True)
    # lastfm = models.URLField(blank=True)

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