from django import forms
from django.forms import SelectDateWidget, DateTimeInput
from datetimepicker.widgets import DateTimePicker
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput

from .models import *

sucursales = Sucursal.objects.all()
combos = Combo.objects.all()
adicionales = Adicional.objects.all()

class EntryForm(forms.Form):
    fecha = forms.DateTimeField(widget=DateTimePickerInput())
    sucursal = forms.ModelChoiceField(sucursales)
    combo =forms.ModelChoiceField(combos)
    encargado = forms.CharField(max_length=30)
    seña = forms.IntegerField()
    fecha_seña = forms.DateField(widget=forms.SelectDateWidget)
    precio = forms.FloatField()
    nombre_solicitante = forms.CharField(max_length=40)
    telefono_solicitante = forms.CharField(max_length=12)
    nombre_cumpleañero = forms.CharField(max_length=40)
    adicionales =forms.ModelMultipleChoiceField(adicionales)
    observaciones = forms.CharField(widget=forms.Textarea, required=False)

class SearchForm(forms.Form):
    f_inicial = forms.DateField(widget=forms.SelectDateWidget, initial=None)
    f_cierre = forms.DateField(widget=forms.SelectDateWidget, initial=None)