from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Evento, Sucursal
from .forms import EntryForm, SearchForm

def index(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():

            date1 = form.cleaned_data['f_inicial']
            date2 = form.cleaned_data['f_cierre']


            eventos = Evento.objects.all().filter(fecha__range=(date1, date2)).order_by('fecha')
            sucursales = Sucursal.objects.get(id_sucursal=1)
            return render(request, "myApp/index.html", {'eventos': eventos, 'sucursales': sucursales, 'form': form})
            return render(request, "myApp/index.html", {'eventos': eventos})
    else:
        form = SearchForm()

        eventos = Evento.objects.all().order_by('fecha')
        sucursales = Sucursal.objects.get(id_sucursal=1)
        return render(request, "myApp/index.html", {'eventos': eventos, 'sucursales': sucursales, 'form': form})


def sucursal(request, pk):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():

            date1 = form.cleaned_data['f_inicial']
            date2 = form.cleaned_data['f_cierre']

            form = SearchForm()

            sucursal = Sucursal.objects.get(id_sucursal=pk)
            eventos = Evento.objects.filter(sucursal=sucursal).filter(fecha__range=(date1,date2))
            return render(request, "myApp/sucursal.html", {'eventos': eventos, 'form':form})

    form = SearchForm()
    sucursal = Sucursal.objects.get(id_sucursal=pk)
    eventos = Evento.objects.filter(sucursal=sucursal)
    return render(request, "myApp/sucursal.html", {'eventos' : eventos, 'form':form})

def detalles(request, pk):
    evento = Evento.objects.get(pk=pk)
    return render(request, "myApp/detalles.html", {'evento' : evento})

def rango(request):
    pass

def add(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            sucursal = form.cleaned_data['sucursal']
            combo = form.cleaned_data['combo']
            encargado = form.cleaned_data['encargado']
            sena = form.cleaned_data['seña']
            fecha_sena = form.cleaned_data['fecha_seña']
            precio = form.cleaned_data['precio']
            nombre_solicitante = form.cleaned_data['nombre_solicitante']
            telefono_solicitante = form.cleaned_data['telefono_solicitante']
            nombre_cumpleanero = form.cleaned_data['nombre_cumpleañero']
            observaciones = form.cleaned_data['observaciones']
            adicionales = form.cleaned_data['adicionales']

            Evento.objects.create(
            fecha=fecha,
            sucursal = sucursal,
            combo = combo,
            encargado = encargado,
            sena = sena,
            fecha_sena = fecha_sena,
            precio = precio,
            nombre_solicitante = nombre_solicitante,
            telefono_solicitante = telefono_solicitante,
            nombre_cumpleanero = nombre_cumpleanero,
            observaciones = observaciones,
            ).save()


            Evento.objects.last().adicionales.set(adicionales)

            return HttpResponseRedirect('/')
    else:
        form = EntryForm()

    return render(request, 'myApp/form2.html', {'form2':form})

def delete(request,pk):

    if request.method == 'DELETE':
        entry = get_object_or_404(Evento, pk=pk)
        entry.delete()


    return HttpResponseRedirect('/')