from django.shortcuts import render
from django.http import HttpResponse
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
    return HttpResponse("Display profile %s" % profile_id)
