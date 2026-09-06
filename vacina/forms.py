from django import forms
from .models import Vacina


class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = ['nome', 'quantidade_dose', 'descricao', 'intervalo_doses_dias']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }
