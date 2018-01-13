from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



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

leave_type = (
    ((0,'A'),(1,'P'),(2,'CL'),(3,'ComL'),(4,'EL'),(5,'HPL'),(6,'LA'),(7,'DL'))
)



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


class staff(models.Model):

    def __str__(self):
         return str(self.staff_id)

    user=models.OneToOneField(User,on_delete=models.CASCADE ,null=False,default=None)
    staff_id=models.IntegerField(primary_key=True ,unique=True)
    name=models.CharField(max_length=30 ,default="employee")
    category=models.ForeignKey(staff_category,on_delete=None)
    department=models.CharField(max_length=5,choices=departments,default='OTH')
    qualification=models.CharField(max_length=30,blank=True)
    joining_date=models.DateField(default=None)
    termination_date=models.DateField(default=None,blank=True)



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



class rec(models.Model):
    emp_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now())
    status=models.IntegerField(default='-1',choices=leave_type)
    time_in = models.DateTimeField(null=True)
    time_out = models.DateTimeField(null=True)

