# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cerdo.models import Cerdos, Vacunas, Partos
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView, DetailView
from cerdo.forms import CerdoForm, PartosForm, VacunasForm, PartosForm
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.core import serializers
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy , resolve
from django.contrib.auth.mixins import LoginRequiredMixin
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin
from django.views.defaults import page_not_found
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
def handler404(request):
    return render(request, '404.html', status=404)

	
@login_required
def home(request):
        return render(request, template_name='admin.html')

@login_required	
def VistaCerdos(request):
    cer = Cerdos.objects.all()
    return render(request, template_name = "cerdo/list_cerdos.html", context={'cerdo1': cer})
   

@login_required
def VistaPartos(request):
    part = Partos.objects.all()
    return render(request, template_name = "parto/list_partos.html", context={'parto1': part})

#funciones para vacunas
@login_required	
def VistaVacunas(request):
    vac = Vacunas.objects.all()
    return render(request, template_name = "vacuna/list_vacunas.html", context={'vacunas1': vac})



class FiltarGeneroM(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        buscar = 'M'
        cerdo = Cerdos.objects.filter(genero=buscar)
        return render(request,'cerdo/list_cerdos.html', {'cerdo1':cerdo})
class FiltarGeneroH(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        buscar = 'H'
        cerdo = Cerdos.objects.filter(genero=buscar)
        return render(request,'cerdo/list_cerdos.html', {'cerdo1':cerdo})

class BuscarCerdo(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        buscar = request.POST['buscalo']
        cerdo = Cerdos.objects.filter(nombre__contains = buscar)
        return render(request, 'cerdo/list_cerdos.html', {'cerdo1':cerdo})


class BuscarParto(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        buscar = request.POST['buscalo']
        partos = Partos.objects.filter(fecha_parto__contains = buscar)
        return render(request, 'parto/buscar.html', {'parto':partos})

class BuscarVacuna(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        buscar = request.POST['buscalo']
        vacunas = Vacunas.objects.filter(nombre__contains = buscar)
        return render(request, 'vacuna/buscar.html', {'vacunas':vacunas})





#class crear vacuna   
class VacunaCrear(LoginRequiredMixin, CreateView):
    model = Vacunas
    form_class = VacunasForm
    template_name = 'vacuna/agregar_vacuna.html'

    def get_success_url(self):
        return reverse('list_vacunas')
 

#editar vacunas
class VacunaEditar(LoginRequiredMixin,UpdateView):
    model = Vacunas
    form_class = VacunasForm
    template_name = 'vacuna/agregar_vacuna.html'
    success_url = reverse_lazy('list_vacunas')
    @method_decorator(permission_required('Vacunas.change_vacunas',reverse_lazy('list_vacunas')))
    def dispatch(self, *args, **kwargs):
        return super(VacunaEditar, self).dispatch(*args, **kwargs)

#eliminar vacunas
class VacunaEliminar(LoginRequiredMixin,DeleteView):
    model = Vacunas
    form_class = VacunasForm
    template_name = 'vacuna/eliminar_vacuna.html'

    def get_context_data(self, **kwargs):
        context_data = super(VacunaEliminar, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        cer = Vacunas.objects.get(id = int(pk))
        context_data.update({'vacunaEliminar': cer})
        return context_data

    def get_success_url(self):
        return reverse('list_vacunas')


#crear cerdos
class CerdoCrear(LoginRequiredMixin, CreateView):
    model = Cerdos
    form_class = CerdoForm
    template_name = 'cerdo/agregar_cerdo.html'

    def get_success_url(self):
        return reverse('list_cerdos')

#modificar cerdo
class CerdoEditar(LoginRequiredMixin,UpdateView):
    model = Cerdos
    form_class = CerdoForm
    template_name = 'cerdo/agregar_cerdo.html'
    success_url = reverse_lazy('list_cerdos')
    @method_decorator(permission_required('Cerdos.change_cerdos',reverse_lazy('list_cerdos')))
    def dispatch(self, *args, **kwargs):
        return super(CerdoEditar, self).dispatch(*args, **kwargs)


#eliminar cerdo
class CerdoEliminar(LoginRequiredMixin,DeleteView):
    model = Cerdos
    form_class = CerdoForm
    template_name = 'cerdo/eliminar_cerdo.html'

    def get_context_data(self, **kwargs):
        context_data = super(CerdoEliminar, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        cer = Cerdos.objects.get(id = int(pk))
        context_data.update({'cerdoEliminar': cer})
        return context_data

    def get_success_url(self):
        return reverse('list_cerdos')


#partos

#class BuscarCerdo(LoginRequiredMixin, TemplateView):
    
     
    #ef post(self, request, *args, **kwargs):
        #buscar = request.POST['buscalo']
    #    print buscar
     #   datos = []
   #      print cer
 #       return render(request, template_name = 'home_teacher.html',  context={'cerdos1': cer})

#crear pdfs  
class CrearPdfCerdo(LoginRequiredMixin, PDFTemplateView):
    template_name = 'cerdo/pdf.html' 
    pdf_filename = 'Reporte_Clientes.pdf'
    
    def get_context_data(self, **kwargs):
    	cliente = Cerdos.objects.all()
    	return super(CrearPdfCerdo, self).get_context_data(
			object_list = cliente,
			pagesize="B4",
			title="Ficha",
			#today = now(),
			** kwargs
        )
        success_url = reverse_lazy('buscar_cerdo')
    
class CrearPdfCerdo4(LoginRequiredMixin, PDFTemplateView):
    template_name = 'cerdo/pdf1.html' 

    def get_context_data(self, **kwargs):
        return super(CrearPdfCerdo4, self).get_context_data(
            pagesize='A4',
            title='Hi there!',
            **kwargs
        )
    
     

#crear pdfs  
class CrearPdfVacunas(LoginRequiredMixin, PDFTemplateView):
    template_name = 'vacuna/pdf.html' 
    pdf_filename = 'Reporte.pdf'
    
    def get_context_data(self, **kwargs):
        cliente2 = Vacunas.objects.all()
    	return super(CrearPdfVacunas, self).get_context_data(
			object_list2 = cliente2,
			pagesize="B4",
			title="Ficha",
			#today = now(),
			** kwargs
        )
        success_url = reverse_lazy('buscar_vacuna')

#crear pdfs  
class CrearPdfParto(LoginRequiredMixin, PDFTemplateView):
    template_name = 'parto/pdf.html' 
    pdf_filename = 'partos.pdf'
    
    def get_context_data(self, **kwargs):
        cliente1 = Partos.objects.all()
    	return super(CrearPdfParto, self).get_context_data(
			object_list1 = cliente1,
			pagesize="B4",
			title="Ficha",
			#today = now(),
			** kwargs
        )
        success_url = reverse_lazy('buscar_parto')




class FichaPDFView(LoginRequiredMixin, PDFTemplateView):
     template_name = 'cerdo/pdf1.html'
     pdf_filename = 'Reporte.pdf'
     model = Cerdos
     form_class = CerdoForm

     def get_context_data(self, **kwargs):
        buscar = self.request.GET.get("id")
        cerdos = Cerdos.objects.filter(id = buscar)
    	return super(FichaPDFView, self).get_context_data(
			object_list = cerdos,
			pagesize="B4",
			title="Ficha",
			#today = now(),
			** kwargs
        )
        success_url = reverse_lazy('list_cerdos')





class PartosCrea(LoginRequiredMixin, CreateView):
    model = Partos
    form_class = PartosForm
    template_name = 'parto/agregar_parto.html'

    def get_success_url(self):
        return reverse('list_partos')

#editar parto
class PartoEditar(LoginRequiredMixin,UpdateView):
    model = Partos
    form_class = PartosForm
    template_name = 'parto/agregar_parto.html'
    success_url = reverse_lazy('list_vacunas')
    @method_decorator(permission_required('Partos.change_partos',reverse_lazy('list_vacunas')))
    def dispatch(self, *args, **kwargs):
        return super(PartoEditar, self).dispatch(*args, **kwargs)

#eliminar parto
class PartoEliminar( LoginRequiredMixin,DeleteView):
    model = Partos
    form_class = PartosForm
    template_name = 'parto/eliminar_parto.html'

    def get_context_data(self, **kwargs):
        context_data = super(PartoEliminar, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        cer = Partos.objects.get(id = int(pk))
        context_data.update({'partoEliminar': cer})
        return context_data

    def get_success_url(self):
        return reverse('list_partos')