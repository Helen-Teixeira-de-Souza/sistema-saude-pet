from django.db import models

# Create your models here.
class Vacina(models.Model):
    """Catálogo/Cadastro das Vacinas"""
    nome = models.CharField('Nome da Vacina', max_length=100)
    quantidade_dose = models.PositiveIntegerField('Quantidade de Doses', default=1)
    descricao = models.TextField('Descrição', blank=True, default='')
    intervalo_doses_dias = models.PositiveIntegerField('Intervalo entre Doses (Dias)', default=0)

    class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'

    def __str__(self):
        return self.nome