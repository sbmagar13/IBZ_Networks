from django.contrib import admin
from sensors.models import *

# Register your models here.
admin.site.register(DeviceStatus)
admin.site.register(Operator)
admin.site.register(InterlockDevice)
admin.site.register(SensorData)
