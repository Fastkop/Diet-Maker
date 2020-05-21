from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method is 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            messages.error(request, "Invalid Credentials")
            return redirect('/login')
        else:
            return redirect(request, '/')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method is 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            messages.error(request, "Invalid Credentials")
            return redirect('/login')
        else:
            return redirect(request, '/')
    else:
        return render(request, 'signup.html')
