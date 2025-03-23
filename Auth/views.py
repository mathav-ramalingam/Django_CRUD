from django.shortcuts import render , redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


def Login(request):
    return render(request , 'login.html')


@api_view(["GET","POST"])
def Register(request):

    if request.method == 'POST':
        name = request.POST.get("username")
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        Register.objects.create(
            name = name,
            phone = phone,
            email = email,
            password = password,
            cpassword = cpassword,
        )

        return redirect('login')

    return redirect('register')