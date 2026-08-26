from django.db import models

class Profissional(models.Model):
    nome = models.CharField('Nome', max_length=150)
    especialidade = models.CharField('Especialidade', max_length=100)
    telefone = models.CharField('Telefone', max_length=20, blank=True, default='')

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"