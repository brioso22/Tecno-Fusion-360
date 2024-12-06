import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, ProductosGuardados, Comentario, Compra,PagoEnLinea, TransferenciaBancaria, DetalleVenta
from datetime import date
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.db.models import Count
from django.views.decorators.csrf import csrf_protect





def tienda(request):
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Filtrar productos con stock mayor o igual a 1
        productos_en_carrito = ProductosGuardados.objects.filter(
            usuario=request.user,
            activo=True,
            cantidad_stock__gte=1  # Filtra solo productos con cantidad_stock >= 1
        )
        cantidad_en_carrito = productos_en_carrito.count()
    else:
        productos_en_carrito = []
        cantidad_en_carrito = 0  # Si no está autenticado, el carrito está vacío

    # Obtiene el valor de 'categoria' desde el parámetro GET
    categoria = request.GET.get('categoria', 'todos')  # Por defecto, muestra 'todos'
    query = request.GET.get('q')  # Obtiene el valor de la búsqueda

    # Filtra los productos por categoría y búsqueda
    if categoria == 'todos':
        productos = Producto.objects.filter(visible=True)  # Solo productos visibles
    else:
        productos = Producto.objects.filter(categoria=categoria, visible=True)

    # Filtra por búsqueda, si se ingresó una consulta
    if query:
        productos = productos.filter(nombre__icontains=query)

    # Devuelve la plantilla con los productos filtrados, búsqueda y cantidad de carrito
    return render(request, 'tienda.html', {
        'productos': productos,
        'categoria': categoria,
        'query': query,
        'carrito': productos_en_carrito,
        'cantidad_en_carrito': cantidad_en_carrito
    })



def sugerencias(request):
    query = request.GET.get('q', '')
    if query:
        # Filtrar productos por nombre que contengan el término de búsqueda
        productos = Producto.objects.filter(nombre__icontains=query, visible=True)[:5]  # Limitar los resultados
        sugerencias = [
            {'nombre': producto.nombre, 'precio': producto.precio, 'categoria': producto.categoria.nombre}
            for producto in productos
        ]
        return JsonResponse({'sugerencias': sugerencias})
    else:
        return JsonResponse({'sugerencias': []})


def tienda_movil(request):
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Filtrar productos con stock mayor o igual a 1
        productos_en_carrito = ProductosGuardados.objects.filter(
            usuario=request.user,
            activo=True,
            cantidad_stock__gte=1  # Filtra solo productos con cantidad_stock >= 1
        )
        cantidad_en_carrito = productos_en_carrito.count()
    else:
        productos_en_carrito = []
        cantidad_en_carrito = 0  # Si no está autenticado, el carrito está vacío

    # Obtiene el valor de 'categoria' desde el parámetro GET
    categoria = request.GET.get('categoria', 'todos')  # Por defecto, muestra 'todos'
    query = request.GET.get('q')  # Obtiene el valor de la búsqueda

    # Filtra los productos por categoría y búsqueda
    if categoria == 'todos':
        productos = Producto.objects.filter(visible=True)  # Solo productos visibles
    else:
        productos = Producto.objects.filter(categoria=categoria, visible=True)

    # Filtra por búsqueda, si se ingresó una consulta
    if query:
        productos = productos.filter(nombre__icontains=query)

    # Devuelve la plantilla con los productos filtrados, búsqueda y cantidad de carrito
    return render(request, 'tienda_movil.html', {
        'productos': productos,
        'categoria': categoria,
        'query': query,
        'carrito': productos_en_carrito,
        'cantidad_en_carrito': cantidad_en_carrito
    })

#def tienda_movil(request):
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        productos_en_carrito = ProductosGuardados.objects.filter(usuario=request.user, activo=True)
    else:
        productos_en_carrito = []  # Si el usuario no está autenticado, no hay productos en el carrito

    # Obtiene el valor de 'categoria' desde el parámetro GET
    categoria = request.GET.get('categoria', 'todos')  # Por defecto, muestra 'todos'
    query = request.GET.get('q')  # Obtiene el valor de la búsqueda

    # Filtra los productos por categoría y búsqueda
    if categoria == 'todos':
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(categoria=categoria)

    # Filtra por búsqueda, si se ingresó una consulta
    if query:
        productos = productos.filter(nombre__icontains=query)

    # Devuelve la plantilla con los productos filtrados y la búsqueda
    return render(request, 'tienda_movil.html', {'productos': productos, 'categoria': categoria, 'query': query, 'carrito': productos_en_carrito})




