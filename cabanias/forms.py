import datetime
from datetime import date

from django import forms
from django.forms import DateInput

from .models import Reserva

class ReservaForm(forms.ModelForm):
    def __init__(self, *args, cabania=None, **kwargs):
        self.cabania = cabania
        super().__init__(*args, **kwargs)

    class Meta:
        model = Reserva
        fields = ["nombre_cliente", "email_cliente", "telefono_cliente", "fecha_ingreso", "fecha_salida"]
        widgets = {
            "nombre_cliente": forms.TextInput(attrs={'class': 'form-control'}),
            "email_cliente": forms.EmailInput(attrs={'class': 'form-control'}),
            "telefono_cliente": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha_ingreso": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "fecha_salida": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean_fecha_ingreso(self):
        fecha_ingreso = self.cleaned_data.get("fecha_ingreso")
        if fecha_ingreso and fecha_ingreso < datetime.date.today():
            raise forms.ValidationError("La fecha de ingreso no puede ser menor a la fecha actual.")
        return fecha_ingreso

    def clean_fecha_salida(self):
        fecha_salida = self.cleaned_data.get("fecha_salida")
        if fecha_salida and fecha_salida < datetime.date.today():
            raise forms.ValidationError("La fecha de salida no puede ser menor a la fecha actual.")
        return fecha_salida

    def clean(self):
        cleaned_data = super().clean()
        fecha_ingreso = cleaned_data.get("fecha_ingreso")
        fecha_salida = cleaned_data.get("fecha_salida")

        if fecha_ingreso and fecha_salida:
            if fecha_salida < fecha_ingreso:
                raise forms.ValidationError("La fecha de salida no puede ser menor a la fecha de ingreso.")

            # Validar disponibilidad en la base de datos
            if self.cabania:
                solapadas = Reserva.objects.filter(
                    cabania=self.cabania,
                    fecha_ingreso__lt=fecha_salida,
                    fecha_salida__gt=fecha_ingreso,
                )

                # Si es una edición de reserva, excluir la instancia actual
                if self.instance.pk:
                    solapadas = solapadas.exclude(pk=self.instance.pk)

                if solapadas.exists():
                    raise forms.ValidationError("La cabaña no está disponible en el rango de fechas seleccionado.")

        return cleaned_data