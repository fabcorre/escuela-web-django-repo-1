#encoding=utf-8
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.core import mail
from .factories import UserProfileFactory, RegistrationProfileFactory
from .models import RegistrationProfile, UserProfile

class UserRegistrationTest(TestCase):
    def setUp(self):
        self.post_data = {
            'username': 'test-user', 
            'email': 'test_user@test.com',
            'first_name': 'Foo',
            'last_name': 'Bar',
            'password': '12341234',
            'passwordr': '12341234',
        }
        self.client = Client()

    def test_user_registration_ok(self):
        self.assertEquals(User.objects.count(), 0)
        self.assertEquals(UserProfile.objects.count(), 0)
        self.assertEquals(RegistrationProfile.objects.count(), 0)

        response = self.client.post(reverse('user-register'), self.post_data)

        self.assertEquals(User.objects.count(), 1)
        self.assertEquals(UserProfile.objects.count(), 1)
        self.assertEquals(RegistrationProfile.objects.count(), 1)
        self.assertEquals(len(mail.outbox),1)
        user = User.objects.get(username=self.post_data['username'])
        self.assertFalse(user.is_active)


class UserValidationTest(TestCase):
    def setUp(self):
        self.reg_profile = RegistrationProfileFactory()
        self.reg_profile.user.is_active = False
        self.reg_profile.user.save()
        self.user_profile = UserProfileFactory(user=self.reg_profile.user)
        self.reg_profile.save()
        self.user_profile.save()
        self.client = Client()

    def test_user_validation_ok(self):
        self.assertFalse(self.reg_profile.consumed)
        
        url_args = {
            'encoded':self.reg_profile.encoded,
        }
        response = self.client.get(reverse('user-validate', kwargs=url_args))

        user = User.objects.get(id=self.reg_profile.user.id)
        rp = RegistrationProfile.objects.get(id=self.reg_profile.id)
        self.assertTrue(user.is_active)
        self.assertTrue(rp.consumed)
