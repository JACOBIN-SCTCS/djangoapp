from django import forms
from .models import leave_request
from .models import staff
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
        
    )

    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
        
    )

    def clean(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry that login was invalid")

        return self.cleaned_data

    def login(self,request):
        username=self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class RegisterForm(forms.ModelForm):

    class Meta:
        model=staff
        fields=['staff_id','name','category','department','qualification'
                ,'joining_date','termination_date']
                
        '''widgets={
            'staff_id':forms.NumberInput(attrs={'class':'form-control',}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'qualification':forms.TextInput(attrs={'class':'form-control'}),
            'joining_date':forms.DateInput(attrs={'class':'form-control'})
            
        }'''    


class LeaveRequestForm(forms.ModelForm):

    class Meta:
        model=leave_request
        fields=('date','type','desc')





