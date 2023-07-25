from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
# Create your views here.

def user_login(request):
    if request.method == "POST":
        username =  request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password != password1:
            messages.error(request,"Password didnot match")
            return redirect('signup')
        # if User.objects.filter(username=username).exists:
        #     messages.error(request,"Username already exists")
        #     return redirect('signup')    
        # if User.objects.filter(email=email).exists:
        #     messages.error(request,"Email already exists")
        #     return redirect('signup')
        user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    return redirect('home')
        