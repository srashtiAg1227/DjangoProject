from django.urls import path, include
from .import views
from .views import *

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view()),
    path('password_encrypt/', views.PasswordEncryptionView.as_view()),
    path('login/', views.UserLoginView.as_view()),
]
