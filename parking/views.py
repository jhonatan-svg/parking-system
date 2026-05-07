from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Vehiculo, Espacio, Tarifa, Cobro

from .forms import (
    ClienteForm,
    VehiculoForm,
    EspacioForm,
    TarifaForm,
    CobroForm
)


def inicio(request):
    return render(request, 'parking/inicio.html')


def lista_clientes(request):
    clientes = Cliente.objects.all()

    return render(request,
                  'parking/clientes/lista.html',
                  {'clientes': clientes})


def crear_cliente(request):

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('clientes')

    else:
        form = ClienteForm()

    return render(request,
                  'parking/clientes/form.html',
                  {'form': form})


def editar_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            return redirect('clientes')

    else:
        form = ClienteForm(instance=cliente)

    return render(request,
                  'parking/clientes/form.html',
                  {'form': form})


def eliminar_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    cliente.delete()

    return redirect('clientes')

def lista_vehiculos(request):

    vehiculos = Vehiculo.objects.all()

    return render(
        request,
        'parking/vehiculos/lista.html',
        {'vehiculos': vehiculos}
    )


def crear_vehiculo(request):

    if request.method == 'POST':

        form = VehiculoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('vehiculos')

    else:
        form = VehiculoForm()

    return render(
        request,
        'parking/vehiculos/form.html',
        {'form': form}
    )


def editar_vehiculo(request, id):

    vehiculo = get_object_or_404(Vehiculo, id=id)

    if request.method == 'POST':

        form = VehiculoForm(
            request.POST,
            instance=vehiculo
        )

        if form.is_valid():
            form.save()
            return redirect('vehiculos')

    else:
        form = VehiculoForm(instance=vehiculo)

    return render(
        request,
        'parking/vehiculos/form.html',
        {'form': form}
    )


def eliminar_vehiculo(request, id):

    vehiculo = get_object_or_404(Vehiculo, id=id)

    vehiculo.delete()

    return redirect('vehiculos')


def lista_espacios(request):

    espacios = Espacio.objects.all()

    return render(
        request,
        'parking/espacios/lista.html',
        {'espacios': espacios}
    )


def crear_espacio(request):

    if request.method == 'POST':

        form = EspacioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('espacios')

    else:
        form = EspacioForm()

    return render(
        request,
        'parking/espacios/form.html',
        {'form': form}
    )


def editar_espacio(request, id):

    espacio = get_object_or_404(Espacio, id=id)

    if request.method == 'POST':

        form = EspacioForm(
            request.POST,
            instance=espacio
        )

        if form.is_valid():
            form.save()
            return redirect('espacios')

    else:
        form = EspacioForm(instance=espacio)

    return render(
        request,
        'parking/espacios/form.html',
        {'form': form}
    )


def eliminar_espacio(request, id):

    espacio = get_object_or_404(Espacio, id=id)

    espacio.delete()

    return redirect('espacios')

def lista_tarifas(request):

    tarifas = Tarifa.objects.all()

    return render(
        request,
        'parking/tarifas/lista.html',
        {'tarifas': tarifas}
    )


def crear_tarifa(request):

    if request.method == 'POST':

        form = TarifaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tarifas')

    else:
        form = TarifaForm()

    return render(
        request,
        'parking/tarifas/form.html',
        {'form': form}
    )


def editar_tarifa(request, id):

    tarifa = get_object_or_404(Tarifa, id=id)

    if request.method == 'POST':

        form = TarifaForm(
            request.POST,
            instance=tarifa
        )

        if form.is_valid():
            form.save()
            return redirect('tarifas')

    else:
        form = TarifaForm(instance=tarifa)

    return render(
        request,
        'parking/tarifas/form.html',
        {'form': form}
    )


def eliminar_tarifa(request, id):

    tarifa = get_object_or_404(Tarifa, id=id)

    tarifa.delete()

    return redirect('tarifas')