from django import forms
from .models import Empleo
class EmpleoForm(forms.ModelForm):
    class Meta:
        model = Empleo
        fields = [
            'nombre',
            'oferente',
        ]

        labels = {
            'nombre': 'Nombre',
            'oferente': 'Oferente',
        }