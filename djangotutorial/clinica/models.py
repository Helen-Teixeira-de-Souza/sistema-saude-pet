from django.db import models
from datetime import date

class Consulta(models.Model):
    data = models.DateField('Data da Consulta')
    profissional = models.CharField('Profissional Responsável', max_length=150)
    diagnostico = models.TextField('Diagnóstico')
    observacoes = models.TextField('Observações', blank=True, null=True)

    def __str__(self):
        return f"Consulta - {self.data}"


class Vacina(models.Model):
    nome = models.CharField('Nome da Vacina', max_length=100)
    data_aplicacao = models.DateField('Data de Aplicação')
    data_reforco = models.DateField('Data de Reforço')

    @property
    def status_alerta(self):
        hoje = date.today()
        dias_para_reforco = (self.data_reforco - hoje).days
        if dias_para_reforco < 0:
            return 'vencida'
        elif dias_para_reforco <= 30:
            return 'proxima'
        return 'em_dia'

    def __str__(self):
        return f"Vacina: {self.nome}"


class Cirurgia(models.Model):
    data = models.DateField('Data da Cirurgia')
    profissional = models.CharField('Profissional Responsável', max_length=150)
    local = models.CharField('Local da Cirurgia', max_length=150)
    procedimento = models.CharField('Procedimento', max_length=200)
    cuidados_pos_operatorios = models.TextField('Cuidados Pós-Operatórios')

    def __str__(self):
        return f"Cirurgia: {self.procedimento}"