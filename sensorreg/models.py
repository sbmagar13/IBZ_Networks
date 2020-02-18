from django.db import models
from django.forms import ModelForm


class DeviceStatus(models.Model):
    ID = models.IntegerField()
    IP = models.GenericIPAddressField(protocol='IPv4')
    Port = models.IntegerField()
    MacAddress = models.CharField(max_length=100)
    AdministrativeRegion = models.CharField(max_length=100,choices=[('gangwon-do', 'Gangwon-do'), ('gyeonggi-do', 'Gyeongii-do')], null=False)
    InstallationRoute = models.CharField(max_length=100, choices=[('a', 'A'), ('b', 'B')], null=False)
    InstallationLocation = models.CharField(max_length=100)
    GPSCoordinates = models.FloatField()  # models.ForeignKey(gps, on_delete=models.CASCADE)
    InterlockDeviceInformation = models.CharField(max_length=100)
