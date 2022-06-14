from django.contrib import admin
from django.contrib.auth.models import User
from .models import Type, profile

admin.site.register(Type)
admin.site.register(profile)
