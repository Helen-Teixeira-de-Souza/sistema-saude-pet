from datetime import date
from django.db import models
from pet.models import Pet
from vacina.models import Vacina

class Vacinacao(models.Model):
    """Registro da aplicação da vacina no Pet"""
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='vacinacoes', verbose_name='Pet')
    vacina = models.ForeignKey(Vacina, on_delete=models.PROTECT, related_name='aplicacoes', verbose_name='Vacina')
    data_aplicacao = models.DateField('Data de Aplicação')
    proxima_dose = models.DateField('Próxima Dose / Reforço', null=True, blank=True)
    dose_atual = models.PositiveIntegerField('Dose Atual', default=1)
    observacoes = models.TextField('Observações', blank=True, default='')

    class Meta:
        verbose_name = 'Vacinação'
        verbose_name_plural = 'Vacinações'

    @property
    def status_alerta(self):
        if not self.proxima_dose:
            return 'em_dia'
        hoje = date.today()
        dias = (self.proxima_dose - hoje).days
        if dias < 0:
            return 'vencida'
        elif dias <= 30:
            return 'proxima'
        return 'em_dia'

    def __str__(self):
        return f"{self.vacina.nome} ({self.dose_atual}ª dose) - Pet: {self.pet.nome}"

class AvisoVacinacao(models.Model):
    vacinacao = models.ForeignKey(
        Vacinacao, 
        on_delete=models.CASCADE, 
        related_name='avisos',
        verbose_name='Vacinação',
        null=True,
        blank=True
    )
    data_aviso = models.DateField('Data do Aviso')
    status = models.CharField('Status', max_length=50, default='Pendente')
    mensagem = models.TextField('Mensagem')

    class Meta:
        verbose_name = 'Aviso de Vacinação'
        verbose_name_plural = 'Avisos de Vacinação'

    def __str__(self):
        pet_nome = self.vacinacao.pet.nome if self.vacinacao else 'Sem Pet'
        return f"Aviso para {pet_nome} - {self.data_aviso.strftime('%d/%m/%Y')}"