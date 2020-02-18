from django.shortcuts import render, redirect
from sensorreg.form import DeviceStatusForm
from sensorreg.models import DeviceStatus

from django.views.generic import ListView


def sensor_list(request):
    context = {'sensor_list': DeviceStatus.objects.all()}
    return render(request, "sensor_status.html", context)


def sensor_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DeviceStatusForm()
        else:
            sensor = DeviceStatus.objects.get(pk=id)
            form = DeviceStatusForm(instance=sensor)
        return render(request, "sensor_register.html", {'form': form})
    else:
        if id == 0:
            form = DeviceStatusForm(request.POST)
        else:
            sensor = DeviceStatus.objects.get(pk=id)
            form = DeviceStatusForm(request.POST, instance=sensor)
        if form.is_valid():
            form.save()
        return redirect('/list')
#Comment

def sensor_delete(request, id):
    sensor = DeviceStatus.objects.get(pk=id)
    sensor.delete()
    return redirect('/list')
