# review later

from django import forms
from .models import Exame

class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ['pet', 'consulta', 'nome', 'data_realizacao', 'resultado', 'observacoes']
        widgets = {
            'pet': forms.Select(attrs={'class': 'form-control'}),
            'consulta': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Hemograma, Raio-X'}),
            'data_realizacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'resultado': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
        labels = {
            'pet': 'Pet (Paciente)',
            'consulta': 'Consulta Relacionada (Opcional)',
            'nome': 'Nome do Exame',
            'data_realizacao': 'Data de Realização',
            'resultado': 'Resultado / Laudo',
            'observacoes': 'Observações',
        }