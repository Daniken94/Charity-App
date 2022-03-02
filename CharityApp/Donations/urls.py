from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import LandingPage, AddDonation



app_name = "donations"

urlpatterns = [
    path('', LandingPage.as_view(), name='landingpage'),
    path('adddonation/', AddDonation.as_view(), name='adddonation'),
]




# pgadmin dbeaver