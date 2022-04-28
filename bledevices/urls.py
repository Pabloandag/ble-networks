from django.urls import path
from . import views

app_name = 'bledevices'
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('device/', views.BleDeviceListView.as_view(), name='all'),
    path('device/<int:pk>',views.BleDeviceDetailView.as_view(), name='bledevice_detail'),
    path('device/create/', views.BleDeviceCreateView.as_view(), name='bledevice_create'),
    path('device/<int:pk>/update/', views.BleDeviceUpdateView.as_view(), name='bledevice_update'),
    path('device/<int:pk>/delete/', views.BleDeviceDeleteView.as_view(), name='bledevice_delete'),
    path('device/<int:pk>/toggle/', views.BleDeviceToggleView.as_view(), name='bledevice_toggle'),
    path('network/', views.BleNetworkListView.as_view(), name='network_all'),
    path('network/<int:pk>',views.BleNetworkDetailView.as_view(), name='network_detail'),
    path('network/create/', views.BleNetworkCreateView.as_view(), name='network_create')
    #path('network/<int:pk>/delete/', views.BleNetworkDeleteView.as_view(), name='network_delete')
]