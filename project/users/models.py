from django.db import models

from django.contrib.auth.models import User

# Create your models here.


# class User (models.Model):
#     first_name = models.CharField(
#         max_length=100, default='new-user', null=True)
#     last_name = models.CharField(max_length=100, default='new-user', null=True)
#     username = models.CharField(max_length=100, default='new-user', null=True)
#     email = models.EmailField(null=True)
#     password = models.CharField(max_length=100, null=True)
#     confirm_password = models.CharField(
#         max_length=100, default='new-user', null=True)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.username

#     class Meta:
#         verbose_name = 'new-users'
