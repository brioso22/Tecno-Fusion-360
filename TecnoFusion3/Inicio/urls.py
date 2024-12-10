from django.urls import path
from .import views
"""
Este archivo define las rutas para la sección de inicio.

Rutas:
    - '': Renderiza la página de inicio.
"""

urlpatterns = [
    path('', views.inicio, name=('inicio')),
]