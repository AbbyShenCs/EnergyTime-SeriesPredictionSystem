import time
from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib.auth.decorators import login_required
from KeShiHua import models
from django.db.models import Q
from django.shortcuts import get_object_or_404, HttpResponseRedirect
import json
import random


# Create your views here.
@login_required
def yujing(request):
    if request.method == 'GET':
        datas = models.ShuJu.objects.all().order_by('-date')
        results = []
        for resu in datas:
            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Temperature'
            dicts['value'] = resu.Temperature  
            dicts['quyu'] = resu.type
            if 4 < resu.Temperature <= 40: 
                dicts['status'] = 'normal'
            elif 40 < resu.Temperature <= 54:  
                dicts['status'] = 'abnormal'
            else:
                dicts['status'] = 'alert'

            results.append(dicts)

            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Humidity'
            dicts['value'] = resu.Humidity 
            dicts['quyu'] = resu.type
            if dicts['value'] < 75:
                dicts['status'] = 'normal'
            else:
                dicts['status'] = 'abnormal'
            results.append(dicts)
        return render(request, r"admin\yujing.html", locals())


@login_required
def chakan(request):
    if request.method == 'GET':
        datas = models.ShuJu.objects.filter(type=1).order_by('-date')
        datas1 = models.ShuJu.objects.filter(type=2).order_by('-date')
        datas2 = models.ShuJu.objects.filter(type=3).order_by('-date')
        results = []
        for resu in datas[::-1][:1]:
            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Temperature'
            dicts['value'] = resu.Temperature
            dicts['quyu'] = resu.type
            if 4 < resu.Temperature <= 40:
                dicts['status'] = 'normal'
            elif 40 < resu.Temperature <= 54:
                dicts['status'] = 'abnormal'
            else:
                dicts['status'] = 'alert'

            results.append(dicts)

            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Humidity'
            dicts['value'] = resu.Humidity
            dicts['quyu'] = resu.type
            if dicts['value'] < 75:
                dicts['status'] = 'normal'
            else:
                dicts['status'] = 'abnormal'
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Total_radiation'
            dicts['value'] = resu.Total_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Direct_radiation'
            dicts['value'] = resu.Direct_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Diffuse_radiation'
            dicts['value'] = resu.Diffuse_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Pressure'
            dicts['value'] = resu.Pressure
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Actual_power'
            dicts['value'] = resu.Actual_power
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Rated_power'
            dicts['value'] = resu.Rated_power
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

        for resu in datas1[::-1][:1]:
            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Temperature'
            dicts['value'] = resu.Temperature
            dicts['quyu'] = resu.type
            if 4 < resu.Temperature <= 40:
                dicts['status'] = 'normal'
            elif 40 < resu.Temperature <= 54:
                dicts['status'] = 'abnormal'
            else:
                dicts['status'] = 'alert'

            results.append(dicts)

            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Humidity'
            dicts['value'] = resu.Humidity
            dicts['quyu'] = resu.type
            if dicts['value'] < 75:
                dicts['status'] = 'normal'
            else:
                dicts['status'] = 'abnormal'
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Total_radiation'
            dicts['value'] = resu.Total_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Direct_radiation'
            dicts['value'] = resu.Direct_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Diffuse_radiation'
            dicts['value'] = resu.Diffuse_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Pressure'
            dicts['value'] = resu.Pressure
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Actual_power'
            dicts['value'] = resu.Actual_power
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Rated_power'
            dicts['value'] = resu.Rated_power
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

        for resu in datas2[::-1][:1]:
            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Temperature'
            dicts['value'] = resu.Temperature
            dicts['quyu'] = resu.type
            if 4 < resu.Temperature <= 40:
                dicts['status'] = 'normal'
            elif 40 < resu.Temperature <= 54:
                dicts['status'] = 'abnormal'
            else:
                dicts['status'] = 'alert'

            results.append(dicts)

            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Humidity'
            dicts['value'] = resu.Humidity
            dicts['quyu'] = resu.type
            if dicts['value'] < 75:
                dicts['status'] = 'normal'
            else:
                dicts['status'] = 'abnormal'
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Total_radiation'
            dicts['value'] = resu.Total_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Direct_radiation'
            dicts['value'] = resu.Direct_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Diffuse_radiation'
            dicts['value'] = resu.Diffuse_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Pressure'
            dicts['value'] = resu.Pressure
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Actual_power'
            dicts['value'] = resu.Actual_power
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Rated_power'
            dicts['value'] = resu.Rated_power
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

        datas = models.YuCe_ShuJu.objects.filter(type=1).order_by('-date')
        datas1 = models.YuCe_ShuJu.objects.filter(type=2).order_by('-date')
        datas2 = models.YuCe_ShuJu.objects.filter(type=3).order_by('-date')
        results1 = []
        for resu in datas[::-1][:1]:
            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Temperature'
            dicts['value'] = resu.Temperature
            dicts['quyu'] = resu.type
            if 4 < resu.Temperature <= 40:
                dicts['status'] = 'normal'
            elif 40 < resu.Temperature <= 54:
                dicts['status'] = 'abnormal'
            else:
                dicts['status'] = 'alert'

            results1.append(dicts)

            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Humidity'
            dicts['value'] = resu.Humidity
            dicts['quyu'] = resu.type
            if dicts['value'] < 75:
                dicts['status'] = 'normal'
            else:
                dicts['status'] = 'abnormal'
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Total_radiation'
            dicts['value'] = resu.Total_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Direct_radiation'
            dicts['value'] = resu.Direct_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Diffuse_radiation'
            dicts['value'] = resu.Diffuse_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Pressure'
            dicts['value'] = resu.Pressure
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Actual_power'
            dicts['value'] = resu.Actual_power
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Rated_power'
            dicts['value'] = resu.Rated_power
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

        for resu in datas1[::-1][:1]:
            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Temperature'
            dicts['value'] = resu.Temperature
            dicts['quyu'] = resu.type
            if 4 < resu.Temperature <= 40:
                dicts['status'] = 'normal'
            elif 40 < resu.Temperature <= 54:
                dicts['status'] = 'abnormal'
            else:
                dicts['status'] = 'alert'

            results1.append(dicts)

            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Humidity'
            dicts['value'] = resu.Humidity
            dicts['quyu'] = resu.type
            if dicts['value'] < 75:
                dicts['status'] = 'normal'
            else:
                dicts['status'] = 'abnormal'
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Total_radiation'
            dicts['value'] = resu.Total_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Direct_radiation'
            dicts['value'] = resu.Direct_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Diffuse_radiation'
            dicts['value'] = resu.Diffuse_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Pressure'
            dicts['value'] = resu.Pressure
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Actual_power'
            dicts['value'] = resu.Actual_power
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Rated_power'
            dicts['value'] = resu.Rated_power
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

        for resu in datas2[::-1][:1]:
            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Temperature'
            dicts['value'] = resu.Temperature
            dicts['quyu'] = resu.type
            if 4 < resu.Temperature <= 40:
                dicts['status'] = 'normal'
            elif 40 < resu.Temperature <= 54:
                dicts['status'] = 'abnormal'
            else:
                dicts['status'] = 'alert'

            results1.append(dicts)

            dicts = {}
            dicts['date'] = resu.date
            dicts['type'] = 'Humidity'
            dicts['value'] = resu.Humidity
            dicts['quyu'] = resu.type
            if dicts['value'] < 75:
                dicts['status'] = 'normal'
            else:
                dicts['status'] = 'abnormal'
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Total_radiation'
            dicts['value'] = resu.Total_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Direct_radiation'
            dicts['value'] = resu.Direct_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Diffuse_radiation'
            dicts['value'] = resu.Diffuse_radiation
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Pressure'
            dicts['value'] = resu.Pressure
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results1.append(dicts)

            dicts = {}
            dicts['type'] = 'Actual_power'
            dicts['value'] = resu.Actual_power
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

            dicts = {}
            dicts['type'] = 'Rated_power'
            dicts['value'] = resu.Rated_power
            dicts['status'] = 'normal'
            dicts['quyu'] = resu.type
            results.append(dicts)

        return render(request, r"admin\chakan.html", locals())


