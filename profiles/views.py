from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Profile

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html', output)

def sign_up(request):
    return render(request, 'signup.html')

def log_in(request):
    return render(request, 'login.html')

def account(request):
    return render(request, 'account.html')

def business(request):
    return render(request, 'business.html')

def profiles(request):

    all_profiles = Profile.objects.all()
    context = {'first_name': all_profiles}

    return render(request, 'profiles.html',context)
