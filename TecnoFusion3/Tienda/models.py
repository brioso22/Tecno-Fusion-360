from time import timezone
from django.db import models
from django.contrib.auth.models import User  # Utilizando el modelo de usuario por defecto de Django
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg



class Producto(models.Model):
    """
    Representa un producto en el catálogo de la tienda de tecnología.

    Attributes:
    - nombre (CharField): Nombre descriptivo del producto.
    - estado (CharField): Condición del producto (nuevo o usado).
    - categoria (CharField): Categoría del producto en el inventario.
    - precio (DecimalField): Precio del producto con precisión de dos decimales.
    - descripcion (TextField): Descripción detallada y características del producto.
    - imagen (ImageField): Imagen visual del producto.
    - promedio_calificacion (DecimalField): Promedio de calificaciones del producto.
    - stock (PositiveIntegerField): Cantidad de unidades disponibles.
    - visible (BooleanField): Indica si el producto está visible para los usuarios.

    Choices:
    - ESTADO_CHOICES: Define los posibles estados del producto.
    - CATEGORIAS_INICIALES: Categorías predefinidas para clasificación.

    Methods:
    - calificacion_promedio: Calcula el promedio de calificaciones del producto.
    """


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
    """
    Gestiona los productos guardados o en lista de deseos de un usuario.

    Attributes:
    - descripcion (CharField): Descripción breve de la lista o guardado.
    - cantidad_stock (IntegerField): Cantidad de productos en esta lista.
    - fecha_guardado (DateField): Fecha de creación de la lista.
    - fecha_actualizacion (DateTimeField): Última fecha de modificación.
    - activo (BooleanField): Indica si la lista está activa.
    - producto (ForeignKey): Referencia al producto guardado.
    - usuario (ForeignKey): Usuario propietario de la lista.
    """

    descripcion = models.CharField(max_length=100)
    cantidad_stock = models.IntegerField()
    fecha_guardado = models.DateField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #is_selected = models.BooleanField(default=False)  # Agregar este campo


class Compra(models.Model):
    """
    Representa una transacción de compra realizada por un usuario.

    Attributes:
    - nombre_completo (CharField): Nombre completo del comprador.
    - correo_electronico (EmailField): Correo electrónico del comprador.
    - numero_telefono (CharField): Número de teléfono de contacto.
    - departamento (CharField): Departamento de envío.
    - ciudad (CharField): Ciudad de envío.
    - direccion (CharField): Dirección completa de envío.
    - codigo_postal (CharField): Código postal opcional.
    - fecha_compra (DateTimeField): Fecha y hora de la compra.
    - usuario (ForeignKey): Usuario que realizó la compra.

    Methods:
    - __str__: Representación en cadena de la compra.
    """

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
    """
    Gestiona los pagos en línea asociados a una compra.

    Attributes:
    - compra (OneToOneField): Compra asociada al pago.
    - numero_tarjeta (CharField): Número de tarjeta de crédito/débito.
    - fecha_vencimiento (CharField): Fecha de vencimiento de la tarjeta.
    - codigo_seguridad (CharField): Código CVV de la tarjeta.
    - nombre_tarjeta (CharField): Nombre del titular de la tarjeta.

    Methods:
    - __str__: Representación en cadena del pago en línea.
    """

    compra = models.OneToOneField(Compra, on_delete=models.CASCADE, related_name="pago_en_linea")
    numero_tarjeta = models.CharField(max_length=20, verbose_name="Número de Tarjeta")
    fecha_vencimiento = models.CharField(max_length=5, verbose_name="Fecha de Vencimiento (MM/AA)")
    codigo_seguridad = models.CharField(max_length=4, verbose_name="Código de Seguridad (CVV)")
    nombre_tarjeta = models.CharField(max_length=255, verbose_name="Nombre en la Tarjeta")

    def __str__(self):
        return f"Pago en Línea - Compra {self.compra.id}"


class TransferenciaBancaria(models.Model):
    """
    Registra las transferencias bancarias como método de pago.

    Attributes:
    - compra (OneToOneField): Compra asociada a la transferencia.
    - nombre_banco (CharField): Nombre de la institución bancaria.
    - numero_cuenta (CharField): Número de cuenta bancaria.
    - titular_cuenta (CharField): Nombre del titular de la cuenta.
    - monto_transferido (DecimalField): Monto de la transferencia.
    - fecha_transferencia (DateField): Fecha de la transferencia.
    - numero_referencia (CharField): Número de referencia de la transferencia.
    - comprobante (ImageField): Imagen del comprobante de transferencia.

    Methods:
    - __str__: Representación en cadena de la transferencia.
    """


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
    """
    Representa los detalles individuales de productos en una venta.

    Attributes:
    - compra (ForeignKey): Compra a la que pertenece este detalle.
    - producto (ForeignKey): Producto específico de este detalle.
    - cantidad (IntegerField): Número de unidades del producto.
    - precio_unitario (DecimalField): Precio de una unidad del producto.
    - precio_total (DecimalField): Precio total para este detalle de venta.
    - is_selected (BooleanField): Indica si este detalle está seleccionado.

    Methods:
    - __str__: Representación en cadena del detalle de venta.
    """

    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="detalles_venta")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return f"Detalle de {self.producto.nombre} (Compra ID: {self.compra.id})"



    
class Comentario(models.Model):
    """
    Gestiona los comentarios y calificaciones de productos.

    Attributes:
    - texto (TextField): Contenido del comentario.
    - fecha (DateTimeField): Fecha de creación del comentario.
    - usuario (ForeignKey): Usuario que realiza el comentario.
    - producto (ForeignKey): Producto comentado.
    - respuesta_a (ForeignKey): Comentario al que responde (si es una respuesta).
    - calificacion (IntegerField): Puntuación del producto (1-5).
    - utilidad (CharField): Indicador de utilidad del comentario.

    Methods:
    - __str__: Representación en cadena del comentario.
    """

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




