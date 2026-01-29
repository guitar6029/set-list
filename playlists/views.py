from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Playlist


@login_required
def my_playlists(request):
    playlists = Playlist.objects.filter(owner=request.user).order_by("-updated_at")
    return render(request, "playlists/my_playlists.html", {"playlists": playlists})


@login_required
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id, owner=request.user)

    # items come from the related_name="items" on PlaylistItem.playlist
    items = playlist.items.all().order_by("position")

    return render(
        request,
        "playlists/playlist_detail.html",
        {"playlist": playlist, "items": items},
    )
