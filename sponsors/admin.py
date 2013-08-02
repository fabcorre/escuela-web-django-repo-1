#coding=utf-8
from django.contrib import admin
from .models import Sponsor, SponsorshipTypes



admin.site.register(Sponsor)
admin.site.register(SponsorshipTypes)
