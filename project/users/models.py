from django.db import models

from django.contrib.auth.models import User


class Type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


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


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    type = models.OneToOneField(Type, on_delete=models.CASCADE, null=True)
