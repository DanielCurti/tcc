# Generated by Django 2.2.4 on 2019-09-17 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('rua', models.CharField(max_length=100)),
                ('complemento', models.CharField(default='.', max_length=50)),
                ('valor', models.FloatField()),
                ('ativo', models.BooleanField(default=True)),
                ('modo', models.CharField(max_length=1)),
                ('abre', models.TimeField(max_length=5)),
                ('fecha', models.TimeField(max_length=5)),
                ('segunda', models.BooleanField(default=False)),
                ('terca', models.BooleanField(default=False)),
                ('quarta', models.BooleanField(default=False)),
                ('quinta', models.BooleanField(default=False)),
                ('sexta', models.BooleanField(default=False)),
                ('sabado', models.BooleanField(default=False)),
                ('domingo', models.BooleanField(default=False)),
                ('lat', models.CharField(default='-27.3667', max_length=100)),
                ('lng', models.CharField(default='-53.000', max_length=100)),
                ('avaliacao', models.IntegerField(default=-1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(default=0)),
                ('horaEntrada', models.DateTimeField()),
                ('horaSaida', models.DateTimeField()),
                ('avaliacaoDono', models.IntegerField(default=-1)),
                ('avaliacaolocador', models.IntegerField(default=-1)),
                ('alugador', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='alugadorReserva', to=settings.AUTH_USER_MODEL)),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='painel.Vagas')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, default='imagens/sem_foto.jpg', upload_to='usuarios')),
                ('saldo', models.FloatField(default=0)),
                ('avaliacao', models.IntegerField(default=-1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, default='imagens/sem_foto.jpg', upload_to='vagas')),
                ('descricao', models.CharField(default=0, max_length=100)),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='painel.Vagas')),
            ],
        ),
    ]
