from django import forms
from .models import Vehiculo


class VehiculoFormulario(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('usuario', 'vin', 'patente',
                  'año', 'fecha', 'marca', 'modelo')
