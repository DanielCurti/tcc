# Generated by Django 2.2.4 on 2019-08-13 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0003_transacao_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='avaliacao',
            field=models.IntegerField(null=True),
        ),
    ]