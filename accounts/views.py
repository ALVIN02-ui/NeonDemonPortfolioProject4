from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
# Create your views here.


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Your account has been created {user.username}')
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

@receiver(user_logged_in)
def show_login_message(sender, user, request, **kwargs):
    messages.info(request, f"Welcome, you are now logged in as {user.username}")

@receiver(user_logged_out)
def show_logout_message(sender, user, request, **kwargs):
    if user is not None:
        messages.info(request, f"Goodbye {user.username}, you have logged out")
