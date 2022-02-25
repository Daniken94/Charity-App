from django.shortcuts import render
from django.views import View
from .forms import MyRegisterForm




class Register(View):
    def get(self, request):
        form = MyRegisterForm()
        return render(request, "register2.html", {"form": form})

    def post(self, request):
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
        return render(request, "register2.html", {"form": form})


class Login(View):
    pass










