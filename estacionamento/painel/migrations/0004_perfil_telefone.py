# Generated by Django 2.2.4 on 2019-10-24 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0003_auto_20191021_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='telefone',
            field=models.CharField(default='', max_length=11),
        ),
    ]
