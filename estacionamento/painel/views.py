from .forms import UsuarioSenha, Cadastro, Vaga
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from .models import Vagas, Perfil, Transacao
from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

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
		u = User.objects.get(username=request.user)
		p = Perfil.objects.get(usuario=request.user)
		contexto = {"u": u, "p": p}
		return render(request, 'meuperfil/index.html', contexto)
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
			usuario.first_name = nome
			usuario.last_name = sobrenome
			usuario.save()
			form = UsuarioSenha(request.POST)
			u = User.objects.get(username=request.user)
			p = Perfil.objects.get(usuario=request.user)
			contexto = {"form": form, "u": u, "p": p,"mensagem": "Cadastro realizado com sucesso"}
			return render(request, 'index.html', contexto)
		else:
			return HttpResponse("Formulário inválido")
	else:
		form = Cadastro()
		contexto = {"form": form}
		return render(request, 'cadastro.html', contexto)


def cadastraVaga(request):
	if request.method == 'POST':
		form = Vaga(request.POST, request.FILES)
		if form.is_valid():
			v = Vagas()
			v.usuario = request.user
			v.estado = form.cleaned_data['estado']
			v.categoria = form.cleaned_data['categoria']
			v.cidade = form.cleaned_data['cidade']
			v.bairro = form.cleaned_data['bairro']
			v.rua = form.cleaned_data['rua']
			v.complemento = form.cleaned_data['complemento']
			v.foto = form.cleaned_data['foto']
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
			v.save()
			u = User.objects.get(username=request.user)
			p = Perfil.objects.get(usuario=request.user)
			contexto = {"u": u, "p": p, "mensagem": "Vaga cadastrada com sucesso"}
			return render(request, 'meuperfil/index.html', contexto)
		else:
			return HttpResponse("Formulário inválido")
	else:
		return HttpResponseRedirect('meuperfil')


def vagas(request):
	if request.user.is_authenticated:
		lista_vagas = Vagas.objects.filter(usuario=request.user) #consulta
		u = User.objects.get(username=request.user)
		p = Perfil.objects.get(usuario=request.user)
		contexto = {"u":u, "p": p,"lista_vagas": lista_vagas} #contexto 
		return render(request, 'meuperfil/vagas.html', contexto)
	else:
		form = UsuarioSenha(request.POST)
		contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
		return render(request, 'index.html', contexto)


def alugarVaga(request):
	if request.user.is_authenticated:
		vagasOcupadas = Vagas.objects.filter(alugado=True)
		agora = timezone.now()	
		for x in vagasOcupadas:
			if x.alugadoAte < agora:
				x.alugado = False
				x.save()
			else:
				pass
		lista_vagas = Vagas.objects.filter(alugado=False).exclude(usuario=request.user) #consulta
		u = User.objects.get(username=request.user)
		p = Perfil.objects.get(usuario=request.user)
		contexto = {"u":u, "p": p,"lista_vagas": lista_vagas} #contexto   
		return render(request, 'meuperfil/alugar.html', contexto)
	else:
		form = UsuarioSenha(request.POST)
		contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
		return render(request, 'index.html', contexto)


def alugar(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			vaga = request.POST.get("vaga")
			preco = request.POST.get("valor")
			preco = preco.replace(',','.')
			usuario = request.POST.get("usuario")
			x = User.objects.get(username=usuario)
			u = Perfil.objects.get(usuario=x)
			u_id = Perfil.objects.get(usuario=request.user)
			if u_id.saldo >= float(preco):
				v = Vagas.objects.get(id=vaga)
				v.alugado = True
				v.alugadoAte = datetime.today() + timedelta(minutes=2)
				v.save()
				saldoAtual = u_id.saldo
				novoSaldo = float(saldoAtual) - float(preco)
				u_id.saldo = novoSaldo
				u_id.save()
				saldoAtual = u.saldo
				novoSaldo = float(saldoAtual) + float(preco)
				u.saldo = novoSaldo
				u.save()
				t = Transacao()
				t.locatario = x
				t.valor = float(preco)
				t.endereco = v.rua+'-'+v.bairro+'-'+v.estado
				t.alugador = request.user
				t.vaga = v
				t.save()
				u = User.objects.get(username=request.user)
				p = Perfil.objects.get(usuario=request.user)
				contexto = {"u": u, "p": p,"mensagem": "Vaga alugada com sucesso"}
				return render(request, 'meuperfil/index.html', contexto)
			else:
				u = User.objects.get(username=request.user)
				p = Perfil.objects.get(usuario=request.user)
				lista_vagas = Vagas.objects.filter(alugado=False).exclude(usuario=request.user) #consulta
				contexto = {"u":u, "p": p,"lista_vagas": lista_vagas, "mensagem": "Você não tem saldo suficiente"} #contexto   
				return render(request, 'meuperfil/alugar.html', contexto)	
		else:
			form = Cadastro()
			contexto = {"form": form}
			return render(request, 'cadastro.html', contexto)
	else:
		form = UsuarioSenha(request.POST)
		contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
		return render(request, 'index.html', contexto)


def transacao(request):
	if request.user.is_authenticated:
		lista_transacoes = Transacao.objects.filter(alugador=request.user) #consulta
		u = User.objects.get(username=request.user)
		p = Perfil.objects.get(usuario=request.user)
		contexto = {"u":u, "p": p,"lista_transacoes": lista_transacoes} #contexto 
		return render(request, 'meuperfil/transacao.html', contexto)
	else:
		form = UsuarioSenha(request.POST)
		contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
		return render(request, 'index.html', contexto)