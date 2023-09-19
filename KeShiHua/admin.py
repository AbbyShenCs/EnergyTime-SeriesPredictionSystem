from django.contrib import admin
from .models import *
from openpyxl import Workbook
from django.http import HttpResponse

admin.site.site_title = "Energy Temporal Forecast"
admin.site.site_header = "Energy Temporal Forecast"


class ExportExcelMixin(object):
    def export_as_excel(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='application/msexcel')
        response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'
        wb = Workbook()
        ws = wb.active
        ws.append(field_names)
        for obj in queryset:
            for field in field_names:
                data = [f'{getattr(obj, field)}' for field in field_names]
            row = ws.append(data)

        wb.save(response)
        return response

    export_as_excel.short_description = 'Export to Excel'


from django.contrib.admin import SimpleListFilter
import datetime
from django.db.models import Q


class CurrentFilter(SimpleListFilter):
    title = 'Alert Status'
    parameter_name = 'Alert Status'

    def lookups(self, request, model_admin):
        return [(1, 'Normal'), (2, 'Abnormal'), (3, 'Alert')]

    def queryset(self, request, queryset):
        # pdb.set_trace()
        if self.value():
            return queryset


@admin.register(ShuJu)
class ShuJu_Admin(admin.ModelAdmin, ExportExcelMixin):
    list_display = (
        "date", "Total_radiation", "Direct_radiation", "Diffuse_radiation", "Temperature", "Pressure", "Humidity",
        "Actual_power", "Rated_power", "type")
    actions = ['export_as_excel']
    search_fields = (
        "date", "Total_radiation", "Direct_radiation", "Diffuse_radiation", "Temperature", "Pressure", "Humidity",
        "Actual_power", "Rated_power", "type")
    list_filter = ("date", "type", CurrentFilter)


@admin.register(Lishi_ShuJu)
class Lishi_ShuJu_Admin(admin.ModelAdmin, ExportExcelMixin):
    list_display = (
        "date", "Total_radiation", "Direct_radiation", "Diffuse_radiation", "Temperature", "Pressure", "Humidity",
        "Actual_power", "Rated_power")
    actions = ['export_as_excel']
    search_fields = (
        "date", "Total_radiation", "Direct_radiation", "Diffuse_radiation", "Temperature", "Pressure", "Humidity",
        "Actual_power", "Rated_power")
    list_filter = ("date", CurrentFilter)


@admin.register(YuCe_ShuJu)
class YuCe_ShuJu_Admin(admin.ModelAdmin, ExportExcelMixin):
    list_display = (
        "date", "Total_radiation", "Direct_radiation", "Diffuse_radiation", "Temperature", "Pressure", "Humidity",
        "Actual_power", "Rated_power", "type")
    actions = ['export_as_excel']
    search_fields = (
        "date", "Total_radiation", "Direct_radiation", "Diffuse_radiation", "Temperature", "Pressure", "Humidity",
        "Actual_power", "Rated_power", "type")
    list_filter = ("date", "type", CurrentFilter)


@admin.register(Lishi_YuCe_ShuJu)
class Lishi_YuCe_ShuJu_Admin(admin.ModelAdmin, ExportExcelMixin):
    list_display = (
        "date", "Total_radiation", "Direct_radiation", "Diffuse_radiation", "Temperature", "Pressure", "Humidity",
        "Actual_power", "Rated_power")
    actions = ['export_as_excel']
    search_fields = (
        "date", "Total_radiation", "Direct_radiation", "Diffuse_radiation", "Temperature", "Pressure", "Humidity",
        "Actual_power", "Rated_power")
    list_filter = ("date",)


from django.contrib.auth.models import User


@admin.register(Users)
class Users_Admin(admin.ModelAdmin, ExportExcelMixin):
    list_display = ("username", "email", "set", "age")
    actions = ['export_as_excel', 'ExcelImportForm']
    search_fields = ("username",)
