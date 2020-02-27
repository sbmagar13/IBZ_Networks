from django.shortcuts import render, redirect
from sensorreg.form import DeviceStatusForm, OperatorForm, InterlockDeviceForm
from sensorreg.models import DeviceStatus,Operator,InterlockDevice

from django.views.generic import ListView



# def env_list(request):
#     form=DeviceStatusForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = DeviceStatusForm()
#     context = {'form': form}
#     return render(request, "show.html", context)


def sensor_list(request):
    context = {'sensor_list': DeviceStatus.objects.all()}
    return render(request, "Environmental/sensor_status.html", context)

def interlock_list(request):
    context = {'interlock_list': InterlockDevice.objects.all()}
    return render(request, "Interlock/interlock_status.html", context)

def operator_list(request):
    context = {'operator_list': Operator.objects.all()}
    return render(request, "Operator/operatorhandset_status.html", context)

def sensor_form(request, sid=0):
    if request.method == "GET":
        if sid == 0:
            form = DeviceStatusForm()
        else:
            sensor = DeviceStatus.objects.get(pk=sid)
            form = DeviceStatusForm(instance=sensor)
        return render(request, "Environmental/sensor_register.html", {'form': form})
    else:
        if sid == 0:
            form = DeviceStatusForm(request.POST)
        else:
            sensor = DeviceStatus.objects.get(pk=sid)
            form = DeviceStatusForm(request.POST, instance=sensor)
        if form.is_valid():
            form.save()
        else:
            return render(request, "Environmental/sensor_register.html", {'form': form})
        return redirect('/envlist')


def interlockdevice_form(request, eid=0):
    if request.method == "GET":
        if eid == 0:
            form = InterlockDeviceForm()
        else:
            interlockdevice = InterlockDevice.objects.get(pk=eid)
            form = InterlockDeviceForm(instance=interlockdevice)
        return render(request, "Interlock/interlockinformation.html", {'form': form})
    else:
        if eid == 0:
            form = InterlockDeviceForm(request.POST)
        else:
            interlockdevice = InterlockDevice.objects.get(pk=eid)
            form = InterlockDeviceForm(request.POST, instance=interlockdevice)
        if form.is_valid():
            form.save()
        else:
            return render(request, "Interlock/interlockinformation.html", {'form': form})
        return redirect('/interlocklist')

def operator_form(request, oid=0):
    if request.method == "GET":
        if oid == 0:
            form = OperatorForm()
        else:
            sensor = Operator.objects.get(pk=oid)
            form = OperatorForm(instance=sensor)
        return render(request, "Operator/operator_register.html", {'form': form})
    else:
        if oid == 0:
            form = OperatorForm(request.POST)
        else:
            sensor =Operator.objects.get(pk=oid)
            form = OperatorForm(request.POST, instance=sensor)
        if form.is_valid():
            form.save()
        else:
            return render(request, "Operator/operator_register.html", {'form': form})
        return redirect('/oplist')
#Comment

def sensor_delete(request, sid):
    sensor = DeviceStatus.objects.get(pk=sid)
    sensor.delete()
    return redirect('/envlist')

def interlockdevice_delete(request, eid):
    interlockdevice = InterlockDevice.objects.get(pk=eid)
    interlockdevice.delete()
    return redirect('/interlocklist')

def operator_delete(request, oid):
    sensor = Operator.objects.get(pk=oid)
    sensor.delete()
    return redirect('/oplist')