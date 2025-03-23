from django.db import models

# Create your models here.

class JobApplication(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    job_role = models.CharField(max_length=300)
    description = models.TextField()



class Joblist(models.Model):
    job_role = models.CharField(max_length=300)
    company_name = models.CharField(max_length=400)
    location = models.CharField(max_length=1000)
    required_skill = models.CharField(max_length=5000)
    qualification = models.CharField(max_length=500)