from django.contrib import admin
from .models import staff_category,staff,leave,rec,dept,leave_request

# Register your models here.
admin.site.register(staff_category)
admin.site.register(staff)
admin.site.register(leave)
admin.site.register(rec)

admin.site.register(dept)
admin.site.register(leave_request)




