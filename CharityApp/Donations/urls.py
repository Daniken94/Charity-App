from django.contrib import admin
from . import views
from django.urls import path




app_name = "donations"


urlpatterns = [
    path('', views.Homepage, name='homepage'),
]