from django.db import models

class Garantia(models.Model):
    nombre = models.CharField(max_length=100)
    factura = models.CharField(max_length=50)
    doc = models.CharField(max_length=20)  # Documento de identidad
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()  # Descripción de la falla
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de garantía de {self.nombre} - Factura: {self.factura}"
