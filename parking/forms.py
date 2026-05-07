from django import forms
from .models import Cliente, Vehiculo, Espacio, Tarifa, Cobro


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'


class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = '__all__'


class EspacioForm(forms.ModelForm):

    class Meta:
        model = Espacio
        fields = '__all__'


class TarifaForm(forms.ModelForm):

    class Meta:
        model = Tarifa
        fields = '__all__'


class CobroForm(forms.ModelForm):

    class Meta:
        model = Cobro
        fields = '__all__'
