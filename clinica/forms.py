from django import forms
from .models import Consulta, Vacina, Cirurgia

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['tutor', 'data', 'profissional', 'diagnostico', 'observacoes']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'diagnostico': forms.Textarea(attrs={'rows': 3}),
            'observacoes': forms.Textarea(attrs={'rows': 2}),
        }

class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = ['nome', 'data_aplicacao', 'data_reforco']

class CirurgiaForm(forms.ModelForm):
    class Meta:
        model = Cirurgia
        fields = ['data', 'profissional', 'local', 'procedimento', 'cuidados_pos_operatorios']