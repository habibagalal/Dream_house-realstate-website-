
from django.db import models
from datetime import datetime  # create intial datetime value
from django.contrib.auth.models import User
from xml.dom.minidom import CharacterData
from django.forms import CharField
from users.models import profile


class property_type(models.Model):
    type = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.type


class Property(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='photos/%y/%m/%d', null=True)
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=3, null=True)

    condition = models.TextField(default='The condition is  ')

    floors = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    view = models.TextField(default='The view is ')
    lat = models.IntegerField()
    SQFT_Living = models.IntegerField()
    SQFT_above = models.IntegerField()
    SQFT_basement = models.IntegerField()
    SQFT_lot15 = models.IntegerField()
    SQFT_living15 = models.IntegerField()
    yr_renovated = models.IntegerField()
    zip_code = models.IntegerField()
    created = models.DateTimeField(default=datetime.now)
   # / user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    city = models.CharField(max_length=50, null=True)
    type = models.ForeignKey(
        property_type, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Property'  # update the name of the class
        ordering = ['title']  # ordering the objects

    def __str__(self):
        return self.title  # return the house name in the admin panel


class UploadedProb(models.Model):  # model for user to upload properites
    type = models.ForeignKey(
        property_type, on_delete=models.CASCADE, null=True)
    images = models.ImageField(upload_to='new_photos/%y/%m/%d', null=True)
    videos = models.FileField(upload_to='videos/%y/%m/%d', null=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    location = models.URLField()
    profile = models.OneToOneField(
        profile, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(datetime.now)
