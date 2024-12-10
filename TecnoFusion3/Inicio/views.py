from django.shortcuts import render
"""
Este archivo contiene la vista principal para la sección de inicio.

Vistas:
    - `inicio`: Renderiza la página de inicio.
"""

# Create your views here.
def inicio(request):
    """
    Renderiza la página de inicio.

    Parámetros:
        - `request`: Objeto HttpRequest que contiene la información de la solicitud.

    Retorna:
        - Un objeto HttpResponse que renderiza la plantilla 'inicio.html'.
    """
    return render(request,'inicio.html')
