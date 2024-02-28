from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class Logform(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))

class Regform(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        widgets={
            # "first_name":forms.TextInput(attrs={"class":"form-control mb-4"}),
            # "last_name":forms.TextInput(attrs={"class":"form-control mb-4"}),
            "username":forms.TextInput(attrs={"class":"form-control "}),
            "email":forms.EmailInput(attrs={"class":"form-control mb-4"}),
     
        }