@login_required
def jiankong(request):
    if request.method == 'GET':
        types = request.GET.get('types')
        types = str(types)
        if types:
            datas = models.ShuJu.objects.filter(type=types).order_by('-date')
        else:
            datas = models.ShuJu.objects.all().order_by('-date')

        #
        Temperature_name = []
        Temperature_count = []
        Temperature_count_1 = ''
        Humidity_count = []
        Humidity_count_1 = ''
        Total_radiation_count = []
        Total_radiation_count_1 = ''
        Diffuse_radiation_count = []
        Diffuse_radiation_count_1 = ''
        Direct_radiation_count = []
        Direct_radiation_count_1 = ''
        Pressure_count = []
        Pressure_count_1 = ''
        Actual_power_count = []
        Actual_power_count_1 = ''
        Rated_power_count = []
        Rated_power_count_1 = ''

        resu = ''
        for resu in datas[::-1][:100]:
            Temperature_name.append(resu.date.strftime('%H:%M:%S'))
            Temperature_count.append(resu.Temperature)
            Humidity_count.append(resu.Humidity)
            Total_radiation_count.append(resu.Total_radiation)
            Diffuse_radiation_count.append(resu.Diffuse_radiation)
            Direct_radiation_count.append(resu.Direct_radiation)
            Pressure_count.append(resu.Pressure)
            Actual_power_count.append(resu.Actual_power)
            Rated_power_count.append(resu.Rated_power)
        if resu:
            Temperature_count_1 = resu.Temperature
            Humidity_count_1 = resu.Humidity
            Total_radiation_count_1 = resu.Total_radiation
            # Total_radiation_count_1 = 399
            Diffuse_radiation_count_1 = resu.Diffuse_radiation
            Direct_radiation_count_1 = resu.Direct_radiation
            Pressure_count_1 = resu.Pressure
            Actual_power_count_1 = resu.Actual_power
            Rated_power_count_1 = resu.Rated_power

        print('Temperature_name', Temperature_name)
        print('Total_radiation_count', Total_radiation_count)
        print('Total_radiation_count_1', Total_radiation_count_1)
        return render(request, r"admin\jiankong.html", locals())


