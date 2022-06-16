

# Register your models here.
from django.contrib.auth.models import User
from django.contrib import admin
from.models import Property, property_type, UploadedProb

# Register your models here.
admin.site.register(Property)
admin.site.register(property_type)
admin.site.register(UploadedProb)
