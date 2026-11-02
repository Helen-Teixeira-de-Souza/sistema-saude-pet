from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import AvisoVacinacao, Vacinacao

# Quantos dias antes da próxima dose o aviso passa a ficar ativo
# (mesma janela de 30 dias usada em Vacinacao.status_alerta).
DIAS_ANTECEDENCIA_AVISO = 30


@receiver(post_save, sender=Vacinacao)
def gerar_aviso_vacinacao(sender, instance, **kwargs):
    """Cria (ou atualiza) o AvisoVacinacao sempre que uma Vacinacao é salva."""
    pendentes = instance.avisos.filter(status='Pendente')

    # Sem próxima dose não há o que avisar
    if not instance.proxima_dose:
        pendentes.delete()
        return

    mensagem = (
        f"A vacina {instance.vacina.nome} ({instance.dose_atual}ª dose) do pet "
        f"{instance.pet.nome} deve ser aplicada até "
        f"{instance.proxima_dose.strftime('%d/%m/%Y')}."
    )
    data_aviso = instance.proxima_dose - timedelta(days=DIAS_ANTECEDENCIA_AVISO)

    AvisoVacinacao.objects.update_or_create(
        vacinacao=instance,
        status='Pendente',
        defaults={'data_aviso': data_aviso, 'mensagem': mensagem},
    )
