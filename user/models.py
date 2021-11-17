from django.db import models
#import DateTimeField
from datetime import datetime
from django.urls import reverse

class Agent(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    phone = models.CharField(max_length=20,null=False,blank=False)
    description = models.CharField(max_length=20,null=True,blank=True)
    email = models.CharField(max_length=20,null=True,blank=False)
    image = models.ImageField(null=True, blank=True)
    #created_at = models.DateTimeField(null=False, blank=True, editable=False)
    updated_at = models.DateTimeField(null=True,blank=True, editable=False)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class Landlord(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Listing(models.Model):

     agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING ,null=True, blank=False)
     title = models.CharField(max_length=500, null=True, blank=False)
     price = models.IntegerField(null=True)
     address =models.CharField(max_length=500, null=True, blank=False)
     city = models.CharField(max_length=500, null=True, blank=False)
     description = models.TextField(max_length=500, null=True, blank=True)
     bedrooms = models.IntegerField(null=True)
     bathrooms = models.DecimalField(null=True,max_digits=2, decimal_places=1)
     garage = models.IntegerField(null=True,default=0)
     sqft = models.IntegerField(null=True)

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     image = models.ImageField(null=True, blank=True)
     image2 = models.ImageField(null=True, blank=True)
     image3 = models.ImageField(null=True, blank=True)
     image4 = models.ImageField(null=True, blank=True)

     def __str__(self):
         return str(self.title)

     @property
     def imageURL(self):
         try:
             url = self.image.url
         except:
             url = ''
         return url


