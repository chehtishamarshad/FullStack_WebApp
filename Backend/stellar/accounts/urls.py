# accounts/urls.py

from django.urls import path
from .views import RegisterView, LoginView, HomePageView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("", HomePageView.as_view(), name="home"),
]
