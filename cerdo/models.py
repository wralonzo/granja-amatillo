# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

GENERO_CHOICES = (
    ('M', 'Macho'),
    ('H', 'Hembra'),
)

class Cerdos(models.Model):
	nombre = models.CharField('Nombre', max_length=50)
	genero = models.CharField(
        'Genero Animal', max_length=1,
        choices=GENERO_CHOICES, default='M')
	peso = models.CharField('Peso', max_length=50)
	status = models.BooleanField(default=True)

	def __str__(self):
		return '{}'.format(self.nombre)	

	class Meta:
		verbose_name = "Cerdos"
		verbose_name_plural = "Cerdos"


class Vacunas(models.Model):
	nombre = models.CharField('Nombre', max_length=50)
	cerdo = models.ForeignKey(Cerdos, null = True)
	descripcion = models.TextField('Descripcion')
	status = models.BooleanField(default=True)

	def __str__(self):
		return '{}'.format(self.nombre)
	class Meta:
		verbose_name = "Vacuna"
		verbose_name_plural = "Vacunas"

class Partos(models.Model):
	cerdo = models.ForeignKey(Cerdos, null = True)
	fecha_gestacion = models.DateField('Fecha de Gestacion')
	fecha_parto = models.DateField('Fecha de parto')
	numero_partos = models.IntegerField('Numero de partos')
	cantidad_por_parto = models.IntegerField('Cantidad de animales por parto')
	status = models.BooleanField(default=True)
	def __str__(self):
    		return '{}'.format(self.cerdo)
	class Meta:
   		verbose_name = "Parto"
		verbose_name_plural = "Partos"

def full_cerdo(self):
	return u'{} {} {}'.format(self.nombre, self.genero, self.peso)

def full_partos(self):
	return u'{} {} {} {} {}'.format(self.cerdo, self.fecha_gestacion, self.fecha_parto, self.numero_partos, self.cantidad_por_parto)

def full_vacunas(self):
	return u'{} {} {}'.format(self.nombre, self.cerdo, self.descripcion)