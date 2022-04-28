from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.utils import timezone
MAC_REGEX = "^([0-9A-F]{2}:){5}([0-9A-Fa-f]{2})|([0-9A-F]{4}\\.[0-9A-F]{4}\\.[0-9A-F]{4})$"

# Create your models here.
class BleDevice(models.Model):
    identifier = models.CharField(max_length=200,validators=[MinLengthValidator(5, "Identifier must be greater than 4 characters")])
    friendly_name = models.CharField(max_length=200,validators=[MinLengthValidator(2, "Friendly name must be greater than 1 character")])
    mac = models.CharField(max_length=17,validators=[RegexValidator(regex=MAC_REGEX,message="Expected format is AA:BB:CC:DD:EE:FF")])
    device_type = models.ForeignKey('BleDeviceType', on_delete=models.CASCADE, null=False)
    network = models.ForeignKey('BleNetwork', on_delete=models.CASCADE, null=False)
    active = models.BooleanField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def toggle_active(self):
        self.active = not self.active
        self.save()
    
    def get_data(self):
        response=[]
        for data in self.data_set.all():
            datadict = {}
            if data.data_type.name == "TemperatureSensor":
                y_value = "Temperature"
            elif data.data_type.name == "HumiditySensor":
                y_value = "Humidity"
            datadict[self.friendly_name] = data.value
            datadict["time"] = data.created_at.strftime("%Y-%m-%d %H:%M:%S")
            response.append(datadict)
        
        return response

    def get_data_type(self):
        if self.device_type.name == "TemperatureSensor":
            return "Temperature"
        else:
            return "Humidity"
    def __str__(self):
        return self.identifier


class BleDeviceType(models.Model):
    name = models.CharField(max_length=50,validators=[MinLengthValidator(2, "Name must be greater than 1 character")])

    def __str__(self):
        return self.name

class Data(models.Model):
    value = models.FloatField()
    data_type = models.ForeignKey('BleDeviceType', on_delete=models.CASCADE, null=False)
    sensor = models.ForeignKey('BleDevice', on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}Data({})".format(self.data_type.name, self.value)

class BleNetwork(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    active = models.BooleanField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def toggle_active(self):
        self.active = not self.active
        for dev in self.bledevice_set.all():
            dev.active = self.active
            dev.save()
        self.save()
    
    def device_count(self):
        return self.bledevice_set.all().count()
    
    def is_fully_functional(self):
        if not self.active:
            return False
        for dev in self.bledevice_set.all():
            if dev.active == False:
                return False
        return True

    def __str__(self):
        return self.name

