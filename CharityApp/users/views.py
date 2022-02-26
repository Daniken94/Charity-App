from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import MyRegisterForm, MyLoginForm




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
        form = MyLoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = MyLoginForm(request.POST)
        if form.is_valid():
            user = form.authenticated



def loginuser(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html")

    return render(request, "login.html")




# class LogoutUser(View):
#     def post(request):
#         logout(request)
#         return redirect("/login/")



def logoutuser(request):
    logout(request)
    return redirect("/")




