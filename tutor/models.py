from django.db import models
from django.contrib.auth.models import User


class Tutor(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='tutor',
        null=True, 
        blank=True
    )
    nome = models.CharField('Nome', max_length=150)
    telefone = models.CharField('Telefone', max_length=20, blank=True, default='')

    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'
        ordering = ['nome']

    def __str__(self):
        return self.nome