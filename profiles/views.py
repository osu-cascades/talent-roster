from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Profile


def index(request):
    return render(request, 'profiles/index.html')

def business(request):
    return render(request, 'profiles/business.html')


class ListView(generic.ListView):

    def get_queryset(self):
        return Profile.objects.order_by('last_name')


class DetailView(generic.DetailView):
    model = Profile



# Delete these once you see that we do not need them.
# profile -> handled by DetailView above.
# sign_up -> handled by Django admin automatically
# log_in ->  handled by Django admin automatically
# account -> handled by Django admin automatically
# profiles -> handled by ListView above.


def profile(request):
    return render(request, 'profiles/profile.html', output)

def sign_up(request):
    return render(request, 'profiles/signup.html')

def log_in(request):
    return render(request, 'profiles/login.html')

def account(request):
    return render(request, 'profiles/account.html')

def profiles(request):
    all_profiles = Profile.objects.order_by('-first_name')
    context = {'all_profiles': all_profiles}
    print(context)
    print(context)

    return render(request, 'profiles/profiles.html',context)