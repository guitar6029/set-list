from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Playlist

@login_required
def my_playlists(request):
    playlists = Playlist.objects.filter(owner=request.user).order_by("-updated_at")
    return render(request, "playlists/my_playlists.html", {"playlists" : playlists})