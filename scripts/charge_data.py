from bledevices.models import BleDevice,BleNetwork, BleDeviceType, Data
import datetime
import random

tz = datetime.timezone.utc
year=2022
month=4
day_range=[1,2]
hour_range=[9,18]
value_range=[20,60]
DATA_QUANTITY = 10

def run():
    Data.objects.all().delete()
    for day in range(day_range[0],day_range[1]):
        for h in range(hour_range[0],hour_range[1]):
            for m in range(0,60,DATA_QUANTITY):
                for data_type in BleDeviceType.objects.all():
                    for sensor in data_type.bledevice_set.all():
                        d = Data(value=random.randrange(value_range[0],value_range[1]),
                        data_type=data_type,
                        sensor=sensor,
                        created_at=datetime.datetime(year=year,month=month,day=day,hour=h,minute=m,tzinfo=tz))
                        d.save()