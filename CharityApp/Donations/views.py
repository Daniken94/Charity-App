from django.shortcuts import render
from django.views import View
from django.db.models import Count, Min, Max, Avg, Sum
from .models import Donations, Institution
from django.contrib.auth.forms import UserCreationForm


# "count_bags": count_bags




class LandingPage(View):
    def get(self, request):
        fundations = Institution.objects.filter(type="fundacja")
        organ = Institution.objects.filter(type="organizacja pozarządowa")
        local = Institution.objects.filter(type="zbiórka lokalna")
        
        count_organ = Donations.objects.all().values('institution')
        count_bags = Donations.objects.all().aggregate(Sum('quantity'))

        empty = []
        count_organs = 0
        for i in count_organ:
            if i not in empty:
                count_organs += 1
                empty.append(i)
    

        return render(request, "index.html", {"fundations": fundations, "organ": organ, "local": local, 
                                                "count_bags": count_bags, "count_organs": count_organs})
        



class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")



class Login(View):
    def get(self, request):
        return render(request, "login.html")



class Register(View):
    def get(self, request):
        return render(request, "register.html")
