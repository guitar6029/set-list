from django.shortcuts import render

# Create your views here.
from playlists.models import Playlist


def home(request):
    playlists = Playlist.objects.filter(visibility=Playlist.Visibility.PUBLIC).order_by(
        "-updated_at"
    )[:12]

    return render(request, "pages/home.html", {"playlists": playlists})
