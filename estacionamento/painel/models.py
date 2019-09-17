from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from datetime import datetime, timedelta

class Perfil(models.Model):
	usuario   = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	imagem    = models.ImageField(blank=True, upload_to='usuarios', default='imagens/sem_foto.jpg')
	saldo     = models.FloatField(default=0)
	avaliacao = models.IntegerField(default=-1)

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
	modo        = models.CharField(max_length=1)
	abre        = models.TimeField(max_length=5)
	fecha       = models.TimeField(max_length=5)
	segunda     = models.BooleanField(default=False)
	terca       = models.BooleanField(default=False)
	quarta      = models.BooleanField(default=False)
	quinta      = models.BooleanField(default=False)
	sexta       = models.BooleanField(default=False)
	sabado      = models.BooleanField(default=False)
	domingo     = models.BooleanField(default=False)
	lat         = models.CharField(max_length=100, default='-27.3667')
	lng         = models.CharField(max_length=100, default='-53.000')
	avaliacao   = models.IntegerField(default=-1)

	def __str__(self):
		return str(self.id)


	def disponivel(self, inicio):
		reservas = self.reservas_set.all()
		for x in reservas:
			tempoMinimo = inicio + timedelta(minutes=+15)
			if x.horaEntrada <= tempoMinimo and x.horaSaida >= inicio:
				return False
			tolerancia = x.horaSaida + timedelta(minutes=+5)
			if x.horaSaida < inicio and tolerancia > inicio:
				return False
		return True


class Reservas(models.Model):
	vaga             = models.ForeignKey(Vagas, on_delete = models.CASCADE)
	valor            = models.FloatField(default=0)
	horaEntrada      = models.DateTimeField()
	horaSaida        = models.DateTimeField()	
	avaliacaoDono    = models.IntegerField(default=-1)
	avaliacaolocador = models.IntegerField(default=-1)
	alugador         = models.ForeignKey('auth.User', default='', on_delete = models.CASCADE, related_name='alugadorReserva')

	def __str__(self):
		return str(self.vaga) +" - "+ str(self.alugador.first_name)+" "+ str(self.alugador.last_name)


class Foto(models.Model):
	vaga      = models.ForeignKey(Vagas, on_delete = models.CASCADE)
	foto      = models.ImageField(blank=True, upload_to='vagas', default='imagens/sem_foto.jpg')
	descricao = models.CharField(max_length=100, default=0)

	def __str__(self):
	 	return self.descricao


