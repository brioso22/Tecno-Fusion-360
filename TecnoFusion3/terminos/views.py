# servicios/views.py
from django.shortcuts import render
"""
Este archivo contiene la vista principal para la sección de servicios.

Vistas:
    - `index`: Renderiza la página principal de servicios.
"""
def index(request):
    """
    Renderiza la página principal de servicios.

    Parámetros:
        - `request`: Objeto HttpRequest que contiene la información de la solicitud.

    Retorna:
        - Un objeto HttpResponse que renderiza la plantilla 'index.html'.
    """
    return render(request, 'index.html')

