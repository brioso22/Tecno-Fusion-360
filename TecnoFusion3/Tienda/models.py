from time import timezone
from django.db import models
from django.contrib.auth.models import User  # Utilizando el modelo de usuario por defecto de Django
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg



class Producto(models.Model):
    ESTADO_CHOICES = [
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado'),
    ]

    CATEGORIAS_INICIALES = [
        ("Motherboard", "Motherboard"),
        ("RAM", "RAM"),
        ("Almacenamiento", "Almacenamiento"),
        ("Teclados", "Teclados"),
        ("Mouses", "Mouses"),
        ("Monitores", "Monitores"),
        ("Sillas", "Sillas"),
        ("Escritorios", "Escritorios"),
    ]

    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='nuevo')
    categoria = models.CharField(max_length=50, choices=CATEGORIAS_INICIALES)  # Ccccategoría como opción
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    promedio_calificacion = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)  # Campo para almacenar el promedio
    stock = models.PositiveIntegerField(default=0)  # Campo para almacenar la cantidad de stock disponible
    visible = models.BooleanField(default=True)  # Campo para controlar la visibilidad del producto



    @property
    def calificacion_promedio(self):
        comentarios = self.comentarios.all()
        if comentarios:
            return comentarios.aggregate(Avg('calificacion'))['calificacion__avg'] or 0
        return 0
    


class ProductosGuardados(models.Model):
    descripcion = models.CharField(max_length=100)
    cantidad_stock = models.IntegerField()
    fecha_guardado = models.DateField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #is_selected = models.BooleanField(default=False)  # Agregar este campo


class Compra(models.Model):
    # Información de contacto
    nombre_completo = models.CharField(max_length=255)
    correo_electronico = models.EmailField(verbose_name="Correo electrónico")
    numero_telefono = models.CharField(max_length=20, verbose_name="Número de teléfono")
    
    # Dirección de envío
    departamento = models.CharField(max_length=100, verbose_name="Departamento")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    codigo_postal = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name="Código Postal"
    )

    fecha_compra = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Compra")

    # Usuario que realizó la compra
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="compras",
        verbose_name="Usuario"
    )

    def __str__(self):
        return f"Compra de {self.nombre_completo} - {self.fecha_compra.strftime('%Y-%m-%d %H:%M')}"


class PagoEnLinea(models.Model):
    compra = models.OneToOneField(Compra, on_delete=models.CASCADE, related_name="pago_en_linea")
    numero_tarjeta = models.CharField(max_length=20, verbose_name="Número de Tarjeta")
    fecha_vencimiento = models.CharField(max_length=5, verbose_name="Fecha de Vencimiento (MM/AA)")
    codigo_seguridad = models.CharField(max_length=4, verbose_name="Código de Seguridad (CVV)")
    nombre_tarjeta = models.CharField(max_length=255, verbose_name="Nombre en la Tarjeta")

    def __str__(self):
        return f"Pago en Línea - Compra {self.compra.id}"

class TransferenciaBancaria(models.Model):
    compra = models.OneToOneField(Compra, on_delete=models.CASCADE, related_name="transferencia")
    nombre_banco = models.CharField(max_length=255, verbose_name="Nombre del Banco")
    numero_cuenta = models.CharField(max_length=20, verbose_name="Número de Cuenta")
    titular_cuenta = models.CharField(max_length=255, verbose_name="Titular de la Cuenta")
    monto_transferido = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto Transferido")
    fecha_transferencia = models.DateField(verbose_name="Fecha de la Transferencia")
    numero_referencia = models.CharField(max_length=50, verbose_name="Número de Referencia")
    comprobante = models.ImageField(upload_to="comprobantes/", verbose_name="Comprobante de Transferencia")

    def __str__(self):
        return f"Transferencia - Compra {self.compra.id}"


class DetalleVenta(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="detalles_venta")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return f"Detalle de {self.producto.nombre} (Compra ID: {self.compra.id})"




    
class Comentario(models.Model):
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='comentarios', on_delete=models.CASCADE, null=True, blank=True)
    respuesta_a = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas')
    

    # Nuevo campo de calificación
    calificacion = models.IntegerField(
        validators=[
            MinValueValidator(1, "La calificación mínima es 1"),
            MaxValueValidator(5, "La calificación máxima es 5")
        ],
        null=True,
        blank=True
    )

    utilidad = models.CharField(max_length=3, choices=[('si', 'Sí'), ('no', 'No'), ('', 'No Respondido')], default='')

    def __str__(self):
        return f'Comentario de {self.usuario.username} sobre {self.producto.nombre}'




