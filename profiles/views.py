from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Profile


def index(request):
    return render(request, 'profiles/index.html')

def list(request):
    profiles = Profile.objects.order_by('last_name')
    context = {
        'profiles': profiles
    }
    return render(request, 'profiles/list.html', context)

def detail(request, profile_id):
    try:
        profile = Profile.objects.get(pk=profile_id)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'profiles/detail.html', {'profile': profile})
