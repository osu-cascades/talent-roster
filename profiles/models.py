from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40, blank=False)
    email = models.CharField(max_length=50, blank=False)
    github_username = models.CharField(max_length=50, blank=False)
    bio = models.CharField(max_length=500, blank=False)
    graduation_date = models.DateField(blank=False)
    photo = models.CharField(max_length=250)
    resume = models.CharField(max_length=250)
    skills = models.CharField(max_length=250)
    website_url = models.CharField(max_length=50)


    def full_name(self):
        return  "%s %s" % (self.first_name, self.last_name)
