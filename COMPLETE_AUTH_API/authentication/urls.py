from django.urls import path, include
from .import views
from .views import *

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view()),
]
