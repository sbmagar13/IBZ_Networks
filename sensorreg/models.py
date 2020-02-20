from django.db import models
#from django-macaddressimport MACAddressField
from django.core.validators import RegexValidator
#gps_validator = RegexValidator(r"^([-+]?)([\d]{1,2})(((\.)(\d+)(,)))(\s*)(([-+]?)([\d]{1,3})((\.)(\d+))?)$", "Not Valid MAC Address!")




class DeviceStatus(models.Model):
    DeviceID = models.IntegerField()
    IP = models.GenericIPAddressField(protocol='IPv4')
    Port = models.IntegerField()
    MacAddress =models.CharField(max_length=17)
    AdministrativeRegion = models.CharField(max_length=100,choices=[('gangwon-do', 'Gangwon-do'), ('gyeonggi-do', 'Gyeongii-do')], null=False)
    InstallationRoute = models.CharField(max_length=100, choices=[('a', 'A'), ('b', 'B')], null=False)
    InstallationLocation = models.CharField(max_length=100)
    GPSCoordinates = models.FloatField(max_length=20)  # models.ForeignKey(gps, on_delete=models.CASCADE)
    InterlockDeviceInformation = models.CharField(max_length=100)


class Operator(models.Model):
    PhoneNo = models.IntegerField()
    Password = models.CharField(max_length=100)
    MacAddress = models.IntegerField()#models.ForeignKey(macAddress, on_delete=models.CASCADE)
    ManagerName = models.CharField(max_length=100)
    ManagerPhoneNo = models.IntegerField()
    Department = models.CharField(max_length=100)
    FinalApprover = models.CharField(max_length=100)
