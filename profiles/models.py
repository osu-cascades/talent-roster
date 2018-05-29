from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40, blank=False)
    email_address = models.EmailField(blank=False)
    graduation_date = models.DateField(blank=False)
    bio = models.CharField(max_length=500, blank=False)
    photo = models.ImageField()
    resume = models.FileField()
    github_username = models.CharField(max_length=50, blank=False)
    website_url = models.URLField()

    def full_name(self):
        return  "%s %s" % (self.first_name, self.last_name)


class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=False)
    level = models.PositiveIntegerField(blank=False)
