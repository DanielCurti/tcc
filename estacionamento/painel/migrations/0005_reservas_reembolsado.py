# Generated by Django 2.2.4 on 2019-10-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0004_perfil_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='reembolsado',
            field=models.BooleanField(default=False),
        ),
    ]