from django import forms
from django.contrib.auth.models import User

class ConnectForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30);
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput);

class UserCreationForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30);
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput);
	repassword = forms.CharField(label="Répéter", widget=forms.PasswordInput, help_text="Enter the same password as above, for verification.");

