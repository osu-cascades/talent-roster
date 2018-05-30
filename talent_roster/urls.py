from django.contrib import admin,auth
from django.urls import include, path
from profiles import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
