from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.base import TemplateView

from bledevices.models import BleDevice, BleDeviceType, BleNetwork

# Create your views here.
class BleDeviceListView(ListView):
    model = BleDevice

class BleDeviceDetailView(DetailView):
    model = BleDevice

class BleDeviceCreateView(CreateView):
    model = BleDevice
    fields = ['identifier', 'friendly_name', 'mac', 'device_type','network','active']
    success_url = reverse_lazy('bledevices:all')

class BleDeviceUpdateView(UpdateView):
    model = BleDevice
    fields = ['identifier', 'friendly_name', 'mac', 'device_type','network','active']
    success_url = reverse_lazy('bledevices:all')

@method_decorator(csrf_exempt, name='dispatch')
class BleDeviceToggleView(UpdateView):
    def post(self,request,pk):
        d = get_object_or_404(BleDevice,id=pk)
        print(d)
        d.toggle_active()
        return HttpResponse()
        

class BleDeviceDeleteView(DeleteView):
    model = BleDevice
    success_url = reverse_lazy('bledevices:all')


class BleDeviceTypeListView(ListView):
    model = BleDeviceType

class BleDeviceTypeDetailView(DetailView):
    model = BleDeviceType

class BleDeviceTypeCreateView(CreateView):
    model = BleDeviceType
    fields = '__all__'
class BleDeviceTypeUpdateView(UpdateView):
    model = BleDeviceType


class BleNetworkListView(ListView):
    model = BleNetwork

class BleNetworkCreateView(CreateView):
    model = BleNetwork
    fields = ['name', 'location', 'active']
    success_url = reverse_lazy('bledevices:home')

class BleNetworkDetailView(DetailView):
    model = BleNetwork

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in network devices list        
        context['connected_devices'] = list(kwargs.get('object').bledevice_set.all())
        return context

class HomeView(TemplateView):
    template_name = 'bledevices/home.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in devices data
        temp_dev_type = get_object_or_404(BleDeviceType,name='TemperatureSensor')
        temp_data = []
        temp_dev_names = []
        for dev in temp_dev_type.bledevice_set.all():
            temp_data = temp_data + dev.get_data()
            temp_dev_names.append(dev.friendly_name)
        hum_dev_type = get_object_or_404(BleDeviceType,name='HumiditySensor')
        hum_data = []
        hum_dev_names = []
        for dev in hum_dev_type.bledevice_set.all():
            hum_data = hum_data + dev.get_data()
            hum_dev_names.append(dev.friendly_name)
        
        context['temp_data'] = temp_data
        context['temp_dev_names'] = temp_dev_names
        context['hum_data'] = hum_data
        context['hum_dev_names'] = hum_dev_names
        context['dev_count'] = BleDevice.objects.all().count()
        context['network_count'] = BleNetwork.objects.all().count()
        context['inactive_dev_count'] = BleDevice.objects.filter(active=False).count()
        nff_networks = 0
        for network in BleNetwork.objects.all():
            if not network.is_fully_functional():
                nff_networks += 1
        context['not_fully_functional_network_count'] = nff_networks
        return context
