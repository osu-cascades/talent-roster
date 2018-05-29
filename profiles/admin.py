from django.contrib import admin
from django import forms
from .models import Profile, Skill


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget = forms.Textarea(attrs={'rows': 5, 'cols': 100}), help_text='500 character maximum')


class SkillForm(forms.ModelForm):
    level = forms.IntegerField(max_value = 5, min_value = 1, widget = forms.Select(choices=(('', 'Choose...'), ('1', '1 (exposed)'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5 (expert)'))))


class SkillInline(admin.StackedInline):
    form = SkillForm
    model = Skill
    extra = 5


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    fieldsets = [
        (None, {'fields': [('first_name','last_name'), ('email_address', 'graduation_date'), 'bio', ('photo', 'resume'), 'github_username','website_url']}),
    ]
    list_display = ('last_name', 'first_name', 'email_address', 'graduation_date')
    list_filter =['graduation_date']
    inlines = [SkillInline]


admin.site.register(Profile, ProfileAdmin)
