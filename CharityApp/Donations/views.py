from django.shortcuts import render
from django.views import View






def Homepage(request):
    return render(request, "index.html")
