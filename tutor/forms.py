from django import forms
from .models import Tutor

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['username', 'first_name', 'last_name', 'email', 'telefone']