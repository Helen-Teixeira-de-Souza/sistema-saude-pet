from django.db import models
from pet.models import Pet
from profissional.models import Profissional


class Consulta(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='consultas', verbose_name='Pet')
    profissional = models.ForeignKey(
        Profissional, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='consultas',
        verbose_name='Profissional'
    )
    data = models.DateField('Data da Consulta')
    diagnostico = models.TextField('Diagnóstico')
    observacoes = models.TextField('Observações', blank=True, default='')

    class Meta:
        ordering = ['-data']
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return f"Consulta de {self.pet.nome} em {self.data.strftime('%d/%m/%Y')}"