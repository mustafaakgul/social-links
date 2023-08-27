from django.db import models

from apps.accounts.models import Profile
from apps.common.models import CoreModel

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


class Link(CoreModel):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name="links"
    )
    title = models.CharField(max_length=255, choices=SOCIAL_ACCOUNTS)
    url = models.URLField(max_length=255)
    #tags = models.ManyToManyField("links.Tag", related_name="links", blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title