from django import forms
from .models import Cirurgia


class CirurgiaForm(forms.ModelForm):
    class Meta:
        model = Cirurgia
        fields = ['pet', 'profissional', 'data', 'local', 'procedimento', 'cuidados_pos_operatorios']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'cuidados_pos_operatorios': forms.Textarea(attrs={'rows': 3}),
        }
