from django.conf.urls import url
from django.urls import path
from . import views

app_name ="attendance"

urlpatterns =[

     # dashboard for a user
    path('dashboard/',views.dashboard,name='dash_board'),

    #dashboard for the admin
    path('admin_user/', views.admin_dashboard, name='admin_user'),


    # registering a new user
    path('admin_user/register/',views.register,name='register'),


    #delete page (may be changed)
    path('admin_user/delete/', views.delete_user, name='delete_user'),

    #url performs the delete functionality
    path('admin_user/delete/<int:id>', views.delete, name='delete'),

    # updating a user page (may be changed)
    path('admin_user/update/', views.update, name='update_user'),

    #url performs update
    path('admin_user/update/<int:pk>', views.Update_view.as_view(), name='update'),


    #logging a user in
    path('login/',views.login_user,name='login'),

    #page displaying table for the days absent
    path('dasboard/leaves',views.leaves,name='leaves'),


    path('dashboard/leave/id/<int:pk>',views.leave_request,name='leave_request')
]



