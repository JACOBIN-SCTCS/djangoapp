from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from  .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import leave,rec
from django.views.generic import View

# Create your views here.



def dashboard(request):
    return render(request,'attendance/user_form.html')


def login_user(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user_obj=form.cleaned_data
            name=user_obj['username']
            password=user_obj['password']
            user=authenticate(username=name,password=password)
            if user is not None:
                login(request,user)
                return redirect('attendance:dash_board')
    else:
        form=LoginForm()
    return render(request,'attendance/login.html',{'form':form})





def  register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            staff=form.save(commit=False)
            user=User.objects.create_user(username=str(form.cleaned_data['staff_id'])
                                         , password=form.cleaned_data['staff_id'])
            id=form.cleaned_data['staff_id']
            staff.user=user
            staff.save()

            leave_rec=leave(emp_id=staff)
            leave_rec.save()



            return redirect('attendance:dash_board')

    else:
        form=RegisterForm()
    return render(request,'attendance/register.html',{'form':form})



