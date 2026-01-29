from django.shortcuts import render, redirect
from django.contrib.auth import login

from accounts.forms import SignUpForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # check if username exists ?
            user = form.save()
            login(request, user)  # auto login after signup
            return redirect("playlists:my_playlists")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})
