from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Donacion(models.Model):
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