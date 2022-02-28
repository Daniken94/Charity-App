from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Login, LogoutUser, Register



app_name = "users"

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
]