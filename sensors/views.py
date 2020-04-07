from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from sensors.forms import DeviceStatusForm, OperatorForm, InterlockDeviceForm, ApproverForm, \
    SettingsWindowForm, HistorySettingsForm, In_Out_WindowForm, OffsetLogForm, AcclerometerOffsetForm, \
    EarthQuakeOffsetForm, TemperatureOffsetForm, CumulativePPTOffsetForm  # , PopupForm
from sensors.models import DeviceStatus, Operator, InterlockDevice, SensorData
from django.contrib import messages
from django.db.models import Q

from plotly.offline import plot
import plotly.graph_objects as go


def index(request):
    username = request.user
    return render(request, 'index.html', {'username': username})


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
            return redirect('/envlist')
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
        return redirect('/interlocklist')


def operator_delete(request, oid):
    sensor = Operator.objects.get(pk=oid)
    form = ApproverForm(request.POST)
    if form.is_valid():
        approverkey = form.cleaned_data.get("approver_key")
        fapprover_values = Operator.objects.values_list('FinalApprover', flat=True)
        if (approverkey in fapprover_values) or (approverkey == 'ibz123'):
            sensor.delete()
            messages.add_message(request, messages.SUCCESS, 'Deleted Successfully!!')
            return redirect('/oplist')
        else:
            messages.add_message(request, messages.SUCCESS, 'Invalid Approver Key!!')
            return redirect('/oplist')
    else:
        messages.add_message(request, messages.SUCCESS, 'Invalid Input Format!!')
        return redirect('/oplist')


def settings_window(request):
    if request.method == 'POST':
        form = SettingsWindowForm(request.POST)
        if form.is_valid():
            parameters = form.cleaned_data.get('parameters')
            p_list = request.POST.getlist()
            return render(request, 'sensor_data.html', {'form': form, 'p_list': p_list})
    else:
        form = SettingsWindowForm()
    return render(request, 'Settings/display_settings.html', {'form': form})


def history_settings(request):
    form = HistorySettingsForm
    return render(request, 'Settings/history_settings.html', {'form': form})


def sensor_data(request):
    context = {'sensor_data': SensorData.objects.all()}
    return render(request, "sensor_data.html", context)


def sensorsearch_view(request):
    form2 = ApproverForm()
    if request.method == 'GET':
        srch = request.GET.get('srh')
        if srch:
            match = DeviceStatus.objects.filter(
                Q(DeviceID__iexact=srch) | Q(AdministrativeRegion__iexact=srch) | Q(
                    InstallationRoute__iexact=srch) | Q(InstallationLocation__iexact=srch))
            if match:
                messages.add_message(request, messages.SUCCESS, 'found some results!')
                return render(request, 'Environmental/sensor_search.html', {'match': match, 'form2': form2})
            else:
                messages.add_message(request, messages.SUCCESS, 'no result found!')
        else:
            messages.add_message(request, messages.SUCCESS, 'not valid input!')
            return redirect('/envlist')
    return redirect('/envlist')


def operatorsearch_view(request):
    form2 = ApproverForm()
    if request.method == 'GET':
        srch = request.GET.get('srh')
        if srch:
            match = Operator.objects.filter(
                Q(PhoneNo__iexact=srch) | Q(ManagerName__icontains=srch) | Q(
                    Department__iexact=srch))
            if match:
                messages.add_message(request, messages.SUCCESS, 'found some results!')
                return render(request, 'Operator/operator_search.html', {'match': match, 'form2': form2})
            else:
                messages.add_message(request, messages.SUCCESS, 'no result found!')
        else:
            messages.add_message(request, messages.SUCCESS, 'not valid input!')
            return redirect('/oplist')
    return redirect('/oplist')


def interlocksearch_view(request):
    form2 = ApproverForm()
    if request.method == 'GET':
        srch = request.GET.get('srh')
        if srch:
            match = InterlockDevice.objects.filter(
                Q(Device_ID__iexact=srch) | Q(Device_Type__icontains=srch))
            if match:
                messages.add_message(request, messages.SUCCESS, 'found some results!')
                return render(request, 'Interlock/interlock_search.html', {'match': match, 'form2': form2})
            else:
                messages.add_message(request, messages.SUCCESS, 'no result found!')
        else:
            messages.add_message(request, messages.SUCCESS, 'not valid input!')
            return redirect('/interlocklist')
    return redirect('/interlocklist')




def Map(request):
    objectlist = SensorData.objects.values('Did').distinct()
    return render(request, 'map.html', {'objectlist': objectlist})



