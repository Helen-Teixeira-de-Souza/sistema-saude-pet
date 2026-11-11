"""Regras de visibilidade: a equipe (staff) vê tudo; o tutor vê apenas os dados dos seus pets."""
from .models import Pet


def e_equipe(user):
    return user.is_staff or user.is_superuser


def pets_visiveis(user):
    qs = Pet.objects.all()
    if e_equipe(user):
        return qs
    return qs.filter(tutor__pk=user.pk)


def filtrar_por_tutor(queryset, user):
    """Filtra qualquer queryset que tenha o campo `pet` (consulta, exame, etc.)."""
    if e_equipe(user):
        return queryset
    return queryset.filter(pet__tutor__pk=user.pk)


def restringir_form(form, user):
    """Limita os <select> de pet/consulta aos registros do próprio tutor."""
    if e_equipe(user):
        return form
    if 'pet' in form.fields:
        form.fields['pet'].queryset = pets_visiveis(user)
    if 'consulta' in form.fields:
        form.fields['consulta'].queryset = form.fields['consulta'].queryset.filter(pet__tutor__pk=user.pk)
    return form


from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def permissao_ou_tutor(perm):
    """Substitui o permission_required nas telas clínicas.

    - Tutor (não-staff) logado: liberado. Os dados dele já ficam limitados aos próprios pets
      por filtrar_por_tutor/restringir_form, então não depende de grupo nem de migrate.
    - Equipe (staff/superusuário): precisa da permissão `perm` (superusuário sempre tem).
    - Sem permissão: erro 403 em vez de mandar para o login (evita o "loop" de login).
    """
    def decorador(view):
        @wraps(view)
        @login_required(login_url='/login/')
        def wrapper(request, *args, **kwargs):
            user = request.user
            if e_equipe(user) and not user.has_perm(perm):
                raise PermissionDenied
            return view(request, *args, **kwargs)
        return wrapper
    return decorador