@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    usuario = request.user

    # Lógica para agregar al carrito
    producto_guardado = ProductosGuardados.objects.filter(producto=producto, usuario=usuario, activo=True).first()
    
    if producto_guardado:
        producto_guardado.cantidad_stock += 1
        producto_guardado.save()
    else:
        ProductosGuardados.objects.create(
            producto=producto,
            usuario=usuario,
            cantidad_stock=1,
            descripcion=producto.descripcion,
            fecha_guardado=date.today(),
            activo=True
        )
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  



@login_required
def agregar_comentario(request, producto_id):
    if request.method == 'POST':
        texto = request.POST.get('texto')
        calificacion = request.POST.get('rate')  # Cambiar de 'calificacion' a 'rate'
        producto = get_object_or_404(Producto, id=producto_id)
        
        comentario = Comentario(
            texto=texto, 
            usuario=request.user, 
            producto=producto,
            calificacion=calificacion
        )
        comentario.save()

        return redirect('vista_product', id=producto.id) 
    return redirect('vista_product', id=producto_id)



def detalle_producto(request, id):
    # Obtener el producto
    producto = get_object_or_404(Producto, id=id)
    
    # Obtener los comentarios relacionados con el producto
    comentarios = producto.comentarios.all()
    
    # Añadir rango de estrellas para cada comentario
    for comentario in comentarios:
        comentario.star_range = range(comentario.calificacion or 0)  # Rango de estrellas basado en la calificación
        # Añadir la fecha formateada en el comentario
        comentario.fecha_formateada = comentario.fecha.strftime('%d/%m/%Y %H:%M')

    # Preparar rango de estrellas para la calificación promedio
    calificacion_promedio = producto.calificacion_promedio
    producto.promedio_stars = range(int(calificacion_promedio)) if calificacion_promedio else range(0)

    # Calificaciones por estrellas para mostrar el porcentaje de cada tipo de calificación
    calificaciones = comentarios.values('calificacion').annotate(count=Count('calificacion'))
    calificaciones_dict = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
    
    for calificacion in calificaciones:
        calificaciones_dict[calificacion['calificacion']] = calificacion['count']
    
    total_comentarios = comentarios.count()
    calificaciones_porcentajes = {
        key: (value / total_comentarios * 100) if total_comentarios > 0 else 0
        for key, value in calificaciones_dict.items()
    }

    # Generar la lista de estrellas (de 5 a 1)
    estrellas = [5, 4, 3, 2, 1]

    # Asegurarse de que las compras también estén disponibles para verificar la compra del usuario
    compras_usuario = Compra.objects.filter(usuario=request.user, detalles_venta__producto=producto)

    # Preparar los detalles de la compra y la verificación de la compra
    for comentario in comentarios:
        # Verificar si el producto fue comprado por el usuario
        comentario.compra_verificada = producto in [detalle.producto for compra in compras_usuario for detalle in compra.detalles_venta.all()]
        # Si es verificado, obtener la fecha de compra
        if comentario.compra_verificada:
            for compra in compras_usuario:
                for detalle in compra.detalles_venta.all():
                    if detalle.producto == producto:
                        comentario.fecha_compra = compra.fecha_compra.strftime('%d/%m/%Y')

    return render(request, 'vista_product.html', {
        'producto': producto,
        'comentarios': comentarios,
        'calificaciones_porcentajes': calificaciones_porcentajes,
        'total_comentarios': total_comentarios,
        'estrellas': estrellas,
        'compras_usuario': compras_usuario,  # Pasamos las compras del usuario
    })


@login_required  # Cambia @csrf_protect por @login_required
def marcar_utilidad_reseña(request, comentario_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            utilidad = data.get("utilidad")
            
            if utilidad in ['si', 'no']:
                comentario = Comentario.objects.get(id=comentario_id)
                
                # Elimina la restricción de que solo el autor puede marcar
                comentario.utilidad = utilidad
                comentario.save()
                return JsonResponse({'success': True, 'utilidad': utilidad})
            else:
                return JsonResponse({'success': False, 'error': 'Respuesta inválida'})
        except Comentario.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Comentario no encontrado'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Método no permitido'})


