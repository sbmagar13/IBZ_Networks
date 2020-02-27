from django.db import models
from .validator import validate_MAC, validate_GPS


class DeviceStatus(models.Model):
    DeviceID = models.IntegerField(unique=True)
    IP = models.GenericIPAddressField(protocol='IPv4', default='0.0.0.0')
    Port = models.IntegerField(default=23000)
    MacAddress =models.CharField(validators=[validate_MAC], max_length=20, default='aa:bb:cc:dd:ee:ff')
    AdministrativeRegion = models.CharField(max_length=100,choices=[('gangwon-do', 'Gangwon-do'), ('gyeonggi-do', 'Gyeongii-do')], null=False)
    InstallationRoute = models.CharField(max_length=100, choices=[('a', 'A'), ('b', 'B')], null=False)
    InstallationLocation = models.CharField(max_length=100)
    GPSCoordinates = models.CharField(validators=[validate_GPS], max_length=100, default='10.141932, 10.371094')  # models.ForeignKey(gps, on_delete=models.CASCADE)
    InterlockDeviceInformation = models.CharField(max_length=100, default="NULL")
    def save(self, *args, **kwargs):
        if self.AdministrativeRegion == "gangwon-do":
            self.DeviceID = int('10' + str(self.DeviceID))
        else:
            self.DeviceID = int('20' + str(self.DeviceID))
        return super(DeviceStatus, self).save(*args, **kwargs)

class InterlockDevice(models.Model):
    Device_ID = models.IntegerField(unique=True)
    IP = models.GenericIPAddressField(protocol='IPv4', default='0.0.0.0')
    Port = models.IntegerField(default=23000)
    Device_Type = models.CharField(max_length=100, choices=[('a', 'Device of Sprinkler'), ('b', 'CCTV'), ('c', 'Electronic Board'), ('d', 'Disaster Broadcast')], null=False)
    Remarks = models.CharField(max_length=100, default="NULL")

class Operator(models.Model):
    PhoneNo = models.IntegerField()
    Password = models.CharField(max_length=100)
    MacAddress = models.IntegerField()#models.ForeignKey(macAddress, on_delete=models.CASCADE)
    ManagerName = models.CharField(max_length=100)
    ManagerPhoneNo = models.IntegerField()
    Department = models.CharField(max_length=100)
    FinalApprover = models.CharField(max_length=100)
