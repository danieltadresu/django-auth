from django.shortcuts import render

from django.contrib.auth.models import User

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

# Create your views here.

def getIndex(request):
    return render(request, 'index.html')

def getLogIn(request):
    return render(request, 'registration/login.html')

def postLogIn(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        print(' No backend authenticated the credentials')
    return render(request, 'index.html')

def getSignUp(request):
    return render(request, 'registration/signup.html')

def postSignUp(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    user.save()
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return render(request, 'index.html')

def getLogOut(request):
    logout(request)
    return render(request, 'index.html')
