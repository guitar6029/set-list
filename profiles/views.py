from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.


@login_required
def account(request):
    Profile.objects.get_or_create(user=request.user)

    current = request.user.profile.avatar
    avatars = [
        {"value": "original", "label": "Original", "filename": "ORIGINAL.jpg"},
        {"value": "book_worm", "label": "Book Worm", "filename": "BOOK_WORM.jpg"},
        {"value": "guitarist", "label": "Guitarist", "filename": "GUITARIST.jpg"},
        {"value": "astronaut", "label": "Astronaut", "filename": "ASTRONAUT.jpg"},
    ]

    for a in avatars:
        a["is_selected"] = (a["value"] == current)

    return render(request, "profiles/account.html", {"avatars": avatars})


@login_required
def update_avatar(request):
    if request.method != "POST":
        return redirect("profiles:account")

    # retrieve the selected choice
    avatar_choice = request.POST.get("avatar")

    valid_choices = {key for key, _label in Profile.Avatar.choices}
    if avatar_choice not in valid_choices:
        return redirect("profiles:account")

    # update the profile
    profile, _ = Profile.objects.get_or_create(user=request.user)
    profile.avatar = avatar_choice
    profile.save(update_fields=["avatar"])

    return redirect("profiles:account")