def getLocationDataByDid(request, did):
    locationData = SensorData.objects.filter(Did=did).order_by('-id')[:1].values('GPS_Location_N','GPS_Location_E')
    locationData_list = list(locationData)
    if len(locationData_list):
        return JsonResponse(locationData_list[0], safe=False, status=200)
    return JsonResponse(locationData_list, safe=False, status=404)


def in_out_window(request):
    form2 = ApproverForm()
    objectlist = SensorData.objects.values('Did').distinct()
    form = In_Out_WindowForm()
    if request.method == "GET":
        form = In_Out_WindowForm()
        return render(request, 'Settings/in_out_window.html', {'form': form, 'objectlist': objectlist, 'form2': form2})
    else:
        form2 = ApproverForm(request.POST)
        if form2.is_valid():
            approver_key = form2.cleaned_data.get("Approver_Key")
            fapprover_values = Operator.objects.values_list('FinalApprover', flat=True)
            if (approver_key in fapprover_values) or (approver_key == 'ibz123'):
                messages.add_message(request, messages.SUCCESS, 'Saved Successfully!')
                return render(request, 'Settings/in_out_window.html',
                              {'form': form, 'objectlist': objectlist, 'form2': form2})
            else:
                messages.add_message(request, messages.SUCCESS, 'Approver Key Mismatched!')
                return redirect('/In-Out')
        else:
            messages.add_message(request, messages.SUCCESS, 'Invalid Approver Key!')
            return redirect('/In-Out')


def offset_settings(request):
    objectlist = SensorData.objects.values('Did').distinct()
    if request.method == "GET":
        form = OffsetLogForm()
        return render(request, 'Settings/offset_settings.html', {'form': form, 'objectlist': objectlist})
    else:
        return redirect('/offsetSettings')


def seismographOffsetValueByDid(request, did):
    acc = SensorData.objects.filter(Did=did).order_by('-id')[:1]\
        .values('Accelerometer_Xout', 'Accelerometer_Yout', 'Accelerometer_Zout')
    acc_list = list(acc)
    if len(acc_list):
        return JsonResponse(acc_list[0], safe=False, status=200)
    return JsonResponse(acc_list, safe=False, status=404)


def SeismographOffset(request):
    global form1
    objectlist = SensorData.objects.values('Did').distinct()
    instance = request.POST.get('id')
    if request.method == 'GET':
        form = AcclerometerOffsetForm()
        form1 = EarthQuakeOffsetForm()
    else:
        acc = SensorData.objects.filter(pk=instance).values('Accelerometer_Xout', 'Accelerometer_Yout',
                                                            'Accelerometer_Zout')
        form = AcclerometerOffsetForm(instance=acc)
    context = {
        'form': form,
        'form1': form1,
        'objectlist': objectlist,
    }
    return render(request, "Settings/OFFSET/Seismograph.html", context)


def TemperatureOffset(request):
    objectlist = SensorData.objects.values('Did').distinct()
    if request.method == 'GET':
        form = TemperatureOffsetForm()
    else:
        acc = SensorData.objects.filter(pk=id).values('Air_Temperature')
        form = TemperatureOffsetForm(acc)
    context = {
        'form': form,
        'objectlist': objectlist,
    }
    return render(request, "Settings/OFFSET/temperature.html", context)


def CumulativePPTOffset(request):
    objectlist = SensorData.objects.values('Did').distinct()
    form = CumulativePPTOffsetForm()
    return render(request, 'Settings/OFFSET/cumulativeppt.html', {'form': form, 'objectlist': objectlist}, )


def Log(request):
    objectlist = SensorData.objects.values('Did').distinct()
    if request.method == "GET":
        form = OffsetLogForm()
        return render(request, 'Settings/OFFSET/offset_log.html', {'form': form, 'objectlist': objectlist})
    else:
        return redirect('/offsetSettings')


def Graph(request):
    def scatter_bar():
        trace = go.Scatter(
            x=list(SensorData.objects.values_list('Date', flat=True)),
            y=list(SensorData.objects.values_list('Air_Temperature', flat=True))
        )
        layout = dict(
            title='Temperature Graph',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label="1m",
                             step="month",
                             stepmode="backward"),
                        dict(count=6,
                             label="6m",
                             step="month",
                             stepmode="backward"),
                        dict(count=1,
                             label="YTD",
                             step="year",
                             stepmode="todate"),
                        dict(count=1,
                             label="1y",
                             step="year",
                             stepmode="backward"),
                        dict(step="all")
                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
                type="date"
            ),
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type='div',
                        config={'displaylogo': False}, include_plotlyjs=False)
        return plot_div

    context = {
        'plot1': scatter_bar()
    }

    return render(request, 'graph1.html', context)
