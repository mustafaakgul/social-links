from django.contrib import admin
from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]
    list_display_links = ["name"]
    search_fields = ["name"]
    list_filter = ["created_at"]

    class Meta:
        model = Tag
