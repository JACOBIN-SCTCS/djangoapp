from django.conf.urls import url
from django.urls import path
from . import views

app_name ="attendance"

urlpatterns =[


    path('dashboard/',views.dashboard,name='dash_board'),
    path('register/',views.register,name='register')

]