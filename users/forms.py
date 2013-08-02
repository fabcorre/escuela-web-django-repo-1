#coding=utf-8
from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
	username = forms.CharField(max_length=32)
	email = forms.EmailField()
	first_name = forms.CharField(max_length=32)
	last_name = forms.CharField(max_length=32)
	password = forms.CharField(max_length=16, widget=forms.PasswordInput)
	passwordr = forms.CharField(max_length=16, widget=forms.PasswordInput)

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			user = User.objects.get(email=email)
			raise forms.ValidationError('El correo %s ya esta regitrado' % email)
		except:
			return email

	def clean_passwordr(self):
		pwd = self.cleaned_data['password']
		pwdr = self.cleaned_data['passwordr']

		if pwd == pwdr:
			return pwd

		raise forms.ValidationError('El password no coincide')
