from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Informaion', {'fields':['first_name','last_name', 'email','bio']}),
        ('Profile Informaion', {'fields':['graduation_date','skills','github_username','photo','resume','website_url']}),
    ]
    list_display = ('email', 'first_name', 'last_name','graduation_date')
    list_filter =['graduation_date']

admin.site.register(Profile, ProfileAdmin)


