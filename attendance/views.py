from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .forms import LoginForm , RegisterForm,LeaveRequestForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import leave
from .models import staff
from .models import rec ,dept
from .models import leave_request as lrequest
from django.urls import reverse
from django.views.generic.edit import UpdateView




#view for a user dashboard
def dashboard(request):

    current_user=request.user
    current_staff=staff.objects.get(user=current_user)

    department_hods = dept.objects.all()

    if department_hods.filter(emp=current_staff).exists():
        hod={ 'hod' : current_staff}
    else:
        hod=None



    return render(request,'attendance/user_dashboard.html',hod)




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
    if request.user.is_superuser:
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




                return redirect('attendance:admin_user')

        else:
            form=RegisterForm()
        return render(request,'attendance/register.html',{'form':form})
    else:
        return redirect('attendance:login')




#delete a user from the app (UI)
def delete_user(request):
    del_flag=1
    staff_list=staff.objects.all()
    return render(request,'attendance/list.html',{'staffs':staff_list , 'delflag':del_flag })




#performs the delete operation
def delete(request,id):
    userfield=User.objects.get(username=id)
    userfield.delete()
    return HttpResponseRedirect(reverse('attendance:delete_user'))




#updating the info of a user(UI0
def update(request):
    updateflag=1
    staff_list=staff.objects.all()
    return render(request,'attendance/list.html',{'staffs':staff_list , 'updateflag':updateflag })



#updating a user functionality
class Update_view(UpdateView):
    model = staff
    fields = ['staff_id','name','category','department','qualification'
                ,'joining_date','termination_date']

    template_name_suffix = '_update_form'



#method to list out the leaves taken by the current user
def leaves(request):

    recs=rec.objects.filter(status=0  , emp_id=staff.objects.get(staff_id=request.user.username))
    return render(request,'attendance/leaves_table_list.html',{'recs':recs})

def leave_request(request,pk):
    requested_leave = rec.objects.get(id=pk)

    if request.method=='POST':
        form=LeaveRequestForm(request.POST)
        if form.is_valid():

            leave_req=form.save(commit=False)

            leave_req.is_accepted=False
            leave_req.emp=requested_leave.emp_id
            leave_req.date=requested_leave.date
            leave_req.department=requested_leave.emp_id.department


            leave_req.save()


            return redirect('attendance:leaves')
    else:

        form=LeaveRequestForm(initial={'date':requested_leave.date})
    return render(request,'attendance/leave_request.html',{'form':form})




def available_leave_request(request):



    current_user=request.user
    current_staff=staff.objects.get(user=current_user)

    department_hods = dept.objects.all()

    if department_hods.filter(emp=current_staff).exists():

        leaverequests=lrequest.objects.filter(is_accepted=False,department=current_staff.department )
        return render(request, 'attendance/leave_requests_list.html',{'requests':leaverequests})

    else:
        return redirect('attendance:dash_board')









