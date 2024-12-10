from django.db import models
"""
Este archivo define el modelo de Contacto para almacenar los mensajes de los usuarios.

Modelo:
    - `Contacto`: Almacena la información de los mensajes enviados por los usuarios.
"""

class Contacto(models.Model):
    """
    Modelo que almacena los mensajes de contacto de los usuarios.

    Campos:
        - `nombre`: Nombre del usuario que envía el mensaje.
        - `email`: Correo electrónico del usuario.
        - `telefono`: Número de teléfono del usuario.
        - `mensaje`: El mensaje enviado por el usuario.
        - `fecha`: Fecha en la que se envió el mensaje (automática).
    """
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)  # Guarda la fecha de envío

    def __str__(self):
        """
        Representación legible del objeto Contacto.
        Devuelve una cadena con el nombre del contacto.
        """
        return f"Mensaje de {self.nombre}"
