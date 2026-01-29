from django.urls import path
from . import views

app_name = "playlists"

urlpatterns = [
    path("", views.my_playlists, name="my_playlists"),
]
