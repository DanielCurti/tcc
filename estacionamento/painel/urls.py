from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('sair', views.sair, name='sair'),
	path('login_view', views.login_view, name='index'),
	path('meuperfil', views.meuperfil, name='meuperfil'),
	path('cadastro', views.cadastro, name='cadastro'),
	path('registro', views.registro, name='registro')
]