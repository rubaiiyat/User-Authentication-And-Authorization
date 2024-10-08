from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def Register(request):
    if not request.user.is_authenticated:
        page = "Register"

        if request.method == "POST":
            form = forms.registration(request.POST)
            if form.is_valid():
                messages.success(request, "Account Created Successfully")
                form.save()
                return redirect("register")
        else:
            form = forms.registration()
        return render(request, "Register.html", {"page": page, "form": form})
    else:
        return redirect("profile")


def userLogin(request):
    if not request.user.is_authenticated:
        page = "Login"
        if request.method == "POST":
            form = AuthenticationForm(request.POST)
            name = request.POST["username"]
            userPass = request.POST["password"]
            user = authenticate(request, username=name, password=userPass)

            if user is not None:
                messages.success(request, "Logged In Successfully")
                login(request, user)
                return redirect("profile")
            else:
                messages.warning(request, "Invalid Username or Password")

        else:
            form = AuthenticationForm()

        return render(request, "login.html", {"page": page, "form": form})
    else:
        return redirect("profile")


@login_required
def userProfile(request):
    page = "Profile"
    data = request.user
    return render(request, "profile.html", {"data": data, "page": page})


@login_required
def editProfile(request):
    if request.method == "POST":
        form = forms.updateProfile(request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request, "Updated Profile Successfully")
            form.save()
            return redirect("profile")
    else:
        form = forms.updateProfile(instance=request.user)
    return render(request, "Edit_Profile.html", {"form": form})


@login_required
def chngPass(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Updated Password Successfully")
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "chngPass.html", {"form": form})


@login_required
def chngPass2(request):
    if request.method == "POST":
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Updated Password Successfully")
            return redirect("profile")
    else:
        form = SetPasswordForm(request.user)

    return render(request, "chngPass.html", {"form": form})


@login_required
def userLogout(request):
    messages.success(request, "Logged Out Successfully")
    logout(request)

    return redirect("home")
