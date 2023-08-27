from django.contrib import admin
from .models import Link, SocialNetwork


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Link._meta.fields]
    list_display_links = ["profile", "url"]
    search_fields = ["profile", "title", "url"]
    list_filter = ["created_at"]

    class Meta:
        model = Link


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SocialNetwork._meta.fields]
    list_display_links = ["network", "base_url"]
    search_fields = ["network", "base_url"]
    list_filter = ["created_at"]

    class Meta:
        model = SocialNetwork