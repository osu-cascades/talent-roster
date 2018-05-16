from django.contrib import admin
from django.urls import include, path
from profiles import views

urlpatterns = [
    path('', views.index),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
