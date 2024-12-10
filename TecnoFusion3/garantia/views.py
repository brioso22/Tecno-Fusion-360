from django.shortcuts import render, redirect
from .models import Garantia
"""
Este archivo define las vistas relacionadas con la funcionalidad de solicitudes de garantía.

Vistas:
    - `formulario_garantia`: Gestiona el formulario para enviar solicitudes de garantía. Permite guardar los datos en la base de datos y renderiza una plantilla HTML.
"""
def formulario_garantia(request):
    """
    Procesa la solicitud de garantía enviada a través de un formulario.

    Métodos:
        - GET: Renderiza el formulario de garantía.
        - POST: Recibe los datos del formulario y los guarda en la base de datos.

    Parámetros:
        - `request`: Objeto HttpRequest que contiene la información de la solicitud.

    Retorna:
        - Un objeto HttpResponse que renderiza la plantilla 'garantia/formulario_garantia.html'.
    """
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        factura = request.POST.get('factura')
        doc = request.POST.get('doc')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        mensaje = request.POST.get('mensaje')

        # Guardar en la base de datos
        nueva_garantia = Garantia(
            nombre=nombre,
            factura=factura,
            doc=doc,
            email=email,
            telefono=telefono,
            mensaje=mensaje
        )
        nueva_garantia.save()

    return render(request, 'garantia/formulario_garantia.html')
