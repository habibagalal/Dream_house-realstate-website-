
from django.db import models
from datetime import datetime  # create intial datetime value
from django.contrib.auth.models import User
from xml.dom.minidom import CharacterData
from django.forms import CharField

# Create your models here.


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
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = 'Property'  # update the name of the class
        ordering = ['title']  # ordering the objects

    def __str__(self):
        return self.title  # return the house name in the admin panel


class property_type(models.Model):
    type = models.ForeignKey(Property, on_delete=models.CASCADE)


class Roles(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Personal_Info(models.Model):
    email = models.EmailField(null=True)
    postalcode = models.IntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    address = models.TextField(null=True)
    phone = models.IntegerField()
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    h = models.CharField(max_length=100, null=True)
