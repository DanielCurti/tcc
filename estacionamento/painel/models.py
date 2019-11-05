from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from datetime import datetime, timedelta

class Perfil(models.Model):
    usuario   = models.OneToOneField(User, on_delete = models.CASCADE)
    imagem    = models.ImageField(blank=True, upload_to='usuarios', default='sem_foto.jpg')
    saldo     = models.FloatField(default=0)
    telefone  = models.CharField(default="", max_length=11)

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
    lat         = models.CharField(max_length=100)
    lng         = models.CharField(max_length=100)
    observacao  = models.CharField(max_length=500, default="")

    def __str__(self):
        return str(self.id) + " " + str(self.usuario.first_name) + " " + str(self.valor)



    def disponivel(self, inicio, fim = None, latit = None, lngit = None):
        if self.ativo == False:
            return False
        if fim == None:
            fim = inicio + timedelta(minutes=30)
        if self.modo == "P":
            if not(self.abre < inicio.time() and self.fecha > fim.time()):
                return False
            dia_semana = inicio.strftime("%a")
            if dia_semana == "Fri":
                if self.sexta == False:
                    return False
            if dia_semana == "Mon":
                if self.segunda == False:
                    return False
            if dia_semana == "Tue":
                if self.terca == False:
                    return False
            if dia_semana == "Wed":
                if self.quarta == False:
                    return False
            if dia_semana == "Thu":
                if self.quinta == False:
                    return False
            if dia_semana == "Sat":
                if self.sabado == False:
                    return False
            if dia_semana == "Sun":
                if self.domingo == False:
                    return False
        
        if latit != None and lngit != None:
            
            latitudemaxima = latit + 0.01
            longitudemaxima = lngit + 0.01
            latitudeminima = latit - 0.01
            longitudeminima = lngit - 0.01
            if float(self.lat) > float(latitudemaxima) or float(self.lat) < float(latitudeminima) or float(self.lng) > float(longitudemaxima) or float(self.lng) < float(longitudeminima):
                return False
            
        reservas = self.reservas_set.all()
        for x in reservas:
            if not((x.horaEntrada < inicio and x.horaSaida < inicio) or (x.horaEntrada > fim and x.horaSaida > fim) or (x.reembolsado == True)):
                return False

        return True


    def nota_vaga(self):
        reservas = self.reservas_set.all()
        n = 0
        vagas_avaliadas =  0 
        for x in reservas:
            if x.avaliacaoDono == -1:
                pass
            else:
                n = n + x.avaliacaoDono
                vagas_avaliadas = vagas_avaliadas + 1
        if vagas_avaliadas == 0:
            pass
        else:
            resultado = n / vagas_avaliadas
            return resultado


    def nota_dono(self):
        r = self.usuario
        reservas = Reservas.objects.filter(vaga__usuario=r)
        n = 0
        vagas_avaliadas =  0 
        for x in reservas:
            if x.avaliacaoDono == -1:
                pass
            else:
                n = n + x.avaliacaoDono
                vagas_avaliadas = vagas_avaliadas + 1
        reservas = Reservas.objects.filter(alugador=r)
        for x in reservas:
            if x.avaliacaolocador == -1:
                pass
            else:
                n = n + x.avaliacaolocador
                vagas_avaliadas = vagas_avaliadas + 1
        if vagas_avaliadas == 0:
            pass
        else:
            resultado = n / vagas_avaliadas
            print(reservas)
            return resultado
    

    def preco(self):
        t = 60
        if self.modo == 'I':
            tv = t / 1440
            preco = self.valor * tv
        else:
            abre = int(datetime.strptime(str(self.abre), '%H:%M:%S').strftime("%s"))
            fecha = int(datetime.strptime(str(self.fecha), '%H:%M:%S').strftime("%s"))
            minutostotais = abs((abre - fecha))
            minutostotais = minutostotais / 60
            tv = t / minutostotais
            preco = self.valor * tv
        preco = preco * 1.1
        return preco

class Reservas(models.Model):
    vaga             = models.ForeignKey(Vagas, on_delete = models.CASCADE)
    valor            = models.FloatField(default=0)
    horaEntrada      = models.DateTimeField()
    horaSaida        = models.DateTimeField()  
    avaliacaoDono    = models.IntegerField(default=-1)
    avaliacaolocador = models.IntegerField(default=-1)
    alugador         = models.ForeignKey('auth.User', default='', on_delete = models.CASCADE, related_name='alugadorReserva')
    reembolsado      = models.BooleanField(default=False)

    def __str__(self):
    	return str(self.id) +" - "+ str(self.alugador.first_name)+" "+ str(self.alugador.last_name)+" "+str(self.horaEntrada)+" até "+str(self.horaSaida)


    def valor_total(self):
        valor = self.valor + (self.valor * 0.1)
        return valor
    


class Foto(models.Model):
	vaga      = models.OneToOneField(Vagas, on_delete = models.CASCADE)
	foto      = models.ImageField(blank=True, upload_to='vagas', default='imagens/sem_foto.jpg')
	descricao = models.CharField(max_length=100, default=0)

	def __str__(self):
	 	return self.descricao 


