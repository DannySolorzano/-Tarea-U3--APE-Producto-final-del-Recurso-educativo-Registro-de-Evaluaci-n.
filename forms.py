from django import forms
from .models import Equipo, Ubicacion, Mantenimiento, AsignacionEquipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            'codigo_inventario', 'tipo', 'marca', 'modelo', 
            'numero_serie', 'anio_adquisicion', 'costo',
            'estado', 'condicion_fisica', 'descripcion'
        ]
        widgets = {
            'anio_adquisicion': forms.NumberInput(attrs={
                'min': 2000,
                'max': 2100,
                'class': 'form-control'
            }),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
        labels = {
            'codigo_inventario': 'Código de Inventario',
            'tipo': 'Tipo de Equipo',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'numero_serie': 'Número de Serie',
            'anio_adquisicion': 'Año de Adquisición',
            'costo': 'Costo ($)',
            'estado': 'Estado',
            'condicion_fisica': 'Condición Física',
            'descripcion': 'Descripción',
        }

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['area', 'aula_laboratorio', 'piso', 'edificio', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
        labels = {
            'area': 'Área',
            'aula_laboratorio': 'Aula/Laboratorio',
            'piso': 'Piso',
            'edificio': 'Edificio',
            'descripcion': 'Descripción',
        }

class AsignacionEquipoForm(forms.ModelForm):
    class Meta:
        model = AsignacionEquipo
        fields = ['equipo', 'ubicacion', 'responsable', 'observaciones']
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
        labels = {
            'equipo': 'Equipo',
            'ubicacion': 'Ubicación',
            'responsable': 'Responsable',
            'observaciones': 'Observaciones',
        }

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = [
            'equipo', 'tipo', 'fecha', 'descripcion',
            'actividades_realizadas', 'repuestos',
            'costo_mantenimiento', 'estado_posterior',
            'observaciones', 'proximo_mantenimiento'
        ]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'proximo_mantenimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'actividades_realizadas': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'repuestos': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'costo_mantenimiento': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'estado_posterior': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'equipo': 'Equipo',
            'tipo': 'Tipo de Mantenimiento',
            'fecha': 'Fecha de Mantenimiento',
            'descripcion': 'Descripción',
            'actividades_realizadas': 'Actividades Realizadas',
            'repuestos': 'Repuestos Utilizados',
            'costo_mantenimiento': 'Costo de Mantenimiento ($)',
            'estado_posterior': 'Estado Posterior',
            'observaciones': 'Observaciones',
            'proximo_mantenimiento': 'Próximo Mantenimiento',
        }