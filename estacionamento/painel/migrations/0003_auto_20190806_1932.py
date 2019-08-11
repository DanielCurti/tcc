# Generated by Django 2.2.2 on 2019-08-06 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('painel', '0002_auto_20190804_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, default='imagens/sem_foto.jpg', upload_to='imagens')),
                ('saldo', models.FloatField(default=0)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='receber',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='vaga',
            name='numero',
        ),
        migrations.AddField(
            model_name='vaga',
            name='complemento',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='categoria',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='estado',
            field=models.CharField(max_length=2),
        ),
        migrations.DeleteModel(
            name='Foto',
        ),
        migrations.DeleteModel(
            name='Receber',
        ),
    ]
