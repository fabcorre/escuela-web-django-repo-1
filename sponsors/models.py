#coding=utf-8
from django.db import models

class SponsorshipTypes(models.Model):
    """
    Clase para almacenar información acerca de los
    tipos de patrocinio de la conferencia
    """    
    name = models.CharField(max_length=32)
    description = models.TextField()
    range_start = models.IntegerField(null=True, blank=True)
    range_end = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Sponsor(models.Model):
    """
    Clase para almacenar información acerca de los
    patrocinantes de la conferencia
    """
    name = models.CharField(max_length=32)
    description = models.TextField()
    logo = models.ImageField(upload_to='sponsor_logos/')
    website = models.URLField(max_length=256)

    def __unicode__(self):
        return self.name
# Create your models here.
