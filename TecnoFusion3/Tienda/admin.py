from django.contrib import admin
from . import models
"""
Este archivo configura la administración de modelos en Django para facilitar su gestión desde el panel de administración.

Modelos registrados:
    - Producto: Administra productos con opciones de filtro y búsqueda.
    - ProductosGuardados: Administra productos guardados por usuarios.

Configuración del modelo Producto:
    - `list_display`: Campos que se muestran en la lista de productos (nombre, precio, categoría, stock, visibilidad).
    - `list_filter`: Permite filtrar productos por visibilidad y categoría.
    - `search_fields`: Permite buscar productos por nombre.
"""
class ProductoAdmin(admin.ModelAdmin):
    """
    Configuración personalizada para el modelo Producto en el panel de administración.

    Opciones:
        - `list_display`: Campos visibles en la lista de productos.
        - `list_filter`: Filtros disponibles en la vista de productos.
        - `search_fields`: Campos por los que se puede buscar.
    """
    list_display = ('nombre', 'precio', 'categoria', 'stock', 'visible')  # Muestra el campo visible en la lista
    list_filter = ('visible', 'categoria')  # Permite filtrar por visibilidad y categoría
    search_fields = ('nombre',)  # Permite buscar productos por nombre

admin.site.register(models.Producto, ProductoAdmin)


admin.site.register(models.ProductosGuardados)