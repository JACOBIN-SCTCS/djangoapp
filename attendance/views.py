from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from  .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import redirect ,get_object_or_404
from .models import leave,rec
from django.views.generic import View
from .models import staff
from django.urls import reverse
# Create your views here.


#view for a user dashboard
def dashboard(request):
        return render(request,'attendance/user_dashboard.html')


#view for the admin dashboard
def admin_dashboard(request):
        if request.user.is_superuser:
            return render(request,'attendance/admin_dashboard.html')
        else:
            return redirect('attendance:login')



#login for a user
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
                if not user.is_superuser:
                    return redirect('attendance:dash_board')
                else:
                    return redirect('attendance:admin_user')
    else:
        form=LoginForm()
    return render(request,'attendance/login.html',{'form':form})




#register a user ( a facility for a superuser (admin))
def  register(request):

        if request.method=='POST':
            form=RegisterForm(request.POST)
            if form.is_valid():
                staff=form.save(commit=False)
                id = form.cleaned_data['staff_id']
                user = User.objects.create_user(username=str(form.cleaned_data['staff_id'])
                                                     , password='user'+str(form.cleaned_data['staff_id']))

                staff.user=user
                staff.save()

                leave_rec=leave(emp_id=staff)
                leave_rec.save()




                return redirect('attendance:dash_board')

        else:
            form=RegisterForm()
        return render(request,'attendance/register.html',{'form':form})





#delete a user from the app
def delete_user(request):
    staff_list=staff.objects.all()
    return render(request,'attendance/delete.html',{'staffs':staff_list})


def delete(request,id):
    userfield=User.objects.get(username=id)
    userfield.delete()
    return HttpResponseRedirect(reverse('attendance:delete_user'))