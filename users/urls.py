#coding=utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('users.views',
    url(r'register/$', 'user_register', name='user-register'),
    url(r'activate/(?P<encoded>.+)/$', 'validate', name='user-validate'),
)
