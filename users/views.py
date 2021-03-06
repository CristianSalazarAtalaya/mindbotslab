
#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#Exceptios
from django.db.utils import IntegrityError

#models
from django.contrib.auth.models import User


# Create your views here.
def login_view(request):
    """login view"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("hi")
        else:
            return render(request,'users/login.html',{'error': 'Invalid username an pasword'})
        
    
    return render(request, 'users/login.html')



@login_required
def logout_view(request):
    """logout user"""
    logout(request)
    return redirect("users:login")

