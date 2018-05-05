from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Profile

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html', output)

def sign_up(request):
    return render(request, 'signup.html')

def log_in(reguest):
    return render(reguest, 'login.html')

def account(reguest):
    return render(reguest, 'account.html')

def business(reguest):
    return render(reguest, 'business.html')

def profiles(reguest):

    all_profiles = Profile.objects.all()
    output = ', '.join([r.first_name for r in all_profiles])
    print(output)

    return render(reguest, 'profiles.html')
