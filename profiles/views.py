from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile


def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def sign_up(request):
    return render(request, 'signup.html')

def log_in(reguest):
    return render(reguest, 'login.html')