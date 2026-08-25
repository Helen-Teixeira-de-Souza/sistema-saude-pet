from django.db import models
from datetime import date, timedelta
from tutor.models import Tutor  # Importa o model Tutor


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


class Consulta(models.Model):
    pet = models.ForeignKey(
        Pet, 
        on_delete=models.CASCADE, 
        related_name='consultas',
        verbose_name='Pet'
    )
    data = models.DateField('Data da Consulta')
    profissional = models.CharField('Profissional Responsável', max_length=150)
    diagnostico = models.TextField('Diagnóstico')
    observacoes = models.TextField('Observações', blank=True, null=True)

    class Meta:
        ordering = ['-data']
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return f"Consulta de {self.pet.nome} em {self.data.strftime('%d/%m/%Y')}"


class Vacina(models.Model):
    pet = models.ForeignKey(
        Pet, 
        on_delete=models.CASCADE, 
        related_name='vacinas',
        verbose_name='Pet'
    )
    nome = models.CharField('Nome da Vacina', max_length=100)
    data_aplicacao = models.DateField('Data de Aplicação')
    data_reforco = models.DateField('Data de Reforço')

    @property
    def verificar_reforco(self):
        hoje = date.today()
        dias_para_reforco = (self.data_reforco - hoje).days
        if dias_para_reforco < 0:
            return 'vencida'
        elif dias_para_reforco <= 30:
            return 'proxima'
        return 'em_dia'

    class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'

    def __str__(self):
        return f"Vacina {self.nome} - Pet: {self.pet.nome}"


class Exame(models.Model):
    pet = models.ForeignKey(
        Pet, 
        on_delete=models.CASCADE, 
        related_name='exames',
        verbose_name='Pet'
    )
    nome = models.CharField('Nome do Exame', max_length=100)
    data_realizacao = models.DateField('Data de Realização')
    veterinario = models.CharField('Veterinário', max_length=150)
    resultado = models.TextField('Resultado', blank=True, null=True)
    observacoes = models.TextField('Observações', blank=True, null=True)

    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'

    def __str__(self):
        return f"Exame {self.nome} - Pet: {self.pet.nome}"


class Medicamento(models.Model):
    pet = models.ForeignKey(
        Pet, 
        on_delete=models.CASCADE, 
        related_name='medicamentos',
        verbose_name='Pet'
    )
    nome = models.CharField('Nome do Medicamento', max_length=100)
    dosagem = models.CharField('Dosagem', max_length=50)
    frequencia = models.CharField('Frequência', max_length=50)
    data_inicio = models.DateField('Data de Início')
    data_fim = models.DateField('Data do Fim')

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'

    def __str__(self):
        return f"Medicamento {self.nome} - Pet: {self.pet.nome}"


class Cirurgia(models.Model):
    pet = models.ForeignKey(
        Pet, 
        on_delete=models.CASCADE, 
        related_name='cirurgias',
        verbose_name='Pet'
    )
    data = models.DateField('Data da Cirurgia')
    profissional = models.CharField('Profissional Responsável', max_length=150)
    local = models.CharField('Local da Cirurgia', max_length=150)
    procedimento = models.CharField('Procedimento', max_length=200)
    cuidados_pos_operatorios = models.TextField('Cuidados Pós-Operatórios')

    class Meta:
        verbose_name = 'Cirurgia'
        verbose_name_plural = 'Cirurgias'

    def __str__(self):
        return f"Cirurgia {self.procedimento} - Pet: {self.pet.nome}"


class AvisoVacinacao(models.Model):
    pet = models.ForeignKey(
        Pet, 
        on_delete=models.CASCADE, 
        related_name='avisos_vacina',
        verbose_name='Pet'
    )
    data_aviso = models.DateField('Data do Aviso')
    status = models.CharField('Status', max_length=50)
    mensagem = models.TextField('Mensagem')

    class Meta:
        verbose_name = 'Aviso de Vacinação'
        verbose_name_plural = 'Avisos de Vacinação'

    def __str__(self):
        return f"Aviso para {self.pet.nome} - {self.data_aviso.strftime('%d/%m/%Y')}"