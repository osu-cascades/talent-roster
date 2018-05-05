from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('<int:profile_id>/', views.detail, name='detail'),
]
