# Generated by Django 4.2.4 on 2023-08-27 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tags", "0001_initial"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialNetwork",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "network",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=255,
                    ),
                ),
                ("base_url", models.URLField(max_length=255)),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="social_networks", to="tags.tag"
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("url", models.URLField(max_length=255)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="links",
                        to="accounts.profile",
                    ),
                ),
                (
                    "title",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="link",
                        to="links.socialnetwork",
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
    ]
