from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Login, Register



app_name = "users"

urlpatterns = [
    path('logina/', Login.as_view(), name='logina'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', Register.as_view(), name='register'),
]