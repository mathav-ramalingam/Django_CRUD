from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Joblist)
class AdminJoblist(admin.ModelAdmin):
    list_display = ['job_role','company_name','location','required_skill','qualification']

@admin.register(JobApplication)
class AdminJobApplication(admin.ModelAdmin):
    list_display = ['name','email','phone','job_role','description']