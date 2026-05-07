from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),

    path('clientes/', views.lista_clientes, name='clientes'),

    path('clientes/nuevo/',
         views.crear_cliente,
         name='crear_cliente'),

    path('clientes/editar/<int:id>/',
         views.editar_cliente,
         name='editar_cliente'),

    path('clientes/eliminar/<int:id>/',
         views.eliminar_cliente,
         name='eliminar_cliente'),



    path('vehiculos/', views.lista_vehiculos, name='vehiculos'),

    path(
        'vehiculos/nuevo/',
        views.crear_vehiculo,
        name='crear_vehiculo'
    ),

    path(
        'vehiculos/editar/<int:id>/',
        views.editar_vehiculo,
        name='editar_vehiculo'
    ),

    path(
        'vehiculos/eliminar/<int:id>/',
        views.eliminar_vehiculo,
        name='eliminar_vehiculo'
    ),


    path('espacios/', views.lista_espacios, name='espacios'),

    path(
        'espacios/nuevo/',
        views.crear_espacio,
        name='crear_espacio'
    ),

    path(
        'espacios/editar/<int:id>/',
        views.editar_espacio,
        name='editar_espacio'
    ),

    path(
        'espacios/eliminar/<int:id>/',
        views.eliminar_espacio,
        name='eliminar_espacio'
    ),

]
