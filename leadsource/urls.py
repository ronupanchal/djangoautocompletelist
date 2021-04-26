from django.urls import path
from . import views
app_name = 'leadsource'

urlpatterns =[
    path('', views.index, name='index'),
    path('lead/create/', views.LeadSourceView.as_view(), name='leadsource_create'),
    path('lead/list/', views.LeadSourceList.as_view(), name='leadsourcelist_list'),
    path('lead/update/<int:pk>', views.LeadSourceUpdateView.as_view(), name='leadsource_update'),
    path('lead/delete/<int:pk>', views.LeadSourceDeleteView.as_view(), name='leadsource_delete'),

    path('location/create/', views.LocationView.as_view(), name='location_create'),
    path('location/list/', views.LocationList.as_view(), name='location_list'),
    path('location/update/<int:pk>', views.LocationUpdateView.as_view(), name='location_update'),
    path('location/delete/<int:pk>', views.LocationDeleteView.as_view(), name='location_delete'),

    path('customertype/create/', views.CustomerTypeView.as_view(), name='customertype_create'),
    path('customertype/list/', views.CustomerTypeList.as_view(), name='customertype_list'),
    path('customertype/update/<int:pk>', views.CustomerTypeUpdateView.as_view(), name='customertype_update'),
    path('customertype/delete/<int:pk>', views.CustomerTypeDeleteView.as_view(), name='customertype_delete'),

    path('location-autocomplete', views.LocationAutocomplete.as_view(), name='location-autocomplete'),
    path('customertype-autocomplete', views.CustomerTypeAutocomplete.as_view(), name='customertype-autocomplete'),
    path('leadsource-autocomplete', views.LeadSourceAutocomplete.as_view(), name='leadsource-autocomplete'),


]