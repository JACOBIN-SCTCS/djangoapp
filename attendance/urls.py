from django.conf.urls import url
from django.urls import path
from . import views

app_name ="attendance"

urlpatterns =[


    path('dashboard/',views.dashboard,name='dash_board'),
    path('admin_user/', views.admin_dashboard, name='admin_user'),

    path('admin_user/register/',views.register,name='register'),
    path('admin_user/delete/', views.delete_user, name='delete_user'),
    path('admin_user/delete/<int:id>', views.delete, name='delete'),
    path('login/',views.login_user,name='login')

]



