from django import forms
from .models import Pet, Vacina, Consulta, Exame, Medicamento, Cirurgia

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['tutor', 'nome', 'especie', 'raca', 'sexo', 'data_nascimento']
        widgets = {'data_nascimento': forms.DateInput(attrs={'type': 'date'})}

class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = ['nome', 'data_aplicacao', 'data_reforco']
        widgets = {
            'data_aplicacao': forms.DateInput(attrs={'type': 'date'}),
            'data_reforco': forms.DateInput(attrs={'type': 'date'}),
        }

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['data', 'profissional', 'diagnostico', 'observacoes']
        widgets = {'data': forms.DateInput(attrs={'type': 'date'})}

class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ['nome', 'data_realizacao', 'veterinario', 'resultado', 'observacoes']
        widgets = {'data_realizacao': forms.DateInput(attrs={'type': 'date'})}

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nome', 'dosagem', 'frequencia', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }

class CirurgiaForm(forms.ModelForm):
    class Meta:
        model = Cirurgia
        fields = ['data', 'profissional', 'local', 'procedimento', 'cuidados_pos_operatorios']
        widgets = {'data': forms.DateInput(attrs={'type': 'date'})}