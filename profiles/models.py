from django.db import models

class Profiles(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    photo = models.CharField(max_length=100)
    resume = models.CharField(max_length=100)
    skills = models.CharField(max_length=250)
    bio = models.CharField(max_length=250)
    git_hub = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    graduation_date = models.DateField(blank=False)

    
