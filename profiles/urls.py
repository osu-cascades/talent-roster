from django.urls import path,include
from . import views
from django.views.generic.base import TemplateView

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.ListView.as_view(), name='list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('business/', views.business, name='business'),
    path('login/', views.login, name='login'),
]
