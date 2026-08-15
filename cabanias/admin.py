from django.contrib import admin
from .models import Cabania, Reserva, Caracteristica
# Register your models here.
admin.site.register(Cabania)
admin.site.register(Caracteristica)
admin.site.register(Reserva)