from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewUserForm
from .models import Profile


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("myapp:index")
    form = NewUserForm()
    context = {"form": form}
    return render(request, "users/register.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        contact_numer = request.POST.get("number")
        image = request.FILES["upload"]
        user = request.user
        profile = Profile(user=user, contact_numer=contact_numer, image=image)
        profile.save()
    return render(request, "users/profile.html")


def seller_profile(request, id):
    seller = User.objects.get(id=id)
    context = {"seller": seller}
    return render(request, "users/seller_profile.html", context)