@login_required
def yuce(request):
    if request.method == 'GET':
        types = request.GET.get('types')
        if types:
            datas = models.YuCe_ShuJu.objects.filter(type=types).order_by('-date')
            datas1 = models.ShuJu.objects.filter(type=types).order_by('-date')
        else:
            datas = models.YuCe_ShuJu.objects.all().order_by('-date')
            datas1 = models.ShuJu.objects.all().order_by('-date')

        #
        Temperature_name = []
        Temperature_count = []
        Temperature_count_1 = ''
        Humidity_count = []
        Humidity_count_1 = ''
        Total_radiation_count = []
        Total_radiation_count_1 = ''
        Diffuse_radiation_count = []
        Diffuse_radiation_count_1 = ''
        Direct_radiation_count = []
        Direct_radiation_count_1 = ''
        Pressure_count = []
        Pressure_count_1 = ''
        Actual_power_count = []
        Actual_power_count_1 = ''
        Rated_power_count = []
        Rated_power_count_1 = ''

        resu = ''
        for resu in datas[:100][::-1]:
            Temperature_name.append(resu.date.strftime('%H:%M:%S'))
            Temperature_count.append(resu.Temperature)
            Humidity_count.append(resu.Humidity)
            Total_radiation_count.append(resu.Total_radiation)
            Diffuse_radiation_count.append(resu.Diffuse_radiation)
            Direct_radiation_count.append(resu.Direct_radiation)
            Pressure_count.append(resu.Pressure)
            Actual_power_count.append(resu.Actual_power)
            Rated_power_count.append(resu.Rated_power)
        if resu:
            Temperature_count_1 = resu.Temperature
            Humidity_count_1 = resu.Humidity
            Total_radiation_count_1 = resu.Total_radiation
            Diffuse_radiation_count_1 = resu.Diffuse_radiation
            Direct_radiation_count_1 = resu.Direct_radiation
            Pressure_count_1 = resu.Pressure
            Actual_power_count_1 = resu.Actual_power
            Rated_power_count_1 = resu.Rated_power

        Temperature_count_2 = []
        Humidity_count_2 = []
        Total_radiation_count_2 = []
        Diffuse_radiation_count_2 = []
        Direct_radiation_count_2 = []
        Pressure_count_2 = []
        Actual_power_count_2 = []
        Rated_power_count_2 = []
        for resu in datas1[:100][::-1]:
            Temperature_count_2.append(resu.Temperature)
            Humidity_count_2.append(resu.Humidity)
            Total_radiation_count_2.append(resu.Total_radiation)
            Diffuse_radiation_count_2.append(resu.Diffuse_radiation)
            Direct_radiation_count_2.append(resu.Direct_radiation)
            Pressure_count_2.append(resu.Pressure)
            Actual_power_count_2.append(resu.Actual_power)
            Rated_power_count_2.append(resu.Rated_power)

        return render(request, r"admin\yuce.html", locals())
