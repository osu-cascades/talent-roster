from django.contrib import admin
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget = forms.Textarea(attrs={'rows': 5, 'cols': 100}))


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    fieldsets = [
        (None, {'fields':[('first_name','last_name'), ('email', 'graduation_date'), 'bio', 'photo', 'resume', 'skills', 'github_username','website_url']}),
    ]
    list_display = ('last_name', 'first_name', 'email', 'graduation_date')
    list_filter =['graduation_date']


admin.site.register(Profile, ProfileAdmin)
