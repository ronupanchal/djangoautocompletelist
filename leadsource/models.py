from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.

class LeadSource(models.Model):
    name = models.CharField(_("Source"), max_length=50, blank=True, null=True)
    url = models.URLField(_("Source URL"), max_length=200, blank=True, null=True)        
    thumbnail = models.ImageField(_("Thumbnail"), upload_to="thumbnails/", null= True, blank=True, default='thumbnails/1.jpg')
    logo = models.ImageField(_("Logo"), upload_to="logo/", null=True, blank=True, default='logo/1.jpg')

    class Meta:
        verbose_name = _("Lead Source")
        verbose_name_plural = _("Lead Sources")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("LeadSource_detail", kwargs={"pk": self.pk})

class CustomerType(models.Model):
    type = models.CharField(_("Customer Type"), max_length=50, 
        help_text='Family| Bachelor | Corporate | Individual...etc', blank=True, null=True)
    
    class Meta:
        verbose_name = _("Customer Type")
        verbose_name_plural = _("Customer Types")

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse("CustomerType_detail", kwargs={"pk": self.pk})

class Location(models.Model):
    name = models.CharField(_("Location Name"), max_length=150, blank=True, null=True)    
    pincode = models.CharField(_("Pin Code"), max_length=10, blank=True, null=True)    
    
    class Meta:
        ordering = ['-id']
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    def __str__(self):
        return self.name
        

    def get_absolute_url(self):
        return reverse("location_detail", kwargs={"pk": self.pk})
