from django.urls import path
from sensorreg import views

urlpatterns = [

    path('sensor/', views.sensor_form, name='sensor_insert'),  # get and post req. for insert operation
    path('envupdate/<int:sid>/', views.sensor_form, name='sensor_update'),  # get and post req. for update operation
    path('envdelete/<int:sid>/', views.sensor_delete, name='sensor_delete'),
    path('envlist/', views.sensor_list, name='sensor_list'),  # get req. to retrieve and display all records

    path('operator/', views.operator_form, name='operator_insert'),  # get and post req. for insert operation
    path('opupdate/<int:oid>/', views.operator_form, name='operator_update'),  # get and post req. for update operation
    path('opdelete/<int:oid>/', views.operator_delete, name='operator_delete'),
    path('oplist/', views.operator_list, name='operator_list')  # get req. to retrieve and display all records
]