from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from .validators import validate_MAC
from multiselectfield import MultiSelectField
from phone_field import PhoneField


class DeviceStatus(models.Model):
    DeviceID = models.IntegerField(unique=True)
    IP = models.GenericIPAddressField(protocol='IPv4', default='0.0.0.0')
    Port = models.IntegerField(default=23000)
    MacAddress = models.CharField(validators=[validate_MAC], max_length=20, default='aa:bb:cc:dd:ee:ff')
    AdministrativeRegion = models.CharField(max_length=100,
                                            choices=[('gangwon-do', 'Gangwon-do'), ('gyeonggi-do', 'Gyeongii-do')],
                                            null=False)
    InstallationRoute = models.CharField(max_length=100, choices=[('a', 'A'), ('b', 'B')], null=False)
    InstallationLocation = models.CharField(max_length=100)
    # GPSCoordinates = models.CharField(validators=[validate_GPS], max_length=100,
    #                                   default='10.141932, 10.371094')
    Long = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    Lat = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    InterlockDeviceID1 = models.CharField(max_length=100, default="None")
    InterlockDeviceID2 = models.CharField(max_length=100, default="None")
    InterlockDeviceID3 = models.CharField(max_length=100, default="None")
    InterlockDeviceID4 = models.CharField(max_length=100, default="None")

    def save(self, *args, **kwargs):
        self.DeviceID
        return super(DeviceStatus, self).save(*args, **kwargs)


class InterlockDevice(models.Model):
    Device_ID = models.IntegerField(unique=True)
    IP = models.GenericIPAddressField(protocol='IPv4', default='0.0.0.0')
    Port = models.IntegerField(default=23000)
    Device_Type = models.CharField(max_length=100,
                                   choices=[('Device of Sprinkler', 'Device of Sprinkler'), ('CCTV', 'CCTV'),
                                            ('Electronic Board', 'Electronic Board'),
                                            ('Disaster Broadcast', 'Disaster Broadcast')], null=False)
    Remarks = models.CharField(max_length=100, default="None")

    def save(self, *args, **kwargs):
        if self.Device_Type == "Device of Sprinkler":
            self.Device_ID = int('10' + str(self.Device_ID))
        elif self.Device_Type == 'CCTV':
            self.Device_ID = int('20' + str(self.Device_ID))
        elif self.Device_Type == 'Electronic Board':
            self.Device_ID = int('30' + str(self.Device_ID))
        else:
            self.Device_ID = int('40' + str(self.Device_ID))
        return super(InterlockDevice, self).save(*args, **kwargs)


class Operator(models.Model):
    PhoneNo = models.IntegerField()
    Password = models.CharField(validators=[MinLengthValidator(10)], max_length=100)
    confirmPassword = models.CharField(max_length=100)
    MacAddress = models.CharField(validators=[validate_MAC], max_length=20,
                                  default='aa:bb:cc:dd:ee:ff')
    ManagerName = models.CharField(max_length=100)
    ManagerPhoneNo = PhoneField(blank=True)
    Department = models.CharField(max_length=100)
    FinalApprover = models.CharField('Final Approver', max_length=100, null=False)

    def clean(self):
        if self.Password != self.confirmPassword:
            raise ValidationError('Passwords are not equal')
        password_validation.validate_password(self.Password, None)
        return self.Password


class SettingsWindow(models.Model):
    Esensor_item = (
        ('Administrative_District', 'Administrative_District'),
        ('Route_Name', 'Route_Name'),
        ('Installation_Location', 'Installation_Location'),
        ('Air_Temp', 'Air_Temp'),
        ('Ground_Temp', 'Ground_Temp'),
        ('Humidity', 'Humidity'),
        ('Atmospheric_Pressure', 'Atmospheric_Pressure'),
        ('Accumulated_Precipitation', 'Accumulated_Precipitation'),
        ('Dust_Concentration', 'Dust_Concentration'),
        ('Radiation_Illumination', 'Radiation_Illumination'),
        ('Solar_Radiation', 'Solar_Radiation'),
        ('Noise_level', 'Noise_level'),
        ('Earthquakes', 'Earthquakes'),
        ('Accelerometer_X:Y:Z', 'Accelerometer_X:Y:Z'),
        ('GPS_coordinates', 'GPS_coordinates'),
        ('Measuremeent_time', 'Measurement_time'),
    )
    Select_Esensor_item = MultiSelectField(choices=Esensor_item)


