from django.contrib import admin
from .models import Playlist, PlaylistItem

# Register your models here.


class PlaylistItemInline(admin.TabularInline):
    model = PlaylistItem
    extra = 0
    ordering = ("position",)


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "visibility", "updated_at")
    list_filter = ("visibility", "created_at", "updated_at")
    search_fields = ("title", "description", "owner__username", "owner__email")
    inlines = [PlaylistItemInline]


@admin.register(PlaylistItem)
class PlaylistItemAdmin(admin.ModelAdmin):
    list_display = ("playlist", "position", "provider", "provider_id", "canonical_url")
    list_filter = ("provider",)
    search_fields = ("canonical_url", "cached_title", "provider_id")
    ordering = ("playlist", "position")
