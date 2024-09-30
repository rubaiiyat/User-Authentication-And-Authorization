from django.shortcuts import render

# Create your views here.


def Register(request):
    return render(request, "Register.html")


def userLogin(request):
    return render(request, "login.html")
