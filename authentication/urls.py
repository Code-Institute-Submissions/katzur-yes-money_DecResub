from . import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import RegistrationView, UsernameValidationView, EmailValidationView, LoginView, IndexView, LogoutView, ContactView


urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('validate-username', csrf_exempt(
        UsernameValidationView.as_view()), name="validate-username"),
    path('validate-email', csrf_exempt(
        EmailValidationView.as_view()), name="validate_email"),
    path('index', IndexView.as_view(), name="index"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('contact', views.contact, name="contact"),
]
