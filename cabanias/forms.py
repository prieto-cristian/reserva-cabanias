from django import forms

from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["nombre_cliente", "email_cliente", "telefono_cliente",
                  "fecha_ingreso", "fecha_salida"]
        widgets = {
            "nombre_cliente": forms.TextInput(attrs={
                'class': 'form-control',
            }),
            "email_cliente": forms.EmailInput(attrs={
                'class': 'form-control',
            }),
            "telefono_cliente": forms.TextInput(attrs={
                'class': 'form-control',
            }),
            "fecha_ingreso": forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            "fecha_salida": forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            })
        }