from .forms import UsuarioSenha, Cadastro, Vaga, AgendarReserva, FotoUsuario
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User 
from .models import Vagas, Perfil, Foto, Reservas
from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    form = UsuarioSenha()
    contexto = {"form": form}
    return render(request, 'index.html', contexto)


def login_view(request):
    if request.method == 'POST':
        form = UsuarioSenha(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['login']
            senha = form.cleaned_data['senha']

            Usuario = authenticate(request, username=usuario, password=senha)
            if Usuario is not None:
                login(request, Usuario)
                return HttpResponseRedirect('meuperfil')
            else:
                contexto = {"form": form, "mensagem": "Usuário ou senha inválida" }
                return render(request, 'index.html', contexto)
        else:
            return HttpResponse("Formulário inválido")
    else:
        form = UsuarioSenha()
        contexto = {"form": form}
        return render(request, 'index.html', contexto)


def sair(request):
    logout(request)
    return HttpResponseRedirect('/painel/')


def meuperfil(request):
    if request.user.is_authenticated:
        lista_vagas = [x for x in Vagas.objects.all().exclude(usuario=request.user) if x.disponivel(timezone.now()) == True] #consulta
		#lista = Vagas.objects.all().exclude(usuario=request.user)
		#lista_vagas = []
		#for v in lista:
		#	if v.disponivel() == True:
		#		lista_vagas.append(v)

        
        u = User.objects.get(username=request.user)
        p = Perfil.objects.get(usuario=request.user)
        contexto = {"u":u, "p": p,"lista_vagas": lista_vagas} #contexto   
        return render(request, 'meuperfil/index.html', contexto)
    else:
        form = UsuarioSenha(request.POST)
        contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
        return render(request, 'index.html', contexto)


def perfil(request):
    if request.user.is_authenticated:
        u = User.objects.get(username=request.user)
        try:
            v = Vagas.objects.filter(usuario=request.user)[:1]
            print(v)
            n = Vagas.objects.get(id=v)
            nota = n.nota_dono
        except ObjectDoesNotExist:
            nota = -1
        p = Perfil.objects.get(usuario=request.user)
        form = FotoUsuario()
        contexto = {"form":form,"u":u, "p": p, "nota": nota} #contexto   
        return render(request, 'meuperfil/perfil.html', contexto)
    else:
        form = UsuarioSenha(request.POST)
        contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
        return render(request, 'index.html', contexto)


def fotoPerfil(request):
    if request.user.is_authenticated:
        u = User.objects.get(username=request.user)
        try:
            v = Vagas.objects.filter(usuario=request.user)[:1]
            n = Vagas.objects.get(id=v)
            nota = n.nota_dono
        except ObjectDoesNotExist:
            nota = -1
        p = Perfil.objects.get(usuario=request.user)
        form = FotoUsuario(request.POST, request.FILES)
        if form.is_valid():
            p.imagem = form.cleaned_data['fotoUsuario']
            p.save()
        else:
            return HttpResponse("Formulário inválido")
        form = FotoUsuario()
        contexto = {"u":u, "p": p, "nota": nota, "form": form} #contexto   
        return render(request, 'meuperfil/perfil.html', contexto)
    else:
        form = UsuarioSenha(request.POST)
        contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
        return render(request, 'index.html', contexto)


def cadastro(request):
    form = Cadastro()
    contexto = {"form": form}
    return render(request, 'cadastro.html', contexto)


def novaVaga(request):
    if request.user.is_authenticated:
        form = Vaga()
        u = User.objects.get(username=request.user)
        p = Perfil.objects.get(usuario=request.user)
        contexto = {"form": form, "u": u, "p": p}
        return render(request, 'meuperfil/cadastraVaga.html', contexto)
    else:
        form = UsuarioSenha(request.POST)
        contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
        return render(request, 'index.html', contexto)


def registro(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            senha = form.cleaned_data['senha']
            nome = form.cleaned_data['nome']

            sobrenome = form.cleaned_data['sobrenome']
            email = form.cleaned_data['email']
            usuario = User.objects.create_user(login, email, senha)

            p = Perfil()
            p.usuario = usuario
            p.saldo = 0
            p.avaliacao = -1
            usuario.first_name = nome
            usuario.last_name = sobrenome
            p.telefone = form.cleaned_data['telefone']
            p.save()
            usuario.save()
            return HttpResponseRedirect('/painel/')
    else:
        form = Cadastro()
        contexto = {"form": form}
        return render(request, 'cadastro.html', contexto)


def cadastraVaga(request):
    if request.method == 'POST':
        form = Vaga(request.POST, request.FILES)
        if form.is_valid():
            v = Vagas()
            f = Foto()
            v.usuario = request.user
            v.estado = form.cleaned_data['estado']
            v.cidade = form.cleaned_data['cidade']
            v.bairro = form.cleaned_data['bairro']
            v.rua = form.cleaned_data['rua']
            v.complemento = form.cleaned_data['complemento']
            v.valor = form.cleaned_data['valor']
            v.modo = form.cleaned_data['modo']
            v.abre = form.cleaned_data['abre']
            v.fecha = form.cleaned_data['fecha']
            v.segunda = form.cleaned_data['segunda']
            v.terca = form.cleaned_data['terca']
            v.quarta = form.cleaned_data['quarta']
            v.quinta = form.cleaned_data['quinta']
            v.sexta = form.cleaned_data['sexta']
            v.sabado = form.cleaned_data['sabado']
            v.domingo = form.cleaned_data['domingo']
            v.lat = request.POST.get('latitude')
            v.lng = request.POST.get('longitude')
            v.observacao = form.cleaned_data['observacao']
            v.save()
            f.vaga = v
            f.foto = form.cleaned_data['foto']
            f.descricao = form.cleaned_data['descricao']
            f.save()
            u = User.objects.get(username=request.user)
            p = Perfil.objects.get(usuario=request.user)
            contexto = {"u": u, "p": p, "mensagem": "Vaga cadastrada com sucesso"}
            return render(request, 'meuperfil/index.html', contexto)
        else:
            return HttpResponse("Formulário inválido")
    else:
        return HttpResponseRedirect('meuperfil')


def reserva(request, x):
    if request.user.is_authenticated:
        if request.method == 'POST':
            vaga = x
            tempo = request.POST.get("hora")
            t = int(tempo)
            v = Vagas.objects.get(id=vaga)
            observacao = v.observacao
            preco = 0
            if v.disponivel(timezone.now()) == True:
                if v.modo == 'I':
                    tv = t / 1440
                    preco = v.valor * tv
                else:
                    abre = int(datetime.strptime(str(v.abre), '%H:%M:%S').strftime("%s"))
                    fecha = int(datetime.strptime(str(v.fecha), '%H:%M:%S').strftime("%s"))
                    minutostotais = abs((abre - fecha))
                    minutostotais = minutostotais / 60
                    tv = t / minutostotais
                    preco = v.valor * tv
                v = Vagas.objects.get(id=vaga)
                usuario = v.usuario
                x = User.objects.get(username=usuario)
                u = Perfil.objects.get(usuario=x)
                u_id = Perfil.objects.get(usuario=request.user)
                if u_id.saldo >= float(preco):
                    v = Vagas.objects.get(id=vaga)
                    v.save()
                    saldoAtual = u_id.saldo
                    novoSaldo = float(saldoAtual) - float(preco + (preco*0.1))
                    u_id.saldo = novoSaldo
                    u_id.save()
                    saldoAtual = u.saldo
                    novoSaldo = float(saldoAtual) + float(preco)
                    u.saldo = novoSaldo
                    u.save()
                    r = Reservas()
                    r.vaga = v
                    r.valor = preco
                    r.horaEntrada = timezone.now()
                    r.horaSaida = timezone.now() + timedelta(minutes=+t)
                    r.alugador = request.user
                    r.save()
                    mensagem = "Vaga Alugada com sucesso"
                    u = User.objects.get(username=request.user)
                    p = Perfil.objects.get(usuario=request.user)
                    contexto = {"u": u, "p": p, "v": v, 'mensagem': mensagem, 'observacao': observacao} 
                    return render(request, 'meuperfil/rota.html', contexto)
                else: 
                    u = User.objects.get(username=request.user) 
                    p = Perfil.objects.get(usuario=request.user) 
                    lista_vagas = [x for x in Vagas.objects.all().exclude(usuario=request.user) if x.disponivel(timezone.now()) == True] #consulta 
                    contexto = {"u":u, "p": p,"lista_vagas": lista_vagas, "mensagem": "Você não tem saldo suficiente"} #contexto    
                    return render(request, 'meuperfil/index.html', contexto)	
            else: 
                    u = User.objects.get(username=request.user) 
                    p = Perfil.objects.get(usuario=request.user) 
                    lista_vagas = [x for x in Vagas.objects.all().exclude(usuario=request.user) if x.disponivel(timezone.now()) == True] #consulta 
                    contexto = {"u":u, "p": p,"lista_vagas": lista_vagas, "mensagem": "Você demorou muito, esta vaga acabou de ser alugada"} #contexto    
                    return render(request, 'meuperfil/index.html', contexto)
        else:
            form = Cadastro()
            contexto = {"form": form}
            return render(request, 'meuperfil/index.html', contexto)
    else:
        form = UsuarioSenha(request.POST)
        contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
        return render(request, 'index.html', contexto)



def vagas(request):
    if request.user.is_authenticated:
        lista_vagas = Vagas.objects.filter(usuario=request.user).exclude(ativo=False) #consulta
        u = User.objects.get(username=request.user)
        p = Perfil.objects.get(usuario=request.user)
        contexto = {"u":u, "p": p,"lista_vagas": lista_vagas} #contexto 
        return render(request, 'meuperfil/vagas.html', contexto)
    else:
        form = UsuarioSenha(request.POST)
        contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
        return render(request, 'index.html', contexto)


def detalhe(request, x):
    if request.user.is_authenticated: 
        v = Vagas.objects.get(id=x)
        fotos = Foto.objects.filter(vaga=v)
        pdv = Perfil.objects.get(usuario=v.usuario)
        u = User.objects.get(username=request.user)
        p = Perfil.objects.get(usuario=request.user)
        if v.modo == 'I':
            precoMinuto = v.valor / 1440
        else:
            abre = int(datetime.strptime(str(v.abre), '%H:%M:%S').strftime("%s"))
            fecha = int(datetime.strptime(str(v.fecha), '%H:%M:%S').strftime("%s"))
            minutostotais = abs((abre - fecha))
            minutostotais = minutostotais / 60
            precoMinuto = v.valor / minutostotais
            

        if v.modo == 'P':
            s = str(timezone.now().year)+"-"+str(timezone.now().month)+'-'+str(timezone.now().day)+" "+str(v.fecha).split(".")[0]
            t = str(timezone.now()).split(".")[0]
            f = '%Y-%m-%d %H:%M:%S'
            dif = round((datetime.strptime(s, f) - datetime.strptime(t, f)).total_seconds()/60, 0)
        else:
            dif = 1440
        contexto = {"u": u, "p": p,"v": v, 'dif': dif, "pdv": pdv,"fotos": fotos,"precoMinuto": precoMinuto} 
        return render(request, 'meuperfil/detalhe.html', contexto)
		
    else:
        form = UsuarioSenha(request.POST)
        contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
        return render(request, 'index.html', contexto)



def transacao(request):
    if request.user.is_authenticated:
        lista_transacoes = Reservas.objects.filter(alugador=request.user).order_by('-horaEntrada') #consulta
        u = User.objects.get(username=request.user)
        p = Perfil.objects.get(usuario=request.user)
        r = range(5)
        contexto = {"u":u, "p": p,"lista_transacoes": lista_transacoes, "r": r} #contexto 
        return render(request, 'meuperfil/transacao.html', contexto)
    else:
        form = UsuarioSenha(request.POST)
        contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
        return render(request, 'index.html', contexto)


def agendarReserva(request):
    u = User.objects.get(username=request.user)
    p = Perfil.objects.get(usuario=request.user)
    contexto = {"u": u, "p":p}
    return render(request, 'meuperfil/agendarReserva.html', contexto)


def buscar(request):
    if request.user.is_authenticated == False:
        form = UsuarioSenha(request.POST)
        contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
        return render(request, 'index.html', contexto)
    if request.method == 'GET':
        u = User.objects.get(username=request.user)
        p = Perfil.objects.get(usuario=request.user)
        contexto = {"u": u, "p": p}
        return render(request, 'meuperfil/agendarReserva.html', contexto)
    tempoEntrada = request.POST.get('horaEntrada')
    dataEntrada = request.POST.get('dataEntrada')
    temp = tempoEntrada.split(':')
    horaEntrada = int(temp[0])
    minutoEntrada = int(temp[1])
    temp = dataEntrada.split('-')
    diaEntrada = int(temp[2])
    mesEntrada = int(temp[1])
    anoEntrada = int(temp[0])

    dataTempoEntrada = datetime(year=anoEntrada, month=mesEntrada, day=diaEntrada, hour=horaEntrada, minute=minutoEntrada)

    tempoSaida = request.POST.get('horaSaida')
    dataSaida = request.POST.get('dataSaida')
    temp = tempoSaida.split(':')
    horaSaida = int(temp[0])
    minutoSaida = int(temp[1])
    temp = dataSaida.split('-')
    diaSaida = int(temp[2])
    mesSaida = int(temp[1])
    anoSaida = int(temp[0])

    dataTempoSaida = datetime(year=anoSaida, month=mesSaida, day=diaSaida, hour=horaSaida, minute=minutoSaida)
    
    lat = float(request.POST.get('lat'))
    lng = float(request.POST.get('lng'))
    
    lista_vagas = [x for x in Vagas.objects.all().exclude(usuario=request.user) if x.disponivel(dataTempoEntrada, dataTempoSaida, lat, lng) == True]#consulta
    u = User.objects.get(username=request.user)
    p = Perfil.objects.get(usuario=request.user)
    t = round((dataTempoSaida - dataTempoEntrada).total_seconds()/60, 0)
    dataTempoEntrada = dataEntrada + " " + tempoEntrada
    dataTempoSaida = dataSaida + " " +tempoSaida

    contexto = {"u": u, "p":p,"t": t, "lista_vagas": lista_vagas,"dataTempoEntrada": dataTempoEntrada, "dataTempoSaida": dataTempoSaida}
    return render(request, 'meuperfil/buscar.html', contexto)


def reservasvaga(request, x):
    if request.user.is_authenticated:
        lista_locatarios = Reservas.objects.filter(vaga=x).order_by('-horaEntrada') #consulta
        u = User.objects.get(username=request.user)
        p = Perfil.objects.get(usuario=request.user)
        r = range(5)
        contexto = {"u":u, "p": p,"lista_locatarios": lista_locatarios, "r": r} #contexto 
        return render(request, 'meuperfil/reservasvaga.html', contexto)
    else:
        form = UsuarioSenha(request.POST)
        contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
        return render(request, 'index.html', contexto)


def rota(request, x):
    if request.user.is_authenticated:
        u = User.objects.get(username=request.user)
        p = Perfil.objects.get(usuario=request.user)
        v = Vagas.objects.get(id=x)
        contexto = {"u": u, "p": p, "v": v}
        return render(request, 'meuperfil/rota.html', contexto)
    else:
        form = UsuarioSenha(request.POST)
        contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
        return render(request, 'index.html', contexto)


def reserve(request, x):
    if request.user.is_authenticated:
        if request.method == 'POST':
            vaga = x
            entrada = request.POST.get('entrada')
            saida = request.POST.get('saida')
            entrada = datetime.strptime(entrada, '%Y-%m-%d %H:%M')
            saida = datetime.strptime(saida, '%Y-%m-%d %H:%M')
            t = round((saida - entrada).total_seconds()/60, 0)
            v = Vagas.objects.get(id=vaga)
            observacao = v.observacao
            preco = 0
            if v.disponivel(entrada, saida) == True:
                if v.modo == 'I':
                    tv = t / 1440
                    preco = v.valor * tv
                else:
                    abre = int(datetime.strptime(str(v.abre), '%H:%M:%S').strftime("%s"))
                    fecha = int(datetime.strptime(str(v.fecha), '%H:%M:%S').strftime("%s"))
                    minutostotais = abs((abre - fecha))
                    minutostotais = minutostotais / 60
                    tv = t / minutostotais
                    preco = v.valor * tv
                v = Vagas.objects.get(id=vaga)
                usuario = v.usuario
                x = User.objects.get(username=usuario)
                u = Perfil.objects.get(usuario=x)
                u_id = Perfil.objects.get(usuario=request.user)
                if u_id.saldo >= float(preco):
                    v = Vagas.objects.get(id=vaga)
                    v.save()
                    saldoAtual = u_id.saldo
                    novoSaldo = float(saldoAtual) - float(preco + (preco*0.1))
                    u_id.saldo = novoSaldo
                    u_id.save()
                    saldoAtual = u.saldo
                    novoSaldo = float(saldoAtual) + float(preco)
                    u.saldo = novoSaldo
                    u.save()
                    r = Reservas()
                    r.vaga = v
                    r.valor = preco
                    r.horaEntrada = entrada
                    r.horaSaida = saida
                    r.alugador = request.user
                    r.save()
                    mensagem = "Vaga Alugada com sucesso"
                    u = User.objects.get(username=request.user)
                    p = Perfil.objects.get(usuario=request.user)
                    contexto = {"u": u, "p": p, 'mensagem': mensagem, 'observacao': observacao} 
                    return render(request, 'meuperfil/''/rota.html', contexto)
                else: 
                    u = User.objects.get(username=request.user) 
                    p = Perfil.objects.get(usuario=request.user) 
                    lista_vagas = [x for x in Vagas.objects.all().exclude(usuario=request.user) if x.disponivel(timezone.now()) == True] #consulta 
                    contexto = {"u":u, "p": p,"lista_vagas": lista_vagas, "mensagem": "Você não tem saldo suficiente"} #contexto    
                    return render(request, 'meuperfil/index.html', contexto)    
            else: 
                    u = User.objects.get(username=request.user) 
                    p = Perfil.objects.get(usuario=request.user) 
                    lista_vagas = [x for x in Vagas.objects.all().exclude(usuario=request.user) if x.disponivel(timezone.now()) == True] #consulta 
                    contexto = {"u":u, "p": p,"lista_vagas": lista_vagas, "mensagem": "Você demorou muito, esta vaga acabou de ser alugada"} #contexto    
                    return render(request, 'meuperfil/index.html', contexto)
        else:
            u = User.objects.get(username=request.user)
            p = Perfil.objects.get(usuario=request.user)
            contexto = {"u": u, "p": p}
            return render(request, 'meuperfil/reservasvaga.html', contexto)
    else:
        form = UsuarioSenha(request.POST)
        contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
        return render(request, 'index.html', contexto)



@csrf_exempt
def api_reembolsar(request, x): 
    if request.method == "POST":
        #adicionar dados do novo post
        transacao = request.POST["idreserva"]
        t = Reservas.objects.get(id=transacao)
        vaga = t.vaga.usuario
        dono = Perfil.objects.get(usuario=vaga)
        alugadorperfil = Perfil.objects.get(usuario=t.alugador) 
        if dono.saldo < t.valor:
            print("nao tem saldo")
            temp = {"status": "Saldo insuficiente para reembolsar esta transação"}
            return JsonResponse(temp)
        else:
            print("tem saldo")
            dono.saldo = dono.saldo-t.valor
            dono.save()
            t.reembolsado = True
            t.save()
            alugadorperfil.saldo = alugadorperfil.saldo + (t.valor * 1.1)
            alugadorperfil.save()
            temp = {"status": "Ok"}
            return JsonResponse(temp)
    else:
        return render(request, 'index.html')


@csrf_exempt
def api_avaliacao (request): 
    if request.method == "POST":
        #adicionar dados do novo post
        transacao = request.POST["idtransacao"]
        nota = request.POST["nota"]
        nota = int(nota) + 1
        t = Reservas.objects.get(id=transacao)
        t.avaliacaoDono = nota
        t.save()
        #contruindo estrutura em JSON
        temp = {"status": "Ok"}
      
        return JsonResponse(temp)


@csrf_exempt
def api_avaliacao2 (request, x): 
    if request.method == "POST":
        #adicionar dados do novo post
        transacao = request.POST["idtransacao"]
        nota = request.POST["nota"]
        nota = int(nota) + 1
        t = Reservas.objects.get(id=transacao)
        t.avaliacaolocador = nota
        t.save()
        #contruindo estrutura em JSON
        temp = {"status": "Ok"}
      
        return JsonResponse(temp)


@csrf_exempt
def api_excluir(request): 
    if request.method == "POST":
        #adicionar dados do novo post
        vaga = request.POST["idvaga"]
        v = Vagas.objects.get(id=vaga)
        v.ativo = False
        v.save()
        #contruindo estrutura em JSON
        temp = {"status": "Ok"}
      
        return JsonResponse(temp)