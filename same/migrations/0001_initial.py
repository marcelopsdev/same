# Generated by Django 5.1.3 on 2025-01-16 13:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArquivamentoSame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(auto_now_add=True)),
                ('data_atendimento', models.DateField(blank=True, null=True)),
                ('num_ficha_atendimento', models.CharField(blank=True, max_length=15, null=True)),
                ('num_prontuario', models.CharField(blank=True, max_length=15, null=True)),
                ('nome_paciente', models.CharField(blank=True, max_length=100, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('mes_faturamento', models.DateField(blank=True, null=True)),
                ('data_arquivamento', models.DateField(blank=True, null=True)),
                ('num_caixa_arquivo', models.CharField(blank=True, max_length=30, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('', ''), ('MASCULINO', 'MASCULINO'), ('FEMININO', 'FEMININO')], max_length=10, null=True)),
                ('raca_cor', models.CharField(blank=True, choices=[('', ''), ('BRANCA', 'BRANCA'), ('PRETA', 'PRETA'), ('PARDA', 'PARDA'), ('AMARELA', 'AMARELA'), ('INDIGENA', 'INDIGENA')], max_length=20, null=True)),
                ('municipio', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_prontuario', models.CharField(blank=True, choices=[('', ''), ('PRONTUARIOS FATURADOS', 'PRONTUARIOS FATURADOS'), ('PRONTUARIOS NAO FATURADOS', 'PRONTUARIOS NAO FATURADOS'), ('PRONTUARIOS MATERNIDADE', 'PRONTUARIOS MATERNIDADE'), ('FICHAS', 'FICHAS'), ('NAO FATURADOS', 'NAO FATURADOS'), ('NAO IDENTIFICADOS', 'NAO IDENTIFICADOS'), ('OPME', 'OPME')], max_length=100, null=True)),
                ('upload_prontuario', models.FileField(blank=True, null=True, upload_to='Prontuario')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
