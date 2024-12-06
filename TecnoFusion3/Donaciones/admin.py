from django.contrib import admin
from .models import Donacion
import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.db import models

class DonacionAdmin(admin.ModelAdmin):
    list_display = ['nombre_empresa', 'rubro_empresa', 'fecha_entrega', 'usuario']
    search_fields = ['nombre_empresa', 'rubro_empresa']
    list_filter = ['fecha_entrega']

    # Acción personalizada para mostrar la gráfica
    def changelist_view(self, request, extra_context=None):
        # Datos para la gráfica (empresas y cantidad de donaciones)
        donaciones_por_empresa = Donacion.objects.values('nombre_empresa').annotate(total_donaciones=models.Count('id')).order_by('-total_donaciones')[:10]
        empresas = [donacion['nombre_empresa'] for donacion in donaciones_por_empresa]
        cantidad_donaciones = [donacion['total_donaciones'] for donacion in donaciones_por_empresa]

        # Crear la gráfica usando matplotlib
        plt.figure(figsize=(10, 6))
        plt.bar(empresas, cantidad_donaciones, color='skyblue')
        plt.title('Empresas que más donan')
        plt.xlabel('Empresa')
        plt.ylabel('Cantidad de Donaciones')
        plt.xticks(rotation=45, ha='right')
        
        # Guardar la imagen en un buffer de memoria para mostrarla en el admin
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        
        # Crear la respuesta HTTP con la imagen
        response = HttpResponse(buffer, content_type='image/png')
        response['Content-Disposition'] = 'inline; filename="donaciones_graph.png"'

        # Retornar la respuesta con la gráfica directamente
        extra_context = extra_context or {}
        extra_context['graph_image'] = response
        
        # Aquí es donde pasamos la plantilla personalizada
        return TemplateResponse(request, 'admin/donacion_graph.html', extra_context)

admin.site.register(Donacion, DonacionAdmin)
