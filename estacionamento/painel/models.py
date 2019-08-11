from django.db import models

class Perfil(models.Model):
	usuario = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	imagem = models.ImageField(blank=True, upload_to='usuarios', default='imagens/sem_foto.jpg')
	saldo = models.FloatField(default=0)


class Vagas(models.Model):
	usuario = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	estado = models.CharField(max_length=2)
	cidade = models.CharField(max_length=100)
	bairro = models.CharField(max_length=100)
	rua    = models.CharField(max_length=100)
	complemento = models.CharField(max_length=50, default='')
	valor  = models.FloatField()
	ativo = models.BooleanField(default=True)
	alugado = models.BooleanField(default=False)
	categoria = models.CharField(max_length=2)
	modo = models.CharField(max_length=1)
	abre = models.CharField(max_length=5)
	fecha = models.CharField(max_length=5)
	foto = models.ImageField(blank=True, upload_to='vagas', default='imagens/sem_foto.jpg')
	segunda =models.BooleanField(default=False)
	terca = models.BooleanField(default=False)
	quarta = models.BooleanField(default=False)
	quinta = models.BooleanField(default=False)
	sexta = models.BooleanField(default=False)
	sabado = models.BooleanField(default=False)
	domingo = models.BooleanField(default=False)
	
