from django.shortcuts import render , redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *

# Create your views here.
def Home(request):
    return render(request , 'home.html')


@api_view(['GET','POST'])
def Job_List(request):

    if request.method == 'GET':
        joblist = Joblist.objects.all()
        print(joblist)

        return render(request , 'jobs.html' , {'job_list':joblist})


@api_view(["GET","POST"])
def apply_job(request):

    if request.method == 'POST':

        name = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        job_role = request.POST.get('jobrole')
        description = request.POST.get('description')

        JobApplication.objects.create(
            name = name,
            email = email,
            phone = phone,
            job_role = job_role,
            description = description,
        )

        return redirect('job_list')


    return redirect('job_list')

 
