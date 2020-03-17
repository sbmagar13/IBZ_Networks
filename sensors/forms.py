from django import forms
from django.forms import PasswordInput

from sensors.models import DeviceStatus, Operator, InterlockDevice, SettingsWindow, HistorySettings, in_out_Window, \
    SensorData


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
                  'Password': 'Password',
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


class In_Out_WindowForm(forms.ModelForm):
    class Meta:
        model = in_out_Window
        fields = '__all__'
        labels = {'Black_Ice_Appearance': 'Black Ice Appeareance',
                  'Black_Ice_Appearance_Operator': 'Black Ice Appearance Operator',
                  'Action_Status': 'Action Status',
                  'InterlockDevice_ID': 'Interlock Device ID',
                  'Action_Taken': 'Action Taken'
                  }


class OffsetLogForm(forms.Form):
    log_cycle = forms.ChoiceField(choices=[("1 day", "One Day"), ("2 Weeks", "Two Weeks")])


class AcclerometerOffsetForm(forms.ModelForm):
    class Meta:
        model = SensorData
        fields = ['Accelerometer_Xout', 'Accelerometer_Yout', 'Accelerometer_Zout']


class EarthQuakeOffsetForm(forms.Form):
    EarthQuake_Xout = forms.FloatField()
    EarthQuake_Yout = forms.FloatField()
    EarthQuake_Zout = forms.FloatField()


class TemperatureOffsetForm(forms.Form):
    OFFSET = forms.FloatField()


class CumulativePPTOffsetForm(forms.Form):
    Reset = forms.BooleanField(required=False)
