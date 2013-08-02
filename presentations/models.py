#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class Track(models.Model):
    """
    Clase para almacenar información 
    referente a los track de la conferencia
    """
    name = models.CharField(max_length=32)
    description = models.TextField()
    room = models.CharField(max_length=256)

    def __unicode(self):
        return '%s | %s' % (self.name, self.room)


class Presentation(models.Model):
    """
    Clase para almacenar información acerca de 
    las distintas presentaciones de la conferencia
    """
    speakers = models.ManyToManyField(User)
    track = models.ForeignKey(Track)
    title = models.CharField(max_length=256)
    description = models.TextField()
    requirements = models.TextField()
    approved = models.BooleanField(default=False)
    start = models.DateTimeField()
    duration = models.IntegerField()
    slides = models.URLField(max_length=256,null=True, blank=True)

    def __unicode__(self):
        return self.title
# Create your models here.
