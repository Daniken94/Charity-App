from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import MyRegisterForm, LoginForm




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






