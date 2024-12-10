from django.urls import path
from . import views
"""
Este archivo define las rutas de la aplicación relacionadas con el manejo de solicitudes de garantía.

Rutas:
    - '': Renderiza el formulario para enviar solicitudes de garantía.
"""

urlpatterns = [
    path('', views.formulario_garantia, name='formulario_garantia'),  # Define la URL con el nombre correcto
]
