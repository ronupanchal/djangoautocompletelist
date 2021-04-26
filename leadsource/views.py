from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import LeadSourceForm, LocationForm, CustomerTypeForm
from .models import LeadSource, Location, CustomerType
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from dal import autocomplete

# Create your views here.

def index(request):
    title ="Dashboard"    
    return render(request, 'index.html')

#--------------LeadSource-----
class LeadSourceView(View):
    
    def get(self, request):
        form = LeadSourceForm()
        return render(request, 'leadsource_create.html', {'form':form})

    def post(self, request):
        if request.method == 'POST':
            form = LeadSourceForm(request.POST, request.FILES)
            if form.is_valid():
                print(form.cleaned_data['name'])
                print(form.cleaned_data['url'])
                print(form)
                form.save()
                return redirect('leadsource:leadsourcelist_list')

class LeadSourceList(ListView):
    model = LeadSource
    template_name = 'leadsource.html'
    context_object_name = 'leadsources'


class LeadSourceUpdateView(UpdateView):
    # specify the model you want to use
    model = LeadSource
    template_name = 'leadsource_form.html'
    # specify the fields
    fields = [
        "name", "url", "thumbnail", "logo"
    ]
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = reverse_lazy('leadsource:leadsourcelist_list')


class LeadSourceDeleteView(DeleteView):
    # specify the model you want to use
    model = LeadSource
    template_name = 'leadsource_confirm_delete.html'
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = reverse_lazy('leadsource:leadsourcelist_list')
#--------------End LeadSource-----

#--------------Location-----
class LocationView(View):
    
    def get(self, request):
        form = LocationForm()
        return render(request, 'location_create.html', {'form':form})

    def post(self, request):
        if request.method == 'POST':
            form = LocationForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data['name'])
                print(form)
                form.save()
                return redirect('leadsource:location_list')

class LocationList(ListView):
    model = Location
    template_name = 'location.html'
    context_object_name = 'locations'


class LocationUpdateView(UpdateView):
    # specify the model you want to use
    model = Location
    template_name = 'location_form.html'
    # specify the fields
    fields = [
        "name"
    ]
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = reverse_lazy('leadsource:location_list')


class LocationDeleteView(DeleteView):
    # specify the model you want to use
    model = Location
    template_name = 'location_confirm_delete.html'
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = reverse_lazy('leadsource:location_list')
#--------------End Location-----
#--------------Customer Type-----
class CustomerTypeView(View):
    
    def get(self, request):
        form = CustomerTypeForm()
        return render(request, 'customertype_create.html', {'form':form})

    def post(self, request):
        if request.method == 'POST':
            form = CustomerTypeForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data['type'])
                print(form)
                form.save()
                return redirect('leadsource:customertype_list')

class CustomerTypeList(ListView):
    model = CustomerType
    template_name = 'customertype.html'
    context_object_name = 'customertypes'


class CustomerTypeUpdateView(UpdateView):

    model = CustomerType
    template_name = 'customertype_form.html'

    fields = [
        "type"
    ]

    success_url = reverse_lazy('leadsource:customertype_list')


class CustomerTypeDeleteView(DeleteView):
    model = CustomerType
    template_name = 'customertype_confirm_delete.html'

    success_url = reverse_lazy('leadsource:customertype_list')
#--------------End Customer Type-----
class LocationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Location.objects.none()

        qs = Location.objects.all()
        print(qs)
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class CustomerTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return CustomerType.objects.none()

        qs = CustomerType.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class LeadSourceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return LeadSource.objects.none()

        qs = LeadSource.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs