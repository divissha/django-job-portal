from django import forms
from .models import Application
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application

        fields = [
         
            'resume'
        ]

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]