from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def list(request):
    return HttpResponse("List of profiles")

def detail(request, profile_id):
    return HttpResponse("Display profile %s" % profile_id)
