from django.contrib import admin

from.models import Saved_items
from.models import Personal_info
from.models import Owner
from.models import Personal_info
from.models import Admin
# Register your models here.

admin.site.register(Saved_items)
admin.site.register(Personal_info)
admin.site.register(Owner)
admin.site.register(Admin)
