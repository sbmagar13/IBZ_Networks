from django import forms
from django.forms import PasswordInput

from sensors.models import DeviceStatus, Operator, InterlockDevice, SettingsWindow, HistorySettings


class DeviceStatusForm(forms.ModelForm):
    class Meta:
        model = DeviceStatus
        fields = '__all__'
        labels = {
            'DeviceID': 'Device ID',
            'IP': 'IP Address',
            'Port': 'Port',
            'MacAddress': 'Mac Address',
            'AdministrativeRegion': 'Administrative Region',
            'InstallationRoute': 'Installation Route',
            'Long': 'Longitude Value',
            'Lat': 'Lattitude Value',
            'InterlockDeviceID1': 'Interlocked Device ID1',
            'InterlockDeviceID2': 'Interlocked Device ID2',
            'InterlockDeviceID3': 'Interlocked Device ID3',
            'InterlockDeviceID4': 'Interlocked Device ID4',
        }


class InterlockDeviceForm(forms.ModelForm):
    class Meta:
        model = InterlockDevice
        fields = ['Device_ID', 'IP', 'Port', 'Device_Type', 'Remarks']
        labels = {'Device_ID': 'Device ID',
                  'IP': 'IP Address',
                  'Port': 'Port',
                  'Device_Type': 'Device Type',
                  'Remarks': 'Remarks',
                  }


class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = ['PhoneNo', 'Password', 'confirmPassword', 'MacAddress', 'ManagerName', 'ManagerPhoneNo', 'Department',
                  'FinalApprover']
        labels = {'PhoneNo': 'Phone ID No.',
                  'Password': 'New Password',
                  'confirmPassword': 'Confirm Password',
                  'MacAddress': 'MAC Address',
                  'ManagerName': 'Manager Name',
                  'ManagerPhoneNo': 'Manager Phone No.',
                  'Department': 'Department',
                  'FinalApprover': 'Final Approver Key',
                  }
        widgets = {
            'Password': PasswordInput(),
            'confirmPassword': PasswordInput(),
        }


class SettingsWindowForm(forms.ModelForm):
    class Meta:
        model = SettingsWindow
        fields = '__all__'


class ApproverForm(forms.Form):
    approver_key = forms.CharField(required=True, label='Approver Key')


class HistorySettingsForm(forms.ModelForm):
    class Meta:
        model = HistorySettings
        fields = '__all__'
