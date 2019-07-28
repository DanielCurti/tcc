from django.db import models

class Usuario(models.Model):
	login = models.CharField(max_length=200)
	senha = models.CharField(min_length=8 ,max_length=30)
	nome  = models.Charfield(max_length=100)
	sobrenome = models.CharField(max_length=100)
	foto = models.ImageField()
	telefone = models.CharField(max_length=14)
	email = models.CharField(max_length=200)
	nascimento = models.CharField(length=10)
	recebimento = models.ForeingKey(Receber, on_delete = models.CASCADE)
	vaga = models.ForeingKey(Vaga, on_delete = models.CASCADE)


class Receber(models.Model):
	FORMA_RECEBIMENTO = (
		('PIC', 'PicPay'),
		('PAY', 'PayPal'),
	)
	forma = models.CharField(max_length=3, choices=FORMA_RECEBIMENTO)
	link = models.CharField(max_length=500)
	qrcode = models.ImageField()


class Vaga(models.model):
	ESTADO = (
		('RS', 'Rio Grande Do Sul'),
		('SC', 'Santa Catarina'),
		('PR', 'Parana'),
	)
	CATEGORIA (
		('Cr', 'Carro'),
		('Mo', 'Motocicleta'),
		('Cn', 'Caaminhão'),
	)
	estado = models.CharField(max_length=2, choices=ESTADO)
	cidade = models.CharField(max_length=100)
	bairro = models.CharField(max_length=100)
	rua    = models.CharField(max_length=100)
	numero = models.CharField(max_length=7)
	valor  = models.FloatField()
	categoria = models.CharField(max_length=2, choices=CATEGORIA)
	
