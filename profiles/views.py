from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def detail(request, profile_id):
    return HttpResponse("Display profile %s" % profile_id)
