from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class employee(models.Model):

    REGULAR_ACADEMIC='RA'
    REGULAR_NON_ACADEMIC='RNA'
    CONTRACT_STAFF_1_YR ='C1'
    CONTRACT_STAFF_6_MNTH='C6'
    AD_HOC_STAFF='AS'
    PART_TIME_STAFF='PF'
    OFFICE_TRAINEE='OT'
    DEPT_TRAINEE='DT'
     

    def __unicode__(self):
        return unicode(self.user) 
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    STAFF_CHOICES=(
      (REGULAR_ACADEMIC,'Regular-Academic'),
      (REGULAR_NON_ACADEMIC,'Regular-NonAcademic'),
      (CONTRACT_STAFF_1_YR,'Contract Staff(1 year)'),
      (CONTRACT_STAFF_6_MNTH,'Contract Staff (6 months)'),
      (AD_HOC_STAFF,'Ad-Hoc Staff'),
      (PART_TIME_STAFF,'Part-time-staff'),
      (OFFICE_TRAINEE,'Office Trainee'),
      (DEPT_TRAINEE,'Department Trainee')
    )

    category=models.CharField(max_length=3,choices=STAFF_CHOICES,default=REGULAR_ACADEMIC)


