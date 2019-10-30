from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name='index'),
	path('sair', views.sair, name='sair'),
	path('login_view', views.login_view, name='index'),
	path('meuperfil', views.meuperfil, name='meuperfil'),
	path('cadastro', views.cadastro, name='cadastro'),
	path('registro', views.registro, name='registro'),
	path('novaVaga', views.novaVaga, name='novaVaga'),
	path('cadastraVaga', views.cadastraVaga, name='cadastraVaga'),
	path('vagas', views.vagas, name='vagas'),
	path('<int:x>/detalhe', views.detalhe, name='detalhe'),
    path('<int:x>/rota', views.rota, name='rota'),
	path('transacao', views.transacao, name='transacao'),
	path('<int:x>/reserva', views.reserva, name='reserva'),
    path('agendarReserva', views.agendarReserva, name='agendarReserva'),
    path('buscar', views.buscar, name='buscar'),
    path('perfil', views.perfil, name='perfil'),
    path('fotoPerfil', views.fotoPerfil, name='fotoPerfil'),
    path('api/avaliacao', views.api_avaliacao, name='api_avaliacao'),
    path('api/excluir', views.api_excluir, name='api_excluir'),
    path('<int:x>/api/reembolsar', views.api_reembolsar, name='api_reembolsar'),
    path('<int:x>/api/avaliacao2', views.api_avaliacao2, name='api_avaliacao2'),
    path('<int:x>/reservasvaga', views.reservasvaga, name='reservasvaga'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)