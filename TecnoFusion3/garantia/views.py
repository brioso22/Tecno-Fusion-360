from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Garantia

def formulario_garantia(request):
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
