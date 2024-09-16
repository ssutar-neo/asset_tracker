from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=True, label='Remember me')
