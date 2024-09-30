from django.shortcuts import render
from . import forms
from django.contrib.auth import login, logout


def Register(request):
    page = "Register"

    if request.method == "POST":
        form = forms.registration(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.registration()
    return render(request, "Register.html", {"page": page, "form": form})
