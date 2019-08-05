from .forms import UsuarioSenha, Cadastro
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
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
		return render(request, 'meuperfil/index.html')
	else:
		form = UsuarioSenha(request.POST)
		contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
		return render(request, 'index.html', contexto)


def cadastro(request):
	if request.user.is_authenticated:
		form = Cadastro()
		contexto = {"form": form}
		return render(request, 'cadastro.html', contexto)
	else:
		form = UsuarioSenha(request.POST)
		contexto = {"form": form, "mensagem": "Você deve fazer login para acessar está área do site." }
		return render(request, 'index.html', contexto)


def registro(request):
	if request.method == 'POST':
		form = Cadastro(request.POST)
		if form.is_valid():
			login = form.cleaned_data['usuario']
			senha = form.cleaned_data['senha']
			nome = form.cleaned_data['nome']
			sobrenome = form.cleaned_data['sobrenome']
			email = form.cleaned_data['email']
			usuario = User.objects.create_user(login, email, senha)
			usuario.first_name = nome
			usuario.last_name = sobrenome
			usuario.save()
			form = UsuarioSenha(request.POST)
			contexto = {"form": form, "mensagem": "Cadastro realizado com sucesso"}
			return render(request, 'index.html', contexto)
		else:
			return HttpResponse("Formulário inválido")
	else:
		form = UsuarioSenha()
		contexto = {"form": form}
		return render(request, 'index.html', contexto)
