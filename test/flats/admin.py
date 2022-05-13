from django.contrib.auth.models import User
from django.contrib import admin
from.models import Property, Roles, Personal_Info, Profile, Login

# Register your models here.
admin.site.register(Property)
admin.site.register(Roles)
admin.site.register(Personal_Info)
admin.site.register(Login)
admin.site.register(Profile)
