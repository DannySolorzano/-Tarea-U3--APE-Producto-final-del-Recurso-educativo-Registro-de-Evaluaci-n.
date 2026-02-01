from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'inventario'

urlpatterns = [
    # Dashboard
    path('', views.dashboard_inventario, name='dashboard'),
    
    # Ruta para inventario/agregar/ que redirige a agregar equipo
    path('agregar/', RedirectView.as_view(pattern_name='inventario:agregar_equipo'), name='agregar'),
    
    # Equipos
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('equipos/agregar/', views.agregar_equipo, name='agregar_equipo'),
    path('equipos/<int:id>/', views.detalle_equipo, name='detalle_equipo'),
    path('equipos/editar/<int:id>/', views.editar_equipo, name='editar_equipo'),
    
    # Mantenimientos
    path('mantenimientos/', views.lista_mantenimientos, name='lista_mantenimientos'),
    path('mantenimientos/agregar/', views.agregar_mantenimiento, name='agregar_mantenimiento'),
    path('mantenimientos/agregar/<int:equipo_id>/', views.agregar_mantenimiento_equipo, name='agregar_mantenimiento_equipo'),
    
    # Ubicaciones y asignaciones
    path('ubicaciones/agregar/', views.agregar_ubicacion, name='agregar_ubicacion'),
    path('asignaciones/agregar/', views.asignar_equipo, name='asignar_equipo'),
    path('asignaciones/agregar/<int:equipo_id>/', views.asignar_equipo, name='asignar_equipo_especifico'),
]