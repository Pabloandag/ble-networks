from django.contrib import admin

from bledevices.models import BleDevice, BleDeviceType, BleNetwork, Data

# Register your models here.

admin.site.register(BleDevice)
admin.site.register(BleDeviceType)
admin.site.register(BleNetwork)
admin.site.register(Data)