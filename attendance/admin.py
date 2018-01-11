from django.contrib import admin
from .models import staff_category,staff,leave

# Register your models here.
admin.site.register(staff_category)
admin.site.register(staff)
admin.site.register(leave)