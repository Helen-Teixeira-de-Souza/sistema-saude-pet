from django import forms
from .models import Vacina


class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = ['nome', 'quantidade_dose', 'descricao', 'intervalo_doses_dias']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs.setdefault('class', 'form-control')
