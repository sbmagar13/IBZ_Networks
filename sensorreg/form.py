from django import forms
from sensorreg.models import DeviceStatus,Operator


class DeviceStatusForm(forms.ModelForm):
    class Meta:
        model = DeviceStatus
        fields = ['DeviceID', 'IP', 'Port', "MacAddress", "AdministrativeRegion", "InstallationRoute", "InstallationLocation",
                  "GPSCoordinates", "InterlockDeviceInformation"]

class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = ('PhoneNo', 'Password', 'MacAddress', 'ManagerName', 'ManagerPhoneNo', 'Department', 'FinalApprover')