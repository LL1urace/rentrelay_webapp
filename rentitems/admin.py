from django.contrib import admin

from rentitems.models import RentCategories, RentItems



# Register your models here.
admin.site.register(RentCategories)
admin.site.register(RentItems)