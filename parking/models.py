from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.placa


class Espacio(models.Model):
    numero = models.IntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Espacio {self.numero}"


class Tarifa(models.Model):
    tipo_vehiculo = models.CharField(max_length=50)
    precio_hora = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.tipo_vehiculo


class Cobro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    tarifa = models.ForeignKey(Tarifa, on_delete=models.CASCADE)

    hora_entrada = models.DateTimeField()
    hora_salida = models.DateTimeField()

    total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Cobro {self.id}"
