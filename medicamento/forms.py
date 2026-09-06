from django import forms
from .models import Medicamento


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['pet', 'consulta', 'nome', 'dosagem', 'frequencia', 'data_inicio', 'duracao_dias']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
        }
