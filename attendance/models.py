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

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    STAFF_CHOICES=(
      (REGULAR_ACADEMIC,'Regular-Academic'),
      (REGULAR_NON_ACADEMIC,'Regular-NonAcademic'),
      (CONTRACT_STAFF_1_YR,'Contract Staff(1 year)'),
      (CONTRACT_STAFF_6_MNTH,'Contract Staff (6 months)'),

    )


    )