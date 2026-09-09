from django import forms
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['pet', 'consulta', 'nome', 'dosagem', 'frequencia', 'duracao_dias', 'data_inicio']
        widgets = {
            'pet': forms.Select(attrs={'class': 'form-control'}),
            'consulta': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Amoxicilina'}),
            'dosagem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 10mg, 1 comprimido'}),
            'frequencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: A cada 12 horas'}),
            'duracao_dias': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 7'}),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'pet': 'Pet (Paciente)',
            'consulta': 'Consulta Relacionada (Opcional)',
            'nome': 'Nome do Medicamento',
            'dosagem': 'Dosagem',
            'frequencia': 'Frequência',
            'duracao_dias': 'Duração (dias)',
            'data_inicio': 'Data de Início',
        }