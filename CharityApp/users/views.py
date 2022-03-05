from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import MyRegisterForm, LoginForm
from Donations.models import Donations, Institution



class Register(View):
    def get(self, request):
        form = MyRegisterForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
        return render(request, "login.html", {"form": form})
            # return redirect('register')


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return redirect("/users/login/")


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect("/")


class AdminPage(View):
    def get(self, request):
        return redirect("/admin")


class UserPage(View):
    def get(self, request):
        current_user = request.user.id
        user_don = Donations.objects.filter(user_id=current_user)
        inst = Institution.objects.all()

        return render(request, "profile.html", {"user_don": user_don, "inst": inst})






