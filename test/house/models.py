from django.db import models

from . import views  

# Create your models here.


class House(models.Model):

    name = models.CharField
    price = models.IntegerField
    zip_code = models.IntegerField
    area = models.IntegerField
    floors = models.IntegerField
    bedrooms = models.IntegerField
    bathrooms = models.IntegerField
    view = models.IntegerField
    condition = models.IntegerField
    lat = models.IntegerField
    SQFT_Living = models.IntegerField
    SQFT_above = models.IntegerField
    SQFT_basement = models.IntegerField
    SQFT_lot15 = models.IntegerField
    SQFT_living15 = models.IntegerField
    yr_renovated = models.IntegerField


class Houses(models.Model):

    name = models.CharField
    price = models.IntegerField
    zip_code = models.IntegerField
    area = models.IntegerField
    floors = models.IntegerField
    bedrooms = models.IntegerField
    bathrooms = models.IntegerField
    view = models.IntegerField
    condition = models.IntegerField
    lat = models.IntegerField
    SQFT_Living = models.IntegerField
    SQFT_above = models.IntegerField
    SQFT_basement = models.IntegerField
    SQFT_lot15 = models.IntegerField
    SQFT_living15 = models.IntegerField
    yr_renovated = models.IntegerField

# class house_owner(models.Model):
