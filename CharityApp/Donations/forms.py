from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Donations




class AddDonationForm(ModelForm):
    class Meta:
        model = Donations
        fields = ["quantity", "city", "street", "home_number", "phone_number", "zip_code", "pick_up_date", "pick_up_time", 
                                        "pick_up_comment", "institution", "categories"]