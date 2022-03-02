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
        
        count_organ = Institution.objects.filter(donations__isnull=False).distinct().count()
        count_bags = Donations.objects.all().aggregate(Sum('quantity'))    

        return render(request, "index.html", {"fundations": fundations, "organ": organ, "local": local, 
                                                "count_bags": count_bags, "count_organ": count_organ})
        



class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")
