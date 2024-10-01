from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.Register, name="register"),
    path("login/", views.userLogin, name="login"),
    path("profile/", views.userProfile, name="profile"),
    path("profile/edit/", views.editProfile, name="edit_profile"),
    path("profile/changepassword/", views.chngPass, name="chngpass"),
    path("profile/changepassword2/", views.chngPass2, name="chngpass2"),
    path("logout/", views.userLogout, name="logout"),
]
