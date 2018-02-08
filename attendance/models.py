from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone


designa=(
    ('H' ,'HOD'),
    ('P','Principal')
)


categories =(

    ('RA','Regular Academic'),
    ('RNA','Regular Non-Academic'),
    ('C1','Contract Staff (1 yr)'),
    ('C6','Contract Staff (6 month)'),
    ('AS','Ad-hoc Staff'),
    ('PF','Part time Staff'),
    ('OT','Office Trainee'),
    ('DT','Department Trainee'),
)

departments =(


    ('BT','BioTechnology'),
    ('CSE','Computer Science'),
    ('EC','Electronics and Communication'),
    ('MECH','Mechanical'),
    ('APPL' ,'Applied Science'),
    ('LIB','Library'),
    ('ADM','Administration'),
    ('OTH','Others'),
)




# 1 : CASUAL LEAVE
# 2: COMPENSATION LEAVE
# 3: EARNED LEAVE
# 4: HALF PAY LEAVE
# 5: LEAVE WITH ALLOWANCE
# 6: DUTY LEAVE



leave_type = (
    ((1,'CL'),(2,'ComL'),(3,'EL'),(4,'HPL'),(5,'LA'),(6,'DL'))
)





# table for storing maximum number of leaves that
# could be taken by a person

class staff_category(models.Model):

    def __str__(self):
        return self.category

    category=models.CharField(max_length=3,choices=categories ,default='RA')
    max_casual_leave=models.IntegerField()
    max_compensation_leave=models.IntegerField()
    max_earned_leave=models.IntegerField()
    max_half_pay_leave=models.IntegerField()
    max_leave_with_allowance=models.IntegerField()
    max_duty_leave=models.IntegerField()


# table for storing details of the staff

class staff(models.Model):

    def __str__(self):
         return str(self.staff_id)

    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE,default=None)
    staff_id=models.IntegerField(primary_key=True ,unique=True)
    name=models.CharField(max_length=30 ,default="employee")
    category=models.ForeignKey(staff_category,on_delete=None)
    department=models.CharField(max_length=5,choices=departments,default='OTH')
    qualification=models.CharField(max_length=30,blank=True)
    joining_date=models.DateField(default=None)
    termination_date=models.DateField(default=None,blank=True)


# table for storing hod's and principal ( people who have to approve leaves
class dept(models.Model):
    emp=models.ForeignKey(staff,on_delete=models.CASCADE)
    designation=models.CharField(choices=designa,max_length=5)


# table for storing leaves and working days taken by a person
class leave(models.Model):


    def __str__(self):
        return str(self.emp_id.staff_id)

    emp_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    present_days=models.IntegerField(default=0)
    casual_leave = models.IntegerField(default=0)
    compensation_leave = models.IntegerField(default=0)
    earned_leave= models.IntegerField(default=0)
    half_pay_leave = models.IntegerField(default=0)
    leave_allowance= models.IntegerField(default=0)
    duty_leave = models.IntegerField(default=0)


# table for storing data from biometric
class rec(models.Model):
    emp_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    status=models.BooleanField(default=1)
    time_in = models.DateTimeField(null=True)
    time_out = models.DateTimeField(null=True)


# table storing leave requests made
class leave_request(models.Model):



    emp=models.ForeignKey(staff,on_delete=models.CASCADE)
    department=models.CharField(max_length=5,choices=departments,default='OTH')
    date=models.DateField(default=timezone.now)
    type=models.IntegerField(choices=leave_type,default=2)
    desc=models.TextField(max_length=500,default="")
    is_accepted=models.BooleanField(default=0)







