from django.urls import path
from sensors import views

urlpatterns = [
    path('home/', views.index, name=''),

    path('sensor/', views.sensor_form, name='sensor_insert'),  # get and post req. for insert operation
    path('envupdate/<int:sid>/', views.sensor_form, name='sensor_update'),  # get and post req. for update operation
    path('envdelete/<int:sid>/', views.sensor_delete, name='sensor_delete'),
    path('envlist/', views.sensor_list, name='sensor_list'),  # get req. to retrieve and display all records

    path('interlock/', views.interlockdevice_form, name='interlock_insert'),  # get and post req. for insert operation
    path('interlockupdate/<int:eid>/', views.interlockdevice_form, name='interlock_update'),
    path('interlockdelete/<int:eid>/', views.interlockdevice_delete, name='interlock_delete'),
    path('interlocklist/', views.interlock_list, name='interlock_list'),  # get req. to retrieve and display all records

    path('operator/', views.operator_form, name='operator_insert'),  # get and post req. for insert operation
    path('opupdate/<int:oid>/', views.operator_form, name='operator_update'),  # get and post req. for update operation
    path('opdelete/<int:oid>/', views.operator_delete, name='operator_delete'),
    path('oplist/', views.operator_list, name='operator_list'),  # get req. to retrieve and display all records

    path('displaySettings/', views.settings_window, name='display_settings'),
    path('historySettings/', views.history_settings, name='history_settings'),
    path('offsetSettings', views.offset_settings, name='offset_settings'),

    path('', views.sensor_data, name='sensor_data'),

    path('sensor/search/', views.sensorsearch_view, name='sensor_search'),
    path('operator/search/', views.operatorsearch_view, name='operator_search'),
    path('interlock/search', views.interlocksearch_view, name='interlock_search'),

    path('in-out/', views.in_out_window, name='in_out'),
    path('map/', views.map, name='map'),

    path('seismograph/', views.SeismographOffset, name='seismograph'),
    path('tempoffset/', views.TemperatureOffset, name='tempoffset'),
    path('cumulitiveppt/', views.CumulativePPTOffset, name='CumulativePPTOffset'),
    path('log/', views.Log, name='logoffset'),
]
