from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class Profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image','location']        