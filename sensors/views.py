from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from sensors.forms import DeviceStatusForm, OperatorForm, InterlockDeviceForm, ApproverForm, \
    SettingsWindowForm, HistorySettingsForm  # , PopupForm
from sensors.models import DeviceStatus, Operator, InterlockDevice, SensorData
from django.contrib import messages
from django.db.models import Q


def index(request):
    return render(request, 'index.html', {})


def sensor_list(request):
    form2 = ApproverForm()
    context = {'sensor_list': DeviceStatus.objects.all(), 'form2': form2}
    return render(request, "Environmental/sensor_status.html", context)


def interlock_list(request):
    context = {'interlock_list': InterlockDevice.objects.all(), 'form2': ApproverForm()}
    return render(request, "Interlock/interlock_status.html", context)


def operator_list(request):
    context = {'operator_list': Operator.objects.all(), 'form2': ApproverForm()}
    return render(request, "Operator/operatorhandset_status.html", context)


def sensor_form(request, sid=0):
    form2 = ApproverForm()
    if request.method == "GET":
        if sid == 0:
            form = DeviceStatusForm()
        else:
            sensor = DeviceStatus.objects.get(pk=sid)
            form = DeviceStatusForm(instance=sensor)
        return render(request, "Environmental/sensor_register.html", {'form': form, 'form2': form2})
    else:
        form2 = ApproverForm(request.POST)
        if form2.is_valid():
            approverkey = form2.cleaned_data.get("approver_key")
            fapprover_values = Operator.objects.values_list('FinalApprover', flat=True)
            if (approverkey in fapprover_values) or (approverkey == 'ibz123'):
                if sid == 0:
                    form = DeviceStatusForm(request.POST)
                else:
                    sensor = DeviceStatus.objects.get(pk=sid)
                    form = DeviceStatusForm(request.POST, instance=sensor)
                if form.is_valid():
                    form.save()
                    messages.add_message(request, messages.SUCCESS, 'Saved Sucessfully!!')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Invalid Input!!')
                    return render(request, "Environmental/sensor_register.html", {'form': form, 'form2': form2})
                return redirect('/envlist')
            elif sid != 0:
                sensor = DeviceStatus.objects.get(pk=sid)
                form = DeviceStatusForm(request.POST, instance=sensor)
                messages.add_message(request, messages.SUCCESS, 'Invalid Approver Key!!')
                return render(request, "Environmental/sensor_register.html", {'form': form, 'form2': form2})
            else:
                messages.add_message(request, messages.SUCCESS, 'Invalid Approver Key!!')
                return redirect('/sensor')
        else:
            messages.add_message(request, messages.SUCCESS, 'Invalid Input!!')
            return redirect('/sensor')


def interlockdevice_form(request, eid=0):
    form2 = ApproverForm()
    if request.method == "GET":
        if eid == 0:
            form = InterlockDeviceForm()
        else:
            interlockdevice = InterlockDevice.objects.get(pk=eid)
            did = str(interlockdevice.Device_ID)
            interlockdevice.Device_ID = int(did[2:])
            form = InterlockDeviceForm(instance=interlockdevice)
        return render(request, "Interlock/InterlockInfo.html", {'form': form, 'form2': form2})
    else:
        form2 = ApproverForm(request.POST)
        if form2.is_valid():
            approverkey = form2.cleaned_data.get("approver_key")
            fapprover_values = Operator.objects.values_list('FinalApprover', flat=True)
            if (approverkey in fapprover_values) or (approverkey == 'ibz123'):
                if eid == 0:
                    form = InterlockDeviceForm(request.POST)
                else:
                    interlockdevice = InterlockDevice.objects.get(pk=eid)
                    form = InterlockDeviceForm(request.POST, instance=interlockdevice)
                if form.is_valid():
                    form.save()
                    messages.add_message(request, messages.SUCCESS, 'Saved Succesfully!!')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Invalid Approver Key!!')
                    return render(request, "Interlock/InterlockInfo.html", {'form': form, 'form2': form2})
                return redirect('/interlocklist')
            else:
                messages.add_message(request, messages.SUCCESS, 'Invalid Approver Key!!')
                return HttpResponseRedirect('/interlock')
        else:
            messages.add_message(request, messages.SUCCESS, 'Invalid Input!!')
            return HttpResponseRedirect('/interlock')


