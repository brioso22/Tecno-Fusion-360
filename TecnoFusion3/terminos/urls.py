from django.urls import path
from . import views
"""
Este archivo define las rutas para la sección de servicios.

Rutas:
    - '': Renderiza la página principal de servicios.
"""

urlpatterns = [
    path('', views.index, name='terminos'),
]