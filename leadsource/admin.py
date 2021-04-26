from django.contrib import admin
from .models import LeadSource, CustomerType, Location

# Register your models here.


admin.site.register(LeadSource)
admin.site.register(CustomerType)
admin.site.register(Location)
