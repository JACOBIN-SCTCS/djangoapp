from django import forms
from django.contrib.auth.models import User
from .models import staff


class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username' ,'password')



class RegisterForm(forms.ModelForm):

    class Meta:
        model=staff
        fields=('staff_id','name','category','department','qualification'
                ,'joining_date','termination_date')


