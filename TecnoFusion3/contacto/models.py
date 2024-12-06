from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)  # Guarda la fecha de envío

    def __str__(self):
        return f"Mensaje de {self.nombre}"
