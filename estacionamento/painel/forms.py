from django import forms 
from django.utils import timezone
from datetime import datetime, timedelta

class UsuarioSenha(forms.Form) :
    login = forms.CharField(label="", max_length=30)
    senha = forms.CharField(widget=forms.PasswordInput(), label="", max_length=20)

    login.widget.attrs['placeholder'] = 'Login'
    senha.widget.attrs['placeholder'] = 'Senha'
    login.widget.attrs['class'] = 'form-control'
    senha.widget.attrs['class'] = 'form-control'


class Cadastro(forms.Form):
    login = forms.CharField(label="")
    senha = forms.CharField(widget=forms.PasswordInput(),label="")
    nome = forms.CharField(label='')
    sobrenome = forms.CharField(label='')
    email = forms.EmailField(label='')
    telefone = forms.CharField(label='')

    login.widget.attrs['placeholder'] = 'Crie seu Usuario'
    login.widget.attrs['class'] = 'form-control'
    senha.widget.attrs['placeholder'] = 'Crie sua Senha'
    senha.widget.attrs['class'] = 'form-control'
    nome.widget.attrs['placeholder'] = 'Nome'
    nome.widget.attrs['class'] = 'form-control'
    sobrenome.widget.attrs['placeholder'] = 'Sobrenome'
    sobrenome.widget.attrs['class'] = 'form-control'
    email.widget.attrs['placeholder'] = 'Endereço de E-mail'
    email.widget.attrs['class'] = 'form-control'
    telefone.widget.attrs['placeholder'] = 'Numero de Telefone'
    telefone.widget.attrs['class'] = 'form-control'


class Vaga(forms.Form):
    ESTADO = (
        ('XX', 'Selecione'),
        ('RS', 'Rio Grande Do Sul'),
        ('SC', 'Santa Catarina'),
        ('PR', 'Parana'),
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
        ('I', 'SIM'),
        ('P', 'NÃO'),
    )
    estado = forms.CharField( label="", widget=forms.Select(choices=ESTADO))
    cidade = forms.CharField(label="", max_length=100)
    bairro = forms.CharField(label="", max_length=100)
    rua = forms.CharField(label="", max_length=100)
    complemento = forms.CharField(label="", max_length=50, required=False)
    valor = forms.FloatField(label='')
    foto = forms.FileField()
    descricao = forms.CharField(label="", max_length=200)
    modo = forms.CharField(label='', widget=forms.Select(choices=MODO))  
    abre = forms.CharField(label="", widget=forms.Select(choices=HORA))
    fecha = forms.CharField(label="",widget=forms.Select(choices=HORA))
    segunda = forms.BooleanField(label='',required=False, widget=forms.CheckboxInput())
    terca = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    quarta = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    quinta = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    sexta = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    sabado = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    domingo = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    observacao = forms.CharField(max_length=500, required=False, widget=forms.Textarea)

    estado.widget.attrs['class'] = 'custom-select'
    cidade.widget.attrs['class'] = 'form-control'
    cidade.widget.attrs['placeholder'] = 'Cidade'
    bairro.widget.attrs['class'] = 'form-control'
    rua.widget.attrs['class'] = 'form-control'
    complemento.widget.attrs['class'] = 'form-control'
    bairro.widget.attrs['placeholder'] = 'Bairro'
    rua.widget.attrs['placeholder'] = 'Rua'
    complemento.widget.attrs['placeholder'] = 'Complemento'
    valor.widget.attrs['class'] = 'form-control'
    foto.widget.attrs['class'] = 'form-control-file'
    descricao.widget.attrs['class'] = 'form-control'
    modo.widget.attrs['class'] = 'custom-select'
    abre.widget.attrs['class'] = 'custom-select'
    fecha.widget.attrs['class'] = 'custom-select'
    observacao.widget.attrs['placeholder'] = 'Use este campo para passar alguma informação relevante sobre o estacionamneto, como a senha de um portão por exemplo.'
    observacao.widget.attrs['class'] = 'form-control'


class AgendarReserva(forms.Form):

    horaEntrada = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"), initial='00:00:00')
    horaSaida = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"), initial='00:00:00')


class FotoUsuario(forms.Form):
    fotoUsuario = forms.FileField()