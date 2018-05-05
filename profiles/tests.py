import unittest
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Profile


class ProfileViewTests(TestCase):

    def test_index_renders_featured_profile(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Featured Profile")


    def test_list_renders_profiles(self):
        response = self.client.get(reverse('profiles:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Profiles")


    def test_list_renders_no_profiles_when_none_exist(self):
        response = self.client.get(reverse('profiles:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No profiles are available")


    def test_detail_renders_student_profile(self):
        profile = create_profile()
        response = self.client.get(reverse('profiles:detail', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fake Student")


class ProfileModelTests(TestCase):

    def test_has_full_name(self):
        self.fail("TODO @rkojan")
        # Create a profile object using create_profile()
        # Assert that the profile objects full_name is equal to "Fake Student"


# Test helpers

def create_profile():
     return Profile.objects.create(
         first_name="Fake",
         last_name="Student",
         email="fake@example.com",
         github_username="fake",
         bio="Fake bio",
         graduation_date=timezone.now(),
         photo="fake",
         resume="fake",
         skills="fake",
         website_url="fake"
     )
