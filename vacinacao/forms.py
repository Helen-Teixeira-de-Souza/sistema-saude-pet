from django import forms
from .models import Vacinacao


class VacinacaoForm(forms.ModelForm):
    class Meta:
        model = Vacinacao
        fields = ['pet', 'vacina', 'data_aplicacao', 'proxima_dose', 'dose_atual', 'observacoes']
        widgets = {
            'data_aplicacao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'proxima_dose': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs.setdefault('class', 'form-control')
