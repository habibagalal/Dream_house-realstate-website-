from django.contrib.auth.models import User
from django.contrib import admin
from.models import House, Roles, Personal_Info, Profile

# Register your models here.
admin.site.register(House)
admin.site.register(Roles)
admin.site.register(Personal_Info)

admin.site.register(Profile)
