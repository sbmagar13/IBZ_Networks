from django.db import models
from .validator import validate_MAC, validate_GPS
#from django-macaddress import MACAddressField
from django.core.validators import RegexValidator
#gps_validator = RegexValidator(r"^([-+]?)([\d]{1,2})(((\.)(\d+)(,)))(\s*)(([-+]?)([\d]{1,3})((\.)(\d+))?)$", "Not Valid GPS Coordinate!")

#'/^(([a-fA-F0-9]{2}-){5}[a-fA-F0-9]{2}|([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}|([0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4})?$/'




class DeviceStatus(models.Model):
    DeviceID = models.IntegerField()
    IP = models.GenericIPAddressField(protocol='IPv4')
    Port = models.IntegerField()
    MacAddress =models.CharField(validators=[validate_MAC], max_length=20)
    AdministrativeRegion = models.CharField(max_length=100,choices=[('gangwon-do', 'Gangwon-do'), ('gyeonggi-do', 'Gyeongii-do')], null=False)
    InstallationRoute = models.CharField(max_length=100, choices=[('a', 'A'), ('b', 'B')], null=False)
    InstallationLocation = models.CharField(max_length=100)
    GPSCoordinates = models.CharField(validators=[validate_GPS], max_length=100)  # models.ForeignKey(gps, on_delete=models.CASCADE)
    InterlockDeviceInformation = models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        if self.AdministrativeRegion == "gangwon-do":
            self.DeviceID = int('10' + str(self.DeviceID))
        else:
            self.DeviceID = int('20' + str(self.DeviceID))
        return super(DeviceStatus, self).save(*args, **kwargs)

class Operator(models.Model):
    PhoneNo = models.IntegerField()
    Password = models.CharField(max_length=100)
    MacAddress = models.IntegerField()#models.ForeignKey(macAddress, on_delete=models.CASCADE)
    ManagerName = models.CharField(max_length=100)
    ManagerPhoneNo = models.IntegerField()
    Department = models.CharField(max_length=100)
    FinalApprover = models.CharField(max_length=100)
