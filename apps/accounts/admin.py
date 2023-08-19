from django.contrib import admin
from apps.accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
    list_display_links = ["user"]
    search_fields = ["user"]
    list_filter = ["created_at"]

    class Meta:
        model = Profile