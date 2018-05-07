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