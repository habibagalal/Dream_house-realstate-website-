from django.db import models
from django.forms import CharField


# Create your models here.


class Personal_info (models.Model):
    name = models.CharField(max_length=100)


class Owner (models.Model):
    name = models.CharField(max_length=100)


class Admin(models.Model):
    name = models.CharField(max_length=100)
