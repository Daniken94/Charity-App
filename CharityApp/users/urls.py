from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Login, LogoutUser, Register, AdminPage, UserPage



app_name = "users"

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('admin/', AdminPage.as_view(), name='admin'),
    path('user/', UserPage.as_view(), name='user'),
]