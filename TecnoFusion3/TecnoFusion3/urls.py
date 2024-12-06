
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


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