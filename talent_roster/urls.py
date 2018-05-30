from django.contrib import admin,auth
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from profiles import views
from django.views.generic.base import TemplateView

admin.site.site_header = 'Talent Roster Administration'
admin.site.site_title = 'Talent Roster Administration'

urlpatterns = [
    path('', views.index),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
