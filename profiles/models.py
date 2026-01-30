from django.db import models
from django.conf import settings


class Profile(models.Model):
    class Avatar(models.TextChoices):
        ASTRONAUT = "astronaut", "Astronaut"
        GUITARIST = "guitarist", "Guitarist"
        BOOK_WORM = "book_worm", "Book Worm"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )

    avatar = models.CharField(
        max_length=32, choices=Avatar.choices, default=Avatar.ASTRONAUT
    )

    updated_at = models.DateTimeField(auto_now=True)
