from django.db import models
from django.contrib.auth.models import User


class Tutor(User):
    nome = models.CharField('Nome', max_length=100, blank=True, default='')
    telefone = models.CharField('Telefone', max_length=20, blank=True, default='')

    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'

    def __str__(self):
        return self.nome