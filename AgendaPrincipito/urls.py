from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rango/', views.rango, name='rango'),
    path('sucursal/<int:pk>', views.sucursal, name= 'sucursal'),
    path('evento/<int:pk>', views.detalles, name='detalles'),
    path('evento/add', views.add, name='add'),
    path('evento/delete/<int:pk>', views.delete, name='delete'),
    path('admin/', admin.site.urls),
]
