#encoding=utf-8
from django.db import models

class State(models.Model):
    """
    Información de estados geográficos
    """
    name = models.CharField(max_length=32)

    def __unicode__(self):
       return self.name
# Create your models here.
