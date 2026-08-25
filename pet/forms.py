from django import forms
from .models import Pet, Profissional, Vacina, Vacinacao, Consulta, Exame, Medicamento, Cirurgia


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['tutor', 'nome', 'especie', 'raca', 'sexo', 'data_nascimento']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }


class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'especialidade', 'telefone']


class VacinaForm(forms.ModelForm):
    """Cadastro base/catálogo de vacinas"""
    class Meta:
        model = Vacina
        fields = ['nome', 'quantidade_dose', 'descricao', 'intervalo_doses_dias']


class VacinacaoForm(forms.ModelForm):
    """Registro de aplicação no Pet"""
    class Meta:
        model = Vacinacao
        fields = ['vacina', 'data_aplicacao', 'proxima_dose', 'dose_atual', 'observacoes']
        widgets = {
            'data_aplicacao': forms.DateInput(attrs={'type': 'date'}),
            'proxima_dose': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['profissional', 'data', 'diagnostico', 'observacoes']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'diagnostico': forms.Textarea(attrs={'rows': 3}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }


class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ['consulta', 'nome', 'data_realizacao', 'resultado', 'observacoes']
        widgets = {
            'data_realizacao': forms.DateInput(attrs={'type': 'date'}),
            'resultado': forms.Textarea(attrs={'rows': 3}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['consulta', 'nome', 'dosagem', 'frequencia', 'data_inicio', 'duracao_dias']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
        }


class CirurgiaForm(forms.ModelForm):
    class Meta:
        model = Cirurgia
        fields = ['profissional', 'data', 'local', 'procedimento', 'cuidados_pos_operatorios']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'cuidados_pos_operatorios': forms.Textarea(attrs={'rows': 3}),
        }