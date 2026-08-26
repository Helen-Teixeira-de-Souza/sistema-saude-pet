from django.db import models
from pet.models import Pet
from profissional.models import Profissional

class Cirurgia(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='cirurgias', verbose_name='Pet')
    profissional = models.ForeignKey(
        Profissional, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='cirurgias',
        verbose_name='Profissional Responsável'
    )
    data = models.DateField('Data da Cirurgia')
    local = models.CharField('Local da Cirurgia', max_length=150)
    procedimento = models.CharField('Procedimento', max_length=200)
    cuidados_pos_operatorios = models.TextField('Cuidados Pós-Operatórios', blank=True, default='')

    class Meta:
        verbose_name = 'Cirurgia'
        verbose_name_plural = 'Cirurgias'

    def __str__(self):
        return f"Cirurgia {self.procedimento} - Pet: {self.pet.nome}"