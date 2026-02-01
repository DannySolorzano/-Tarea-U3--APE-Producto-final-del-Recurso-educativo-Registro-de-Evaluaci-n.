# accesibilidad/urls.py
from django.urls import path
from . import views

# ¡IMPORTANTE! Esta línea define el namespace
app_name = 'accesibilidad'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # INSTITUCIONES
    path('instituciones/', views.lista_instituciones, name='lista_instituciones'),
    path('instituciones/nueva/', views.nueva_institucion, name='nueva_institucion'),
    path('instituciones/<int:institucion_id>/', views.detalle_institucion, name='detalle_institucion'),
    
    # ENCUESTAS - Usa los nombres correctos de tus funciones
    path('encuestas/seleccionar/', views.seleccionar_institucion, name='seleccionar_institucion'),
    path('encuestas/crear/', views.crear_encuesta, name='crear_encuesta'),
    path('encuestas/', views.lista_encuestas, name='lista_encuestas'),
    path('encuestas/<int:encuesta_id>/', views.detalle_encuesta, name='detalle_encuesta'),
]