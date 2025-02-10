from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from apps.states_and_cities.models import City
import datetime

SEXO = [
    ('', ''),
    ('MASCULINO', 'MASCULINO'),
    ('FEMININO', 'FEMININO'),
]

TIPO_DE_PRONTUARIO = [
    ('', ''),
    ('PRONTUARIOS FATURADOS', 'PRONTUARIOS FATURADOS'),
    ('PRONTUARIOS NAO FATURADOS', 'PRONTUARIOS NAO FATURADOS'),
    ('PRONTUARIOS MATERNIDADE', 'PRONTUARIOS MATERNIDADE'),
    ('FICHAS', 'FICHAS'),
    ('NAO FATURADOS', 'NAO FATURADOS'),
    ('NAO IDENTIFICADOS', 'NAO IDENTIFICADOS'),
    ('OPME', 'OPME'),
]

RACA_COR = [
    ('', ''),
    ('BRANCA', 'BRANCA'),
    ('PRETA', 'PRETA'),
    ('PARDA', 'PARDA'),
    ('AMARELA', 'AMARELA'),
    ('INDIGENA', 'INDIGENA'),
]
class ArquivamentoSame(models.Model):
    created_in = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  
    data_atendimento = models.DateField(default=datetime.date.today)
    num_ficha_atendimento = models.CharField(max_length=15, null=True, blank=True)
    num_prontuario = models.CharField(max_length=15)
    nome_paciente = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    mes_faturamento = models.DateField(null=True, blank=True) #Anterior a apresentação?
    data_arquivamento = models.DateField(default=datetime.date.today, null=True, blank=True)
    num_caixa_arquivo = models.CharField(max_length=30)
    sexo = models.CharField(choices=SEXO ,max_length=10, null=True, blank=True)
    raca_cor = models.CharField(choices=RACA_COR, max_length=20, null=True, blank=True)
    municipio = models.CharField(max_length=100, null=True, blank=True)
    tipo_prontuario = models.CharField(choices=TIPO_DE_PRONTUARIO, max_length=100, null=True, blank=True)
    upload_prontuario = models.FileField(upload_to=f'{num_prontuario} {nome_paciente}')

    def get_absolute_url(self):
        return reverse('same')

    def __str__(self):
        return self.nome_paciente


