from django import forms
from sensorreg.models import DeviceStatus


class DeviceStatusForm(forms.ModelForm):

    class Meta:
        model = DeviceStatus
        fields = ['ID', 'IP', 'Port', "MacAddress", "AdministrativeRegion", "InstallationRoute", "InstallationLocation",
                  "GPSCoordinates", "InterlockDeviceInformation"]

