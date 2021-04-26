from django.forms import models
from .models import LeadSource, CustomerType, Location


class LeadSourceForm(models.ModelForm):
    class Meta:
        model = LeadSource
        fields = "__all__"


class CustomerTypeForm(models.ModelForm):
    class Meta:
        model = CustomerType
        fields = "__all__"


class LocationForm(models.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"
