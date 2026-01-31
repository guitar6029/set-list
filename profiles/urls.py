from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.account, name="account"),
    path("avatar/", views.update_avatar, name="update_avatar" )
]
