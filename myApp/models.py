from django.db import models
from datetime import datetime, timedelta

one_week = timedelta(days=7)
# Create your models here.
class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, null = True)
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=12, null=True)

    def __str__(self):
        return "Sucursal " + self.direccion

class Adicional(models.Model):
    nombre = models.CharField(max_length=80)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class Combo(models.Model):
    id_combo = models.AutoField(primary_key=True)
    precio = models.FloatField()
    descripcion = models.TextField()

    def getElementos(self):
        return self.descripcion.split("\n")

    def __str__(self):
        return "Combo " + str(self.id_combo)

class Evento(models.Model):
    fecha = models.DateTimeField(null=False)
    sucursal = models.ForeignKey(Sucursal, on_delete=False)
    combo = models.ForeignKey(Combo, on_delete=False, null=True)
    encargado = models.CharField(max_length=30)
    sena = models.IntegerField()
    fecha_sena = models.DateField()
    vencimiento = models.DateField(null=True)
    precio = models.FloatField()
    nombre_solicitante = models.CharField(max_length=40)
    telefono_solicitante= models.CharField(max_length=12)
    nombre_cumpleanero = models.CharField(max_length=40)
    observaciones = models.TextField(null=True)
    adicionales = models.ManyToManyField(Adicional, blank=True, null=True)

    def deuda(self):
        return self.precio - self.sena

    def vencimiento(self):
        return self.fecha - one_week

    def __str__(self):
        return "Evento " + self.fecha.strftime("%d %b %Y")