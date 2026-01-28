from django.db import models
import uuid

# Create your models here.

from django.conf import settings


class Playlist(models.Model):
    class Visibility(models.TextChoices):
        PRIVATE = "private", "Private"
        UNLISTED = "unlisted", "Unlisted"
        PUBLIC = "public", "Public"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="playlists"
    )

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    visibility = models.CharField(
        max_length=16, choices=Visibility.choices, default=Visibility.PRIVATE
    )

    share_token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["updated_at"]
        indexes = [models.Index(fields=["owner", "visibility"])]

    def __str__(self):
        return f"{self.title}"
