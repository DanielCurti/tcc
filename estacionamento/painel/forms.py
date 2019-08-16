from django import forms 

class UsuarioSenha(forms.Form) :
	login = forms.CharField(label='Login', max_length=30)
	senha = forms.CharField(widget=forms.PasswordInput(), label='Senha', max_length=20)


class Cadastro(forms.Form):
	login = forms.CharField(label="Digite seu usuario")
	senha = forms.CharField(widget=forms.PasswordInput(),label="Crie uma senha")
	nome = forms.CharField(label='Nome')
	sobrenome = forms.CharField(label='sobrenome')
	email = forms.CharField(label='E-mail')


class Vaga(forms.Form):
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
	HORA = (
		('00:00', '00:00'),
		('00:30', '00:30'),
		('01:00', '01:00'),
		('01:30', '01:30'),
		('02:00', '02:00'),
		('02:30', '02:30'),
		('03:00', '03:00'),
		('03:30', '03:30'),
		('04:00', '04:00'),
		('04:30', '04:30'),
		('05:00', '05:00'),
		('05:30', '05:30'),
		('06:00', '06:00'),
		('06:30', '06:30'),
		('07:00', '07:00'),
		('07:30', '07:30'),
		('08:00', '08:00'),
		('08:30', '08:30'),
		('09:00', '09:00'),
		('09:30', '09:30'),
		('10:00', '10:00'),
		('10:30', '10:30'),
		('11:00', '11:00'),
		('11:30', '11:30'),
		('12:00', '12:00'),
		('12:30', '12:30'),
		('13:00', '13:00'),
		('13:30', '13:30'),
		('14:00', '14:00'),
		('14:30', '14:30'),
		('15:00', '15:00'),
		('15:30', '15:30'),
		('16:00', '16:00'),
		('16:30', '16:30'),
		('17:00', '17:00'),
		('17:30', '17:30'),
		('18:00', '18:00'),
		('18:30', '18:30'),
		('19:00', '19:00'),
		('19:30', '19:30'),
		('20:00', '20:00'),
		('20:30', '20:30'),
		('21:00', '21:00'),
		('21:30', '21:30'),
		('22:00', '22:00'),
		('22:30', '22:30'),
		('23:00', '23:00'),
		('23:30', '23:30'),

	)
	MODO = (
		('I', 'Integral'),
		('P', 'Parcial'),
	)
	estado = forms.CharField(widget=forms.Select(choices=ESTADO))
	categoria = forms.CharField(widget=forms.Select(choices=CATEGORIA))
	cidade = forms.CharField(max_length=100)
	bairro = forms.CharField(max_length=100)
	rua = forms.CharField(max_length=100)
	complemento = forms.CharField(max_length=50, required=False)
	valor = forms.FloatField(label='Valor Diário')
	foto = forms.FileField()
	modo = forms.CharField(widget=forms.Select(choices=MODO))
	abre = forms.CharField(widget=forms.Select(choices=HORA))
	fecha = forms.CharField(widget=forms.Select(choices=HORA))
	segunda = forms.BooleanField(required=False, widget=forms.CheckboxInput())
	terca = forms.BooleanField(required=False, widget=forms.CheckboxInput())
	quarta = forms.BooleanField(required=False, widget=forms.CheckboxInput())
	quinta = forms.BooleanField(required=False, widget=forms.CheckboxInput())
	sexta = forms.BooleanField(required=False, widget=forms.CheckboxInput())
	sabado = forms.BooleanField(required=False, widget=forms.CheckboxInput())
	domingo = forms.BooleanField(required=False, widget=forms.CheckboxInput())


	