def operator_form(request, oid=0):
    form2 = ApproverForm()
    if request.method == "GET":
        if oid == 0:
            form = OperatorForm()
        else:
            operator1 = Operator.objects.get(pk=oid)
            form = OperatorForm(instance=operator1)
        return render(request, "Operator/operator_register.html", {'form': form, 'form2': form2})
    else:
        form2 = ApproverForm(request.POST)
        if form2.is_valid():
            approverkey = form2.cleaned_data.get("approver_key")
            if approverkey == 'ibz123':
                if oid == 0:
                    form = OperatorForm(request.POST)
                else:
                    operator1 = Operator.objects.get(pk=oid)
                    form = OperatorForm(request.POST, instance=operator1)
                if form.is_valid():
                    form.save()
                    messages.add_message(request, messages.SUCCESS, 'Saved Successfully!!')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Invalid Input Format!!')
                    return render(request, "Operator/operator_register.html", {'form': form, 'form2': form2})
                return redirect('/oplist')


def sensor_delete(request, sid):
    sensor = DeviceStatus.objects.get(pk=sid)
    form2 = ApproverForm(request.POST)
    if form2.is_valid():
        approverkey = form2.cleaned_data.get("approver_key")
        fapprover_values = Operator.objects.values_list('FinalApprover', flat=True)
        if (approverkey in fapprover_values) or (approverkey == 'ibz123'):
            sensor.delete()
            messages.add_message(request, messages.SUCCESS, 'Deleted Successfully!!')
            return redirect('/envlist')
        else:
            messages.add_message(request, messages.SUCCESS, 'Invalid Approver Key!!')
            return redirect('/oplist')
    else:
        messages.add_message(request, messages.SUCCESS, 'Invalid Input Format!!')
        return redirect('/envlist')


def interlockdevice_delete(request, eid):
    interlockdevice = InterlockDevice.objects.get(pk=eid)
    form = ApproverForm(request.POST)
    if form.is_valid():
        approverkey = form.cleaned_data.get("approver_key")
        fapprover_values = Operator.objects.values_list('FinalApprover', flat=True)
        if (approverkey in fapprover_values) or (approverkey == 'ibz123'):
            interlockdevice.delete()
            messages.add_message(request, messages.SUCCESS, 'Deleted Successfully!!')
            return redirect('/interlocklist')
        else:
            messages.add_message(request, messages.SUCCESS, 'Invalid Approver Key!!')
            return redirect('/interlocklist')
    else:
        messages.add_message(request, messages.SUCCESS, 'Invalid Input Format!!')
        return redirect('/oplist')


def operator_delete(request, oid):
    sensor = Operator.objects.get(pk=oid)
    form = ApproverForm(request.POST)
    if form.is_valid():
        approverkey = form.cleaned_data.get("approver_key")
        fapprover_values = Operator.objects.values_list('FinalApprover', flat=True)
        if (approverkey in fapprover_values) or (approverkey == 'ibz123'):
            sensor.delete()
            return redirect('/oplist')
        return redirect('/oplist')
    return redirect('/oplist')


def settings_window(request):
    form = SettingsWindowForm()
    return render(request, 'Settings/display_settings.html', {'form': form})


def history_settings(request):
    form = HistorySettingsForm
    return render(request, 'Settings/history_settings.html', {'form': form})


def sensor_data(request):
    context = {'sensor_data': SensorData.objects.all()}
    return render(request, "sensor_data.html", context)


def search_view(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = DeviceStatus.objects.filter(
                Q(DeviceID__iexact=srch) | Q(AdministrativeRegion__iexact=srch) | Q(
                    InstallationRoute__iexact=srch) | Q(InstallationLocation__iexact=srch))
            if match:
                messages.add_message(request, messages.SUCCESS, 'found some results!')
                return render(request, 'Environmental/sensor_status.html', {'match': match})
            else:
                messages.add_message(request, messages.SUCCESS, 'no result found!')
        else:
            messages.add_message(request, messages.SUCCESS, 'not valid input')
            return redirect('/envlist')
    return redirect('/envlist')



