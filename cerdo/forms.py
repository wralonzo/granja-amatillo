from django import forms
from cerdo.models import Cerdos, Partos, Vacunas
from django.contrib.admin import widgets  

class CerdoForm(forms.ModelForm):
    class Meta:
        model = Cerdos
        fields = '__all__'
        widgets = {
            'nombre': forms.DateInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'peso': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
##buscar cerdo


class PartosForm(forms.ModelForm):
    class Meta:
        model = Partos
        fields = '__all__'
        widgets = {
            'cerdo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_gestacion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_parto': forms.DateInput(attrs={'class': 'form-control'}),
            'numero_partos': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_por_parto': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
class VacunasForm(forms.ModelForm):
    class Meta:
        model = Vacunas
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            
            'cerdo': forms.Select(attrs={'class': 'form-control' }),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

