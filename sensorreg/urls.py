from django.urls import path
from sensorreg import views

urlpatterns = [

    path('sensor/', views.sensor_form, name='sensor_insert'),  # get and post req. for insert operation
    path('<int:id>/', views.sensor_form, name='sensor_update'),  # get and post req. for update operation
    path('delete/<int:id>/', views.sensor_delete, name='sensor_delete'),
    path('list/', views.sensor_list, name='sensor_list')  # get req. to retrieve and display all records
]