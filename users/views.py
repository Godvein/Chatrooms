from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as user_logout
from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login
# Create your views here.

def logout(request):
    user_logout(request)
    return redirect("home")

def register(request):
    if request.method == "POST":
        
        username = request.POST.get("username")
        if User.objects.filter(username = username).exists():
            messages.error(request, "username already exists")
            return redirect("register")
        password = request.POST.get("password")
        user = User(username = username, password = password)
        user.save()
        messages.success(request, "account created successfully please login")
        return redirect("login")
    return render(request, "users/register.html")

def login(request):
    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            return redirect("home")
        else:
            messages.error(request, "username or password didnt match")
            return redirect("login")
        
    return render(request, "users/login.html")
