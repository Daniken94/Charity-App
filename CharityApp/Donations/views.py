from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Count, Min, Max, Avg, Sum
from .models import Category, Donations, Institution
from .forms import AddDonationForm





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
        form = AddDonationForm(user=request.user)

        current_user = request.user.id
        category = Category.objects.all()
        inst = Institution.objects.all()

        if current_user is not None:
            return render(request, "form.html", {"category": category, "inst": inst, "form": form})
        else:
            return redirect("/users/login/")

    def post(self, request):
        form = AddDonationForm(request.POST, user=request.user)
        
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.save()
        return render(request, "form-confirmation.html", {"form": form})
