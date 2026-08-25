from datetime import date, timedelta
from django.db import models
from tutor.models import Tutor


class Profissional(models.Model):
    nome = models.CharField('Nome', max_length=150)
    especialidade = models.CharField('Especialidade', max_length=100)
    telefone = models.CharField('Telefone', max_length=20, blank=True, default='')

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"

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

    @property
    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - (
            (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )

    def __str__(self):
        return f"{self.nome} ({self.especie}) - Tutor: {self.tutor.nome}"


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


class Vacinacao(models.Model):
    """Registro da aplicação da vacina no Pet"""
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='vacinacoes', verbose_name='Pet')
    vacina = models.ForeignKey(Vacina, on_delete=models.PROTECT, related_name='aplicacoes', verbose_name='Vacina')
    data_aplicacao = models.DateField('Data de Aplicação')
    proxima_dose = models.DateField('Próxima Dose / Reforço', null=True, blank=True)
    dose_atual = models.PositiveIntegerField('Dose Atual', default=1)
    observacoes = models.TextField('Observações', blank=True, default='')

    class Meta:
        verbose_name = 'Vacinação'
        verbose_name_plural = 'Vacinações'

    @property
    def status_alerta(self):
        if not self.proxima_dose:
            return 'em_dia'
        hoje = date.today()
        dias = (self.proxima_dose - hoje).days
        if dias < 0:
            return 'vencida'
        elif dias <= 30:
            return 'proxima'
        return 'em_dia'

    def __str__(self):
        return f"{self.vacina.nome} ({self.dose_atual}ª dose) - Pet: {self.pet.nome}"


class AvisoVacinacao(models.Model):
    vacinacao = models.ForeignKey(
        Vacinacao, 
        on_delete=models.CASCADE, 
        related_name='avisos',
        verbose_name='Vacinação',
        null=True,
        blank=True
    )
    data_aviso = models.DateField('Data do Aviso')
    status = models.CharField('Status', max_length=50, default='Pendente')
    mensagem = models.TextField('Mensagem')

    class Meta:
        verbose_name = 'Aviso de Vacinação'
        verbose_name_plural = 'Avisos de Vacinação'

    def __str__(self):
        pet_nome = self.vacinacao.pet.nome if self.vacinacao else 'Sem Pet'
        return f"Aviso para {pet_nome} - {self.data_aviso.strftime('%d/%m/%Y')}"


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


class Exame(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='exames', verbose_name='Pet')
    consulta = models.ForeignKey(
        Consulta, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='exames',
        verbose_name='Consulta de Origem'
    )
    nome = models.CharField('Nome do Exame', max_length=100)
    data_realizacao = models.DateField('Data de Realização')
    resultado = models.TextField('Resultado', blank=True, default='')
    observacoes = models.TextField('Observações', blank=True, default='')

    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'

    def __str__(self):
        return f"Exame {self.nome} - Pet: {self.pet.nome}"


class Medicamento(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='medicamentos', verbose_name='Pet')
    consulta = models.ForeignKey(
        Consulta, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='medicamentos',
        verbose_name='Consulta de Prescrição'
    )
    nome = models.CharField('Nome do Medicamento', max_length=100)
    dosagem = models.CharField('Dosagem', max_length=50)
    frequencia = models.CharField('Frequência', max_length=50)
    data_inicio = models.DateField('Data de Início')
    duracao_dias = models.PositiveIntegerField('Duração (Dias)', default=1)

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'

    @property
    def data_fim(self):
        return self.data_inicio + timedelta(days=self.duracao_dias)

    @property
    def status_tratamento(self):
        hoje = date.today()
        return 'Concluído' if hoje > self.data_fim else 'Em andamento'

    def __str__(self):
        return f"{self.nome} - Pet: {self.pet.nome}"


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