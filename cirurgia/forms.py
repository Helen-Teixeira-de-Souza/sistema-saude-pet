from django import forms
from .models import Cirurgia


class CirurgiaForm(forms.ModelForm):
    class Meta:
        model = Cirurgia
        fields = ['pet', 'profissional', 'data', 'local', 'procedimento', 'cuidados_pos_operatorios']
        widgets = {
            'data': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'cuidados_pos_operatorios': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs.setdefault('class', 'form-control')
