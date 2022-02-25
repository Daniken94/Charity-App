from django.shortcuts import render
from django.views import View
from .models import Donations, Institution
from django.contrib.auth.forms import UserCreationForm


# "count_bags": count_bags
# czy anahory mają tak wyglądać, bo niby działa
# wyświetlanie kategorii w fundacjach



class LandingPage(View):
    def get(self, request):
        donations = Donations.objects.all()
        fundations = Institution.objects.filter(type="fundacja")
        organ = Institution.objects.filter(type="organizacja pozarządowa")
        local = Institution.objects.filter(type="zbiórka lokalna")

        count_organ = Donations.objects.all().count()
        # count_bags = Donations.objects.filter(donations__gt=0).count()

        return render(request, "index.html", {"count_organ": count_organ, "fundations": fundations, "organ": organ, "local": local})
        # "count_bags": count_bags



class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")



class Login(View):
    def get(self, request):
        return render(request, "login.html")



class Register(View):
    def get(self, request):
        return render(request, "register.html")
