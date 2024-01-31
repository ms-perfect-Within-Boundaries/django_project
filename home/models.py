from django import forms

class UserLogin(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

def __str__(self):
        return self.username
  
"""# yourappname/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserLogin(AbstractUser):
    # Add any additional fields you need
    # Example:
    # profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    username = models.CharField(max_length=255, required=True, null=True, blank=True)
    password = models.CharField(widget=models.PasswordInput, required=True, null=True, blank=True)

def __str__(self):
        return self.username
  
"""


    