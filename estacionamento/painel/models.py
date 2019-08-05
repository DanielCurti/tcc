from django.db import models

class Foto(models.Model):
	usuario = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	imagem = models.ImageField(blank=True, upload_to='imagens', default='imagens/sem_foto.jpg')


class Receber(models.Model):
	usuario = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	FORMA_RECEBIMENTO = (
		('PIC', 'PicPay'),
		('PAY', 'PayPal'),
	)
	forma = models.CharField(max_length=3, choices=FORMA_RECEBIMENTO)
	link = models.CharField(max_length=500)
	qrcode = models.ImageField()


class Vaga(models.Model):
	usuario = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	ESTADO = (
		('RS', 'Rio Grande Do Sul'),
		('SC', 'Santa Catarina'),
		('PR', 'Parana'),
	)
	CATEGORIA = (
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
	
