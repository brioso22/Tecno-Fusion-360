from django.urls import path
from . import views

"""
Este archivo define las rutas de la aplicación y los controladores asociados a cada una.

Rutas:
    - '': Muestra la tienda principal.
    - 'tienda_movil': Muestra la versión móvil de la tienda.
    - 'vista_product/<int:id>/': Muestra el detalle de un producto específico.
    - 'comentarios/agregar/<int:producto_id>/': Permite agregar un comentario a un producto.
    - 'agregar_al_carrito/<int:producto_id>/': Agrega un producto al carrito del usuario.
    - 'compra/': Procesa la compra de productos.
    - 'marcar_utilidad_reseña/<int:comentario_id>/': Marca una reseña como útil o no.
    - 'sugerencias/': Proporciona sugerencias de productos según un término de búsqueda.
"""

urlpatterns = [
    path('',views.tienda, name='tienda'),
    path('tienda_movil',views.tienda_movil, name='tienda_movil'),

    path('vista_product/<int:id>/', views.detalle_producto, name='vista_product'),  # Ruta correcta para el detalle del producto
    
    path('comentarios/agregar/<int:producto_id>/', views.agregar_comentario, name='agregar_comentario'),  # Ruta con parámetro
    
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),



    path('compra/', views.proceso_compra, name='proceso_compra'),
    path('marcar_utilidad_reseña/<int:comentario_id>/', views.marcar_utilidad_reseña, name='marcar_utilidad_reseña'),
    path('sugerencias/', views.sugerencias, name='sugerencias'),

]





