from django.conf.urls import url, include
from cerdo import  views

from django.contrib.auth.views import login, logout_then_login



from django.contrib import admin


urlpatterns = [
	url(r'^ver', views.VistaCerdos, name='list_cerdos'),
    url(r'^crearCerdo/', views.CerdoCrear.as_view(), name='crear_cerdos'),
    url(r'^editarcerdo/(?P<pk>\d+)', views.CerdoEditar.as_view(), name='editar_cerdos'),
    url(r'^eliminarcerdo/(?P<pk>\d+)', views.CerdoEliminar.as_view(), name='eliminar_cerdos'),
    url(r'^buscar/', views.BuscarCerdo.as_view(), name='buscar_cerdo'),
    url(r'^pdfcerdo/', views.CrearPdfCerdo.as_view(), name="pdfcerdo"),
    url(r'^pdfcerdo1/', views.CrearPdfCerdo4.as_view(), name="pdfcerdo1"),
    url(r'^generoM/', views.FiltarGeneroM.as_view(), name="generoM"),
     url(r'^generoH/', views.FiltarGeneroH.as_view(), name="generoH"),

    #url(r'^BuscarCerdo1/(?P<nombre>\d+)/$', views.BuscarCerdo, name="buscar_cerdo-list"),
    #vacunas
    url(r'^vacunas/', views.VistaVacunas, name='list_vacunas'),
    url(r'^crearvacunas/', views.VacunaCrear.as_view(), name='crear_vacunas'),
    url(r'^editarvacunas/(?P<pk>\d+)', views.VacunaEditar.as_view(), name='editar_vacunas'),
    url(r'^eliminarvacunas/(?P<pk>\d+)', views.VacunaEliminar.as_view(), name='eliminar_vacunas'),
    url(r'^pdfVacuna/', views.CrearPdfVacunas.as_view(), name="pdfvacuna"),
    url(r'^buscarvacuna/', views.BuscarVacuna.as_view(), name='buscar_vacuna'),
    #partos
    url(r'^partos/', views.VistaPartos, name='list_partos'),
	url(r'^crearpartos/', views.PartosCrea.as_view(), name='crear_partos'),
    url(r'^editarpartos/(?P<pk>\d+)', views.PartoEditar.as_view(), name='editar_partos'),
    url(r'^eliminarpartos/(?P<pk>\d+)', views.PartoEliminar.as_view(), name='eliminar_partos'),
    url(r'^buscarparto/', views.BuscarParto.as_view(), name='buscar_parto'),
    url(r'^pdfparto/', views.CrearPdfParto.as_view(), name="pdfparto"),
   # url(r'^buscar/', views.BuscarCerdo.as_view(), name='buscar_cerdo'),   
]