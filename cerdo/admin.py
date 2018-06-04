# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Cerdo':
            kwargs['queryset'] = Cerdo.objects.filter(genero='M').order_by('fecha_parto')
        return super(ConsumerAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class VistaCerdo(admin.ModelAdmin):
	
	list_display = ['nombre', 'genero', 'peso', 'status']
	list_filter = ['status', 'genero']
	search_fields = ['nombre']

class VistaVacuna(admin.ModelAdmin):
    	
	list_display = ['nombre', 'cerdo', 'descripcion', 'status']
	list_filter = ['status']
	search_fields = ['nombre']

class VistaParto(admin.ModelAdmin):
    	
	list_display = ['cerdo', 'fecha_gestacion', 'fecha_parto', 'numero_partos','cantidad_por_parto']
	list_filter = ['status', 'fecha_parto']
	search_fields = ['cerdo']

admin.site.register(Cerdos, VistaCerdo)
admin.site.register(Vacunas, VistaVacuna)
admin.site.register(Partos, VistaParto)

