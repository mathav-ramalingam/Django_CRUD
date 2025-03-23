from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=300)
    password = models.CharField(max_length=300)


