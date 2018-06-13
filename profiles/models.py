from django.db import models


def profile_media_path(instance, filename):
    return 'profiles/owner_{0}/{1}'.format('TODO', filename)


class Profile(models.Model):
    first_name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40, blank=False)
    email_address = models.EmailField(blank=False)
    graduation_date = models.DateField(blank=False)
    bio = models.CharField(max_length=500, blank=False)
    #photo = models.ImageField(upload_to=profile_media_path)
    resume = models.FileField(upload_to=profile_media_path)
    github_username = models.CharField(max_length=50, blank=False)
    website_url = models.URLField()

    def full_name(self):
        return  "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return self.full_name()


class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=False)
    CHOICES = [(None, 'Choose...'), (1, '1 (exposed)'), (2, '2'), (3, '3'), (4, '4'), (5, '5 (expert)')]
    level = models.PositiveIntegerField(blank=False, choices=CHOICES)

