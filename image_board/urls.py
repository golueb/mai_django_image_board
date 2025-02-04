from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import *

urlpatterns = [
    # Главная страница
    path('', MainPageView.as_view(), name='home')
]