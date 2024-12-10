
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

"""
Este archivo contiene la configuración de las rutas de la aplicación principal. Aquí se incluyen las rutas para cada una de las aplicaciones dentro del proyecto Django.

Rutas principales:
    - 'admin/': Acceso al panel de administración de Django.
    - '': Redirige a la aplicación de inicio.
    - 'accounts/': Maneja la autenticación a través de `allauth`.
    - 'tienda/': Redirige a la aplicación Tienda.
    - 'donaciones/': Redirige a la aplicación Donaciones.
    - 'preguntasF/': Redirige a la aplicación Preguntas Frecuentes.
    - 'terminos/': Redirige a la aplicación de términos y condiciones.
    - 'contactanos/': Redirige a la aplicación de contacto.
    - 'garantia/': Redirige a la aplicación de Garantía.

Se agregan también las configuraciones necesarias para servir archivos estáticos y medios en modo de desarrollo.
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Inicio.urls')),
    path('accounts/', include('allauth.urls')),
    path('tienda/',include('Tienda.urls')),
    path('donaciones/',include("Donaciones.urls")),
    path('preguntasF/', include("PreguntasFre.urls")),
    path('terminos/', include('terminos.urls')),
    path('contactanos/', include('contacto.urls')),  # Incluir las URLs de la app contacto
    path('garantia/', include('garantia.urls')),  # Incluye la aplicación "garantia"
]

# Agregar esto al final de tus urls.py para servir archivos de medios durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)