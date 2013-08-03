#coding=utf-8
from django.forms import ModelForm
from .models import Presentation

class CreateEditPresenationForm(ModelForm):
    class Meta:
        model = Presentation


