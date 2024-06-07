from django.db import models


# Create your models here.

class bigdb(models.Model):
    CatName = models.CharField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)
    img = models.ImageField(upload_to='Product Images',null=True,blank=True)

class Productdb(models.Model):
    category_name = models.CharField(max_length=100,null=True,blank=True)
    product_name = models.CharField(max_length=100,null=True,blank=True)
    Des = models.CharField(max_length=100,null=True,blank=True)
    pp = models.IntegerField(null=True,blank=True)
    img = models.ImageField(upload_to='Category Images',null=True,blank=True)
