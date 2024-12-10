from django.db import models
"""
Este archivo define el modelo `Garantia` que representa las solicitudes de garantía enviadas por los clientes.

Modelo:
    - Garantia: Almacena información sobre solicitudes de garantía, incluyendo datos del cliente, detalles del producto y fecha de la solicitud.
"""

class Garantia(models.Model):

    """
    Modelo que representa una solicitud de garantía.

    Campos:
        - `nombre`: Nombre del cliente.
        - `factura`: Número de factura del producto.
        - `doc`: Documento de identidad del cliente.
        - `email`: Dirección de correo electrónico del cliente.
        - `telefono`: Número de teléfono del cliente.
        - `mensaje`: Descripción de la falla o problema del producto.
        - `fecha`: Fecha en la que se creó la solicitud.
    """
    nombre = models.CharField(max_length=100)
    factura = models.CharField(max_length=50)
    doc = models.CharField(max_length=20)  # Documento de identidad
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()  # Descripción de la falla
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Devuelve una representación legible del modelo en formato:
        "Solicitud de garantía de [nombre] - Factura: [factura]".
        """
        return f"Solicitud de garantía de {self.nombre} - Factura: {self.factura}"
