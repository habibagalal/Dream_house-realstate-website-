from distutils.command.upload import upload
from django.db import models

from . import views

# Create your models here.


class House(models.Model):

    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='photos/%y/%m/%d', default='Hi')
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=3, default='Hi')
    condition = models.TextField(
        default='start type the condition of the House ')
    floors = models.IntegerField
    bedrooms = models.IntegerField
    bathrooms = models.IntegerField
    view = models.TextField()
    lat = models.IntegerField
    SQFT_Living = models.IntegerField
    SQFT_above = models.IntegerField
    SQFT_basement = models.IntegerField
    SQFT_lot15 = models.IntegerField
    SQFT_living15 = models.IntegerField
    yr_renovated = models.IntegerField
    zip_code = models.IntegerField


class Houses(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='photos/%y/%m/%d', default='Hi')
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=3, default='Hi')
    condition = models.TextField(
        default='start type the condition of the House ')
    floors = models.IntegerField
    bedrooms = models.IntegerField
    bathrooms = models.IntegerField
    view = models.TextField(default='Hi')
    lat = models.IntegerField
    SQFT_Living = models.IntegerField()
    SQFT_above = models.IntegerField()
    SQFT_basement = models.IntegerField()
    SQFT_lot15 = models.IntegerField()
    SQFT_living15 = models.IntegerField()
    yr_renovated = models.IntegerField()
    zip_code = models.IntegerField()
