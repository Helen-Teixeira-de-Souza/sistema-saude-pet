from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import TutorCreationForm
from .models import Tutor


@admin.register(Tutor)
class TutorAdmin(UserAdmin):
    """Usa o UserAdmin para que a senha seja gravada com hash.
    (Com o ModelAdmin simples a senha era salva em texto puro e o login nunca funcionava.)"""
    add_form = TutorCreationForm
    list_display = ('username', 'nome', 'email', 'telefone', 'is_active')
    search_fields = ('username', 'nome', 'email')
    fieldsets = UserAdmin.fieldsets + (('Dados do tutor', {'fields': ('nome', 'telefone')}),)
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'nome', 'email', 'telefone', 'password1', 'password2')}),
    )
