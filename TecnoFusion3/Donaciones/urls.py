from django.urls import path
from . import views
"""
Este archivo define las rutas relacionadas con la funcionalidad de donaciones.

Rutas:
    - '': Renderiza la página principal de donaciones.
    - 'registrar-donacion/': Permite registrar una nueva donación.
"""

urlpatterns = [
    path('', views.donaciones, name='donaciones'),
    path('registrar-donacion/', views.registrar_donacion, name='registrar_donacion'),
]