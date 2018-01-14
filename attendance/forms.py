from django import forms
from django.contrib.auth.models import User
from .models import staff


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )

    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )


class RegisterForm(forms.ModelForm):

    class Meta:
        model=staff
        fields=('staff_id','name','category','department','qualification'
                ,'joining_date','termination_date')


