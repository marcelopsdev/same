# Generated by Django 5.1.3 on 2025-01-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('same', '0004_alter_arquivamentosame_upload_prontuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivamentosame',
            name='upload_prontuario',
            field=models.FileField(upload_to='<django.db.models.fields.CharField> <django.db.models.fields.CharField>'),
        ),
    ]