@login_required
def proceso_compra(request):
    productos_en_carrito = ProductosGuardados.objects.filter(usuario=request.user)

    if request.method == 'POST':
        # Crear la compra
        compra = Compra.objects.create(
            nombre_completo=request.POST.get('nombre_completo'),
            correo_electronico=request.POST.get('correo_electronico'),
            numero_telefono=request.POST.get('numero_telefono'),
            departamento=request.POST.get('departamento'),
            ciudad=request.POST.get('ciudad'),
            direccion=request.POST.get('direccion'),
            codigo_postal=request.POST.get('codigo_postal', None),
            usuario=request.user,
        )

        # Obtener los productos seleccionados
        selected_product_ids = request.POST.get('selected_products', '').split(',')
        selected_product_ids = [pid for pid in selected_product_ids if pid]  # Eliminar cadenas vacías

        # Procesar productos seleccionados
        for item in productos_en_carrito:
            if str(item.producto.id) in selected_product_ids:
                cantidad = item.cantidad_stock
                precio_unitario = item.producto.precio
                precio_total = cantidad * precio_unitario

                # Crear el detalle de venta
                DetalleVenta.objects.create(
                    compra=compra,
                    producto=item.producto,
                    cantidad=cantidad,
                    precio_unitario=precio_unitario,
                    precio_total=precio_total,
                    is_selected=True
                )

                # Restar el stock del producto principal
                if item.producto.stock >= cantidad:
                    item.producto.stock -= cantidad
                else:
                    # Opcional: Manejo de casos donde el stock no es suficiente
                    return HttpResponse("Error: stock insuficiente para el producto.")

                # Guardar cambios en el modelo Producto
                item.producto.save()

                # Establecer el stock del producto guardado a cero
                item.cantidad_stock = 0
                item.save()

        # Manejo de método de pago
        metodo_pago = request.POST.get('payment-method')
        if metodo_pago == 'online':
            PagoEnLinea.objects.create(
                compra=compra,
                numero_tarjeta=request.POST.get('numero_tarjeta'),
                fecha_vencimiento=request.POST.get('fecha_vencimiento'),
                codigo_seguridad=request.POST.get('codigo_seguridad'),
                nombre_tarjeta=request.POST.get('nombre_tarjeta'),
            )
        elif metodo_pago == 'transfer':
            TransferenciaBancaria.objects.create(
                compra=compra,
                nombre_banco=request.POST.get('nombre_banco'),
                numero_cuenta=request.POST.get('numero_cuenta'),
                titular_cuenta=request.POST.get('titular_cuenta'),
                monto_transferido=request.POST.get('monto_transferido'),
                fecha_transferencia=request.POST.get('fecha_transferencia'),
                numero_referencia=request.POST.get('numero_referencia'),
                comprobante=request.FILES.get('comprobante'),
            )

        return HttpResponse("Compra guardada exitosamente.")
    
    return render(request, 'ProceCom.html', {'carrito': productos_en_carrito})



#def proceso_compra(request):
    if request.method == 'POST':
        # Capturamos los datos del formulario
        nombre_completo = request.POST.get('nombre_completo')
        correo_electronico = request.POST.get('correo_electronico')
        numero_telefono = request.POST.get('numero_telefono')
        departamento = request.POST.get('departamento')
        ciudad = request.POST.get('ciudad')
        direccion = request.POST.get('direccion')
        codigo_postal = request.POST.get('codigo_postal', '')  # Código postal opcional
        
        # Guardamos los datos en la base de datos
        Compra.objects.create(
            nombre_completo=nombre_completo,
            correo_electronico=correo_electronico,
            numero_telefono=numero_telefono,
            departamento=departamento,
            ciudad=ciudad,
            direccion=direccion,
            codigo_postal=codigo_postal
        )
        
        # Redirigir o mostrar un mensaje de éxito
        return HttpResponse("Compra guardada exitosamente.")
    
    # Si no es POST, renderizamos un formulario (opcional)
    return render(request, 'ProceCom.html')



#def proceso_Compra(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        for key in request.POST:
            if key.startswith('toggler-'):
                producto_id = key.split('-')[1]
                is_selected = request.POST.get(key) == '1'

                # Buscar el producto correspondiente
                try:
                    item = ProductosGuardados.objects.get(producto__id=producto_id, usuario=request.user)
                    item.producto.is_selected = is_selected
                    item.producto.save()
                except ProductosGuardados.DoesNotExist:
                    return JsonResponse({'error': 'Producto no encontrado'}, status=404)

        return JsonResponse({'success': True, 'message': 'Estado actualizado correctamente'})

    # Renderizado normal para GET
    productos_en_carrito = ProductosGuardados.objects.filter(usuario=request.user)
    return render(request, 'ProceCom.html', {'carrito': productos_en_carrito})




