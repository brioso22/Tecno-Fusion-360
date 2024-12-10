from django.urls import path
from . import views
"""
Este archivo define las rutas para la sección de contacto.

Rutas:
    - '': Renderiza el formulario de contacto.
"""

urlpatterns = [
    path('', views.contactanos, name='contactanos'),
]
