#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Clase para almacenar información referente a
    Perfiles de usuarios
    """
    user = models.OneToOneField(User)
    gravatar = models.CharField(max_length=32)
    about = models.TextField(null=True, blank=True)
    twitter = models.CharField(max_length=16)
    blog = models.URLField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.twitter

class RegistrationProfile(models.Model):
    """
    Clase para almacenar datos de validación
    de lo usuarios cuando se registran
    """
    user = models.OneToOneField(User)
    token = models.CharField(max_length=32)
    encoded = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    consumed = models.DateTimeField(blank=True, null=True)
# Create your models here.
