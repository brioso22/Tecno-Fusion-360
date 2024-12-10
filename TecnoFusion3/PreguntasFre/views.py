from django.shortcuts import render

"""
Este archivo define la vista para la página de Preguntas Frecuentes.

Vistas:
    - `preguntasFre`: Renderiza la plantilla que muestra las preguntas frecuentes.
"""

# Create your views here.
def preguntasFre(request):
    """
    Renderiza la página de preguntas frecuentes.

    Parámetros:
        - `request`: Objeto HttpRequest que contiene la información de la solicitud.

    Retorna:
        - Un objeto HttpResponse que renderiza la plantilla 'preguntasFre.html'.
    """
    return render(request,'preguntasFre.html')