class HistorySettings(models.Model):
    Item_list = (
        ('Air_Temp', 'Air_Temp'),
        ('Ground_Temp', 'Ground_Temp'),
        ('Humidity', 'Humidity'),
        ('Atmospheric_Pressure', 'Atmospheric_Pressure'),
        ('Accumulated_Precipitation', 'Accumulated_Precipitation'),
        ('Dust_Concentration', 'Dust_Concentration'),
        ('Radiation_Illumination', 'Radiation_Illumination'),
        ('Solar_Radiation', 'Solar_Radiation'),
        ('Noise_Level', 'Noise_Level'),
        ('Earthquakes', 'Earthquakes'),
        ('Accelerometer_X:Y:Z', 'Accelerometer_X:Y:Z'),
        ('GPS_coordinates', 'GPS_coordinates'),
        ('Measurement_time', 'Measurement_time'),
    )

    Graph = (
        ('Line_graph', 'Line_graph'),
        ('Bar_graph', 'Bar_graph'),
        ('Scatter_graph', 'Scatter_graph'),
    )

    Item_List = MultiSelectField(choices= Item_list)
    Graph_Setting = MultiSelectField(choices=Graph)
    Save = models.CharField(max_length=100, choices=[('6_months', '6_months'), ('1_year', '1_year')])
    Delete = models.CharField(max_length=100, choices=[('6_months', '6_months'), ('1_year', '1_year')])
    Cycle_time = models.CharField(max_length=100, choices=[('6_months', '6_months'), ('1_year', '1_year')])


class SensorData(models.Model):
    Did = models.IntegerField()
    MAC_Address = models.CharField(max_length=8)
    Date = models.DateField()
    Time = models.TimeField()
    WeekDay = models.IntegerField()
    Air_Temperature = models.FloatField()
    Humidity = models.FloatField()
    Air_Pressure = models.FloatField()
    Accumulated_PPT = models.FloatField()
    Dust_Concentration = models.FloatField()
    Radiation_Illuminance = models.FloatField()
    Solar_Radiation = models.FloatField()
    RoadSurface_Temperature = models.FloatField()
    Noise_Level = models.IntegerField()
    Accelerometer_Xout = models.FloatField()
    Accelerometer_Yout = models.FloatField()
    Accelerometer_Zout = models.FloatField()
    GPS_Location_N = models.FloatField()
    GPS_Location_E = models.FloatField()


# classoperator(models.Model):
#     PhoneNo = models.CharField(validators=[MinLengthValidator(10)], max_length=20)
#     password = models.CharField(validators=[MinLengthValidator(10)],max_length=100)
#     confirmPassword = models.CharField(max_length=100)
#     MacAddress = models.CharField(validators=[validate_MAC], max_length=100, default='AA:BB:CC:DD:EE:FF')
#     ManagerName = models.CharField(max_length=100)
#     ManagerPhoneNo = models.CharField(validators=[MinLengthValidator(10)], max_length=20)
#     Department = models.CharField(max_length=100)
#     FinalApprover = models.CharField(max_length=100)
#
#     def clean(self):
#         if self.password != self.confirmPassword:
#             raise ValidationError('Passwords are not equal')
#         password_validation.validate_password(self.password, None)
#         return self.password
#
# def __str__(self): return self.PhoneNo, self.password, self.confirmPassword, self.MacAddress, self.ManagerName,
# self.ManagerPhoneNo, self.Department, self.FinalApprover