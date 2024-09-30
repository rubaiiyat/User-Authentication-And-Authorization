from django.shortcuts import render


def home(request):
    page = "Home"
    return render(request, "home.html", {"page": page})
