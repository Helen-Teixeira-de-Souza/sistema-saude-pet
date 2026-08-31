from django.db import models
from django.utils import timezone
from datetime import timedelta, date
from pet.models import Pet
from consulta.models import Consulta


# Create your models here.
class Medicamento(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='medicamentos', verbose_name='Pet')
    consulta = models.ForeignKey(
        Consulta, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='medicamentos',
        verbose_name='Consulta de Prescrição'
    )
    nome = models.CharField('Nome do Medicamento', max_length=100)
    dosagem = models.CharField('Dosagem', max_length=50)
    frequencia = models.CharField('Frequência', max_length=50)
    data_inicio = models.DateField('Data de Início')
    duracao_dias = models.PositiveIntegerField('Duração (Dias)', default=1)

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'

    @property
    def data_fim(self):
        return self.data_inicio + timedelta(days=self.duracao_dias)

    @property
    def status_tratamento(self):
        hoje = date.today()
        return 'Concluído' if hoje > self.data_fim else 'Em andamento'

    def __str__(self):
        return f"{self.nome} - Pet: {self.pet.nome}"
