from django.apps import AppConfig
from django.db.models.signals import post_migrate, post_save

GRUPO_TUTORES = 'Tutores'

# Apps cujos registros o tutor pode cadastrar/editar/excluir (sempre restrito aos seus pets).
# Para tirar uma permissão do tutor, basta remover o app/ação daqui e rodar "migrate".
APPS_DO_TUTOR = ['consulta', 'exame', 'medicamento', 'cirurgia', 'vacinacao']
ACOES = ['add', 'change', 'delete', 'view']


def garantir_grupo_tutores(sender=None, **kwargs):
    """Cria o grupo 'Tutores' com as permissões necessárias e coloca nele os tutores existentes."""
    from django.apps import apps as django_apps
    from django.contrib.auth.management import create_permissions
    from django.contrib.auth.models import Group, Permission
    from .models import Tutor

    # As permissões de cada app só são criadas no post_migrate do próprio app,
    # que pode rodar depois deste; criamos aqui para não depender da ordem.
    using = kwargs.get('using', 'default')
    for label in APPS_DO_TUTOR:
        create_permissions(django_apps.get_app_config(label), verbosity=0, using=using)

    grupo, _ = Group.objects.using(using).get_or_create(name=GRUPO_TUTORES)
    codenames = [f'{acao}_{app}' for app in APPS_DO_TUTOR for acao in ACOES]
    perms = Permission.objects.using(using).filter(
        codename__in=codenames, content_type__app_label__in=APPS_DO_TUTOR
    )
    grupo.permissions.set(perms)

    for tutor in Tutor.objects.using(using).all():
        tutor.groups.add(grupo)


def adicionar_tutor_ao_grupo(sender, instance, created, **kwargs):
    """Todo tutor novo (cadastro público ou pelo admin) entra no grupo 'Tutores'."""
    if created:
        from django.contrib.auth.models import Group
        grupo, _ = Group.objects.get_or_create(name=GRUPO_TUTORES)
        instance.groups.add(grupo)


class TutorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tutor'

    def ready(self):
        from .models import Tutor
        post_migrate.connect(garantir_grupo_tutores, dispatch_uid='tutor_garantir_grupo')
        post_save.connect(adicionar_tutor_ao_grupo, sender=Tutor, dispatch_uid='tutor_add_grupo')
