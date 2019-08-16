from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from datetime import datetime

class Perfil(models.Model):
	usuario = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	imagem  = models.ImageField(blank=True, upload_to='usuarios', default='imagens/sem_foto.jpg')
	saldo   = models.FloatField(default=0)

	def __str__(self):
		return str(self.usuario)


class Vagas(models.Model):
	usuario     = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	estado      = models.CharField(max_length=2)
	cidade      = models.CharField(max_length=100)
	bairro      = models.CharField(max_length=100)
	rua         = models.CharField(max_length=100)
	complemento = models.CharField(max_length=50, default='.')
	valor       = models.FloatField()
	ativo       = models.BooleanField(default=True)
	alugado     = models.BooleanField(default=False)
	categoria   = models.CharField(max_length=2)
	modo        = models.CharField(max_length=1)
	alugadoAte  = models.DateTimeField(default=timezone.now)
	abre        = models.CharField(max_length=5)
	fecha       = models.CharField(max_length=5)
	foto        = models.ImageField(blank=True, upload_to='vagas', default='imagens/sem_foto.jpg')
	segunda     = models.BooleanField(default=False)
	terca       = models.BooleanField(default=False)
	quarta      = models.BooleanField(default=False)
	quinta      = models.BooleanField(default=False)
	sexta       = models.BooleanField(default=False)
	sabado      = models.BooleanField(default=False)
	domingo     = models.BooleanField(default=False)
	
	def __str__(self):
		return str(self.id)


class Transacao(models.Model):
	vaga      = models.ForeignKey(Vagas, on_delete = models.CASCADE)
	locatario = models.ForeignKey(User, default='', on_delete = models.CASCADE, related_name='locatario')
	valor     = models.FloatField(default=0)
	avaliacao = models.IntegerField(null=True)
	data      = models.DateTimeField(default=timezone.now)
	endereco  = models.CharField(max_length=100, default='')
	alugador  = models.ForeignKey('auth.User', default='', on_delete = models.CASCADE, related_name='alugador')

	def __str__(self):
		return str(self.vaga)


class Reservas(models.Model);
	vaga        = models.ForeignKey(Vagas, on_delete = models.CASCADE)
	locatario   = models.ForeignKey(User, default='', on_delete = models.CASCADE, related_name='locatario')
	valor       = models.FloatField(default=0)
	data        = models.DateTimeField(default=timezone.now)
	horaEntrada = models.DateTimeField()
	horaSaida   = models.DateTimeField()	
	alugador    = models.ForeignKey('auth.User', default='', on_delete = models.CASCADE, related_name='alugador')