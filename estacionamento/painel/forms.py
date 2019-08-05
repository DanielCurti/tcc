from django import forms 

class UsuarioSenha(forms.Form) :
	login = forms.CharField(label='Login', max_length=30)
	senha = forms.CharField(label='Senha', max_length=20)


class Cadastro(forms.Form):
	usuario = forms.CharField(label="Digite seu usuario")
	senha = forms.CharField(label="Crie uma senha")
	nome = forms.CharField(label='Nome')
	sobrenome = forms.CharField(label='sobrenome')
	email = forms.CharField(label='E-mail')