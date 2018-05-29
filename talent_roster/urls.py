from django.contrib import admin
from django.urls import include, path
from profiles import views

admin.site.site_header = 'Talent Roster Administration'
admin.site.site_title = 'Talent Roster Administration'

urlpatterns = [
    path('', views.index),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
