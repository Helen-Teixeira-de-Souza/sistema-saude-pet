from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Tutor


class TutorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Tutor
        fields = ('username', 'email', 'nome', 'telefone')
        labels = {
            'username': 'Nome de usuário',
            'email': 'E-mail',
            'password1': 'Senha',
            'password2': 'Confirmação de senha',
        }


class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['username', 'nome', 'email', 'telefone']