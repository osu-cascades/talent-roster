from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile


def index(request):
    return render(request, 'index.html')

def list(request):
    profiles = Profile.objects.order_by('last_name')
    output = ', '.join([p.full_name for p in profiles])
    return HttpResponse("List of profiles\n" + output)

def detail(request, profile_id):
    return HttpResponse("Display profile %s" % profile_id)
