# Generated by Django 4.2.20 on 2025-05-03 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(verbose_name='Data e Hora')),
                ('status', models.CharField(choices=[('SC', 'Agendada'), ('CF', 'Confirmada'), ('CA', 'Cancelada'), ('CO', 'Concluída')], default='SC', max_length=2, verbose_name='Status')),
                ('reason', models.TextField(blank=True, null=True, verbose_name='Motivo da Consulta')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
                'ordering': ['date_time'],
            },
        ),
    ]
