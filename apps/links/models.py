from django.db import models

from apps.accounts.models import Profile
from django.contrib.auth.models import User
from apps.common.models import CoreModel
from apps.tags.models import Tag

SOCIAL_ACCOUNTS = [
    ("website", "Website"),
    ("linkedin", "LinkedIn"),
    ("instagram", "Instagram"),
    ("tiktok", "TikTok"),
    ("twitter", "Twitter"),
    ("facebook", "Facebook"),
    ("github", "GitHub"),
    ("youtube", "YouTube"),
    ("medium", "Medium"),
    ("reddit", "Reddit"),
    ("stackoverflow", "Stack Overflow"),
    ("discord", "Discord"),
    ("twitch", "Twitch"),
    ("steam", "Steam"),
    ("spotify", "Spotify"),
    ("pinterest", "Pinterest"),
    ("snapchat", "Snapchat"),
    ("tumblr", "Tumblr"),
    ("vimeo", "Vimeo"),
    ("whatsapp", "WhatsApp"),
    ("telegram", "Telegram"),
    ("skype", "Skype"),
    ("quora", "Quora"),
    ("soundcloud", "SoundCloud"),
    ("github_gist", "GitHub Gist"),
    ("dribbble", "Dribbble"),
    ("behance", "Behance"),
    ("devto", "Dev.to"),
    ("codepen", "CodePen"),
    ("foursquare", "Foursquare"),
    ("goodreads", "Goodreads"),
    ("hackernews", "Hacker News"),
    ("keybase", "Keybase"),
    ("kaggle", "Kaggle"),
    ("lastfm", "Last.fm"),
    ("gitlab", "GitLab"),
    ("bitbucket", "Bitbucket"),
    ("mixcloud", "Mixcloud"),
    ("producthunt", "Product Hunt"),
    ("slideshare", "SlideShare"),
    ("basecamp", "Basecamp"),
    ("freecodecamp", "freeCodeCamp"),
    ("wordpress", "WordPress"),
    ("aboutme", "About.me"),
    ("bandcamp", "Bandcamp"),
]


class SocialNetwork(CoreModel):
    network = models.CharField(max_length=255, choices=SOCIAL_ACCOUNTS)
    base_url = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag, related_name="social_networks", blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.network


class Link(CoreModel):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name="links"
    )
    title = models.ForeignKey(SocialNetwork, on_delete=models.PROTECT, related_name="link")
    url = models.URLField(max_length=255)
    # tags = models.ManyToManyField(Tag, related_name="links", blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.url


class CustomLink(CoreModel):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="customlinks"
    )
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title