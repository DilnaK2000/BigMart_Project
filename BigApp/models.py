from django.db import models

# Create your models here.
class biginput_db(models.Model):
    Your_Name = models.CharField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=100,null=True,blank=True)
    Message = models.CharField(max_length=100,null=True,blank=True)

class logindb(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    Confirm_password = models.CharField(max_length=100,null=True,blank=True)

class cartdb(models.Model):
    usename = models.CharField(max_length=100,null=True,blank=True)
    proname = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    quantity = models.IntegerField(null=True, blank=True)

