from typing import Type
from django.db import models
class Userreg(models.Model):
    uname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    umail=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    trans=models.CharField(max_length=100,default='null')
    class Meta:
        db_table="newreg"

class Usertravel(models.Model):
    uname=models.CharField(max_length=100)
    umode=models.CharField(max_length=100)
    udate=models.DateField(max_length=100)
    utime=models.TimeField(max_length=100)
    ufrom=models.CharField(max_length=100)
    uto=models.CharField(max_length=100)
    class Meta:
        db_table="Travel"

class Bus(models.Model):

    Company=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    date=models.DateTimeField(blank=True)
    seats=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)
    utime=models.TimeField(max_length=100)
    class Meta:
        db_table="Bus"
    
    
    


  
