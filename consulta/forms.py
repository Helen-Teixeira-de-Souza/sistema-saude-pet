from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['pet', 'profissional', 'data', 'diagnostico', 'observacoes']
        widgets = {
            'pet': forms.Select(attrs={'class': 'form-select'}),
            'profissional': forms.Select(attrs={'class': 'form-select'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Informe o diagnóstico...'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observações adicionais da consulta...'}),
        }