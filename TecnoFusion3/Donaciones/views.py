from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Donacion
from django.core.mail import send_mail

# Create your views here.
def donaciones(request):
    return render(request, 'donaciones.html')

@login_required
def registrar_donacion(request):
    if request.method == 'POST':
        nombre_empresa = request.POST.get('nombre_empresa')
        rubro_empresa = request.POST.get('rubro_empresa')
        descripcion_equipo = request.POST.get('descripcion_equipo')
        fecha_entrega = request.POST.get('fecha_entrega')
        ubicacion_donante = request.POST.get('ubicacion_donante')
        comentarios_adicionales = request.POST.get('comentarios_adicionales')
        terminos = request.POST.get('terminos') == 'on'

        donacion = Donacion(
            nombre_empresa=nombre_empresa,
            rubro_empresa=rubro_empresa,
            descripcion_equipo=descripcion_equipo,
            fecha_entrega=fecha_entrega,
            ubicacion_donante=ubicacion_donante,
            comentarios_adicionales=comentarios_adicionales,
            terminos=terminos,
            usuario=request.user  
        )
        donacion.save()

        # Enviar correo al usuario confirmando la donación
        send_mail(
            'Confirmación de Donación',
            'Tu solicitud de donación ha sido enviada con éxito.',
            'tecnofusion360t@gmail.com',  
            [request.user.email],  
            fail_silently=False,
        )

        # Enviar correo al anfitrión (correo del administrador)
        send_mail(
            'Nueva Donación Recibida',
            f'Una nueva donación ha sido registrada.\n\n'
            f'Nombre de la empresa: {nombre_empresa}\n'
            f'Rubro de la empresa: {rubro_empresa}\n'
            f'Descripción del equipo: {descripcion_equipo}\n'
            f'Fecha de entrega: {fecha_entrega}\n'
            f'Ubicación del donante: {ubicacion_donante}\n'
            f'Comentarios adicionales: {comentarios_adicionales}\n\n'
            f'Información del donante:\n'
            f'Nombre del usuario: {request.user.get_full_name()}\n'
            f'Correo del usuario: {request.user.email}',
            'tecnofusion360t@gmail.com',  # Aquí puedes colocar el correo del anfitrión (administrador)
            ['admin@tucorreo.com'],  # Reemplaza con el correo del administrador
            fail_silently=False,
        )

        messages.success(request, 'Donación registrada con éxito. Se ha enviado un correo de confirmación.')
        return redirect('tienda')  

    return render(request, 'donaciones.html')
