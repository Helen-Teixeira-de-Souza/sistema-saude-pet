from django import forms
from django.contrib.auth.models import User
from .models import Tutor


class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['user', 'nome', 'telefone']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),
            'nome': forms.TextInput(attrs={'placeholder': 'Nome completo do tutor'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(00) 90000-0000'}),
        }


class TutorUserForm(forms.ModelForm):
    
    username = forms.CharField(label='Nome de Usuário', max_length=150)
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = Tutor
        fields = ['nome', 'telefone']

    def save(self, commit=True):
        tutor = super().save(commit=False)
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        tutor.user = user

        if commit:
            tutor.save()
        return tutor