from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contacto

def contactanos(request):
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
