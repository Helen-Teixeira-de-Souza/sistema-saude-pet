from django import forms
from .models import Vacinacao


class VacinacaoForm(forms.ModelForm):
    class Meta:
        model = Vacinacao
        fields = ['pet', 'vacina', 'data_aplicacao', 'proxima_dose', 'dose_atual', 'observacoes']
        widgets = {
            'data_aplicacao': forms.DateInput(attrs={'type': 'date'}),
            'proxima_dose': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
