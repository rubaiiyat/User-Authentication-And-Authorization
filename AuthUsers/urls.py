from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.Register, name="register"),
    path("login/", views.userLogin, name="login"),
    path("profile/", views.userProfile, name="profile"),
    path("logout/", views.userLogout, name="logout"),
]
