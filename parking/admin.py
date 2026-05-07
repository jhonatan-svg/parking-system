from django.contrib import admin
from .models import Cliente, Vehiculo, Espacio, Tarifa, Cobro

admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Espacio)
admin.site.register(Tarifa)
admin.site.register(Cobro)
