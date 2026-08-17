from django.contrib import admin
from .models import Cabania, Reserva, Caracteristica
# Register your models here.
class ReservaAdmin(admin.ModelAdmin):
    search_fields = ["cabania",]
    list_display = ("cabania__id","cabania", "fecha_ingreso", "fecha_salida", "fecha_solicitud")
    class Meta:
        fields = "__all__"


admin.site.register(Cabania)
admin.site.register(Caracteristica)
admin.site.register(Reserva, ReservaAdmin)