from django.urls import path
from . import views

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





