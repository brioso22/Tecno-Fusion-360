from django.contrib import admin
from . import models

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'stock', 'visible')  # Muestra el campo visible en la lista
    list_filter = ('visible', 'categoria')  # Permite filtrar por visibilidad y categoría
    search_fields = ('nombre',)  # Permite buscar productos por nombre

admin.site.register(models.Producto, ProductoAdmin)


admin.site.register(models.ProductosGuardados)