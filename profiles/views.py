from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Profile


def index(request):
    return render(request, 'profiles/index.html')


class ListView(generic.ListView):
    template_name = 'profiles/list.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.order_by('last_name')


class DetailView(generic.DetailView):
    model = Profile
    template_name = 'profiles/detail.html'
