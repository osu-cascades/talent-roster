from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    return render(request, 'profiles/index.html')

def list(request):
    profiles = Profile.objects.order_by('last_name')
    return render(request, 'profiles/list.html', {'profiles': profiles})

def detail(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'profiles/detail.html', {'profile': profile})
