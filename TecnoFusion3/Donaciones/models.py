from django.db import models
from django.contrib.auth.models import User

"""
Este archivo define el modelo `Donacion` que representa las donaciones registradas por los usuarios.

Modelo:
    - Donacion: Almacena la información de una donación, incluyendo los detalles del equipo, la empresa y el usuario que realizó la donación.
"""

# Create your models here.
class Donacion(models.Model):
    """
    Modelo que representa una donación registrada.

    Campos:
        - `nombre_empresa`: Nombre de la empresa donante.
        - `rubro_empresa`: Rubro de la empresa.
        - `descripcion_equipo`: Descripción de los equipos donados.
        - `fecha_entrega`: Fecha propuesta para la entrega de los equipos.
        - `ubicacion_donante`: Ubicación del donante.
        - `comentarios_adicionales`: Comentarios adicionales sobre la donación.
        - `terminos`: Indica si se aceptaron los términos y condiciones.
        - `usuario`: Usuario autenticado que realizó la donación.
    """

    nombre_empresa = models.CharField(max_length=255, default="Empresa desconocida")
    rubro_empresa = models.CharField(max_length=255, default="rubro desconocida")
    descripcion_equipo = models.TextField(default="Sin descripción")
    fecha_entrega = models.DateField(null=True, blank=True)
    ubicacion_donante = models.CharField(max_length=255, default="Ubicación desconocida")
    comentarios_adicionales = models.TextField(blank=True, null=True)
    terminos = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  


    def __str__(self):
        return self.nombre_empresa