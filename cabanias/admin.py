from django.contrib import admin
from .models import Cabania, Reserva, Caracteristica
# Register your models here.
class ReservaAdmin(admin.ModelAdmin):
    search_fields = ["cabania",]
    list_display = ("cabania__id","cabania", "fecha_ingreso", "fecha_salida", "fecha_solicitud")
    class Meta:
        fields = "__all__"


class CabaniaAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)
    list_display = ("nombre", "descripcion", "capacidad_personas")


class CaracteristicaAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)


admin.site.register(Cabania, CabaniaAdmin)
admin.site.register(Caracteristica, CaracteristicaAdmin)
admin.site.register(Reserva, ReservaAdmin)