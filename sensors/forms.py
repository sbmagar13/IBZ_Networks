from django import forms
from django.forms import PasswordInput

from sensors.models import DeviceStatus, Operator, InterlockDevice, SettingsWindow, HistorySettings


class DeviceStatusForm(forms.ModelForm):
    class Meta:
        model = DeviceStatus
        fields = '__all__'


class InterlockDeviceForm(forms.ModelForm):
    class Meta:
        model = InterlockDevice
        fields = ['Device_ID', 'IP', 'Port', 'Device_Type', 'Remarks']


class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = ['PhoneNo', 'Password', 'confirmPassword', 'MacAddress', 'ManagerName', 'ManagerPhoneNo', 'Department',
                  'FinalApprover']
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
