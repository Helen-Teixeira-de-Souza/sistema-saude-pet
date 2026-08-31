from django.db import models
from pet.models import Pet
from consulta.models import Consulta


class Exame(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='exames', verbose_name='Pet')
    consulta = models.ForeignKey(
        Consulta, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='exames',
        verbose_name='Consulta de Origem'
    )
    nome = models.CharField('Nome do Exame', max_length=100)
    data_realizacao = models.DateField('Data de Realização')
    resultado = models.TextField('Resultado', blank=True, default='')
    observacoes = models.TextField('Observações', blank=True, default='')

    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'

    def __str__(self):
        return f"Exame {self.nome} - Pet: {self.pet.nome}"