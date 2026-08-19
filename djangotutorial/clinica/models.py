from django.db import models
from datetime import date, timedelta

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

class Medicamento(models.Model):
#    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    nome = models.CharField('Nome do Medicamento', max_length=100)
    dosagem = models.CharField('Dosagem', max_length=50)
    frequencia = models.CharField('Frequência', max_length=50)
    data_inicio = models.DateField('Data de Início')
    duracao_dias = models.IntegerField('Duração em Dias')

    @property
    def calcular_data_fim(self):
        if self.data_inicio and self.duracao_dias:
            return self.data_inicio + timedelta(days=self.duracao_dias)
        return None

    @property
    def verificar_status_tratamento(self):
        data_fim = self.calcular_data_fim
        if data_fim:
            hoje = date.today()
            if hoje > data_fim:
                return 'Concluído'
            return 'Em andamento'
        return 'Indefinido'

    def __str__(self):
        return self.nome

class Exame(models.Model):
#    pet = models.ForeignKey('Pet', on_delete=models.CASCADE)

# Exame pode ou não estar vinculado a uma consulta
    consulta = models.ForeignKey('Consulta',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    nome = models.CharField('Nome do Exame', max_length=100)
    data_realizacao = models.DateField('Data de Realização')
    resultado = models.TextField('Resultado', blank=True)
    observacoes = models.TextField('Observações', blank=True)

    def anexar_resultado(self, novo_resultado):
        self.resultado = novo_resultado
        self.save()

    def __str__(self):
        return self.nome    