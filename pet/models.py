from datetime import date
from django.db import models
from tutor.models import Tutor

class Pet(models.Model):
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]

    tutor = models.ForeignKey(
        Tutor, 
        on_delete=models.CASCADE, 
        related_name='pets',
        verbose_name='Tutor'
    )
    nome = models.CharField('Nome', max_length=100)
    especie = models.CharField('Espécie', max_length=50)
    raca = models.CharField('Raça', max_length=50)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField('Data de Nascimento')

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    def __str__(self):
        return f"{self.nome} ({self.especie}) - Tutor: {self.tutor.nome}"