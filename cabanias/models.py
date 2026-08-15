from django.db import models
from django.db.models import (TextField, PositiveIntegerField, CharField,
                              DecimalField, BooleanField, ManyToManyField,
                              ForeignKey, CASCADE, EmailField, DateField,
                              DateTimeField)


# Create your models here.
class Caracteristica(models.Model):
    nombre = CharField(max_length=100)


class Cabania(models.Model):
    nombre = CharField(max_length=254)
    descripcion = TextField()
    capacidad_personas = PositiveIntegerField(default=2)
    precio_por_noche = DecimalField(max_digits=10, decimal_places=2)
    disponible = BooleanField(default=True)
    caracteristicas = ManyToManyField(Caracteristica)


class Reserva(models.Model):
    cabania = ForeignKey(Cabania, on_delete=CASCADE, related_name="reservas")
    nombre_clientes = CharField(max_length=50)
    email_cliente = EmailField()
    telefono_cliente = CharField(max_length=30)
    fecha_ingreso = DateField()
    fecha_salida = DateField()
    fecha_solicitud = DateTimeField(auto_now_add=True)