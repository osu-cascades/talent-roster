from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Profile

def index(request):
    return render(request, 'profiles/index.html')

def profile(request):
    return render(request, 'profiles/profile.html', output)

def sign_up(request):
    return render(request, 'profiles/signup.html')

def log_in(request):
    return render(request, 'profiles/login.html')

def account(request):
    return render(request, 'profiles/account.html')

def business(request):
    return render(request, 'profiles/business.html')

def profiles(request):
    all_profiles = Profile.objects.order_by('-first_name')
    context = {'all_profiles': all_profiles}
    print(context)
    print(context)

    return render(request, 'profiles/profiles.html',context)
