from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contacto
"""
Este archivo contiene las vistas para la sección de contacto.

Vistas:
    - `contactanos`: Renderiza el formulario de contacto y guarda los datos enviados.
"""

def contactanos(request):
    """
    Muestra el formulario de contacto y guarda la información cuando se envía.

    Parámetros:
        - `request`: Objeto HttpRequest que contiene la información de la solicitud.

    Retorna:
        - Un objeto HttpResponse que renderiza la plantilla 'contacto/contactanos.html'.
        - Si la solicitud es POST, guarda los datos de contacto en la base de datos y valida que todos los campos estén completos.
    """
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        mensaje = request.POST.get('mensaje')

        # Validación simple
        if not (nombre and email and telefono and mensaje):
            return HttpResponse("Por favor, completa todos los campos.", status=400)

        # Guardar en la base de datos
        contacto = Contacto(nombre=nombre, email=email, telefono=telefono, mensaje=mensaje)
        contacto.save()


    return render(request, 'contacto/contactanos.html')
