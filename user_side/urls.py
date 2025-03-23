from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('job/',Job_List, name='job_list'),
    path('apply/',apply_job, name='apply_job'),
]

