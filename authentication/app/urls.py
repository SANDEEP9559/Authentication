from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('success', views.success, name="success"),
    path('token_send', views.token_send, name="token_send"),
    
]