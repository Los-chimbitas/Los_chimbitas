from django import forms
from .models import Oferta

class VariableForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = [
            'ofertap',
        ]
        labels = {
            'ofertap': 'Ofertap',
        }