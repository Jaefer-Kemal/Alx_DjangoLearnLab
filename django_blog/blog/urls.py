from django.urls import path
from .views import register, index, profile_view
from django.contrib.auth import views as auth_views

# Define URL patterns in blog/urls.py
# to handle paths for login (/login),
# logout (/logout), registration (/register),
# and profile management (/profile).

app_name = "blog"
urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="blog/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="blog/logout.html", http_method_names=["get", "post"]
        ),
        name="logout",
    ),
    path('profile/', profile_view, name='profile'),
]
