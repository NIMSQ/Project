from django import forms
from .models import Login
class LoginForm(forms.Form):
     username = forms.CharField(max_length = 50)
     password = forms.CharField(max_length=50, widget=forms.PasswordInput)