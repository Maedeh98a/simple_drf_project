from django.contrib import admin
from api_profile.models import UserProfile, ProfileFeedItem


admin.site.register(UserProfile)


@admin.register(ProfileFeedItem)
class ProfileFeedItemAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'status_text']