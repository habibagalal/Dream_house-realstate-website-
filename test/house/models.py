from django.db import models

# Create your models here.


class House(models.Model):
    name = models.CharField
    price = models.IntegerField


class Houses(models.Model):
    name = models.CharField
    price = models.IntegerField
