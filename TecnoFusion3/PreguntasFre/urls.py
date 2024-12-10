from django.urls import path
from . import views
"""
Este archivo define las rutas relacionadas con las Preguntas Frecuentes.

Rutas:
    - '': Renderiza la página de preguntas frecuentes.
"""

urlpatterns = [
    path('', views.preguntasFre, name='preguntasF')
]