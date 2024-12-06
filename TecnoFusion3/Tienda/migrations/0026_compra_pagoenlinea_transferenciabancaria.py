# Generated by Django 5.1.2 on 2024-11-26 03:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0025_remove_transferenciabancaria_compra_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=255, verbose_name='Nombre completo')),
                ('correo_electronico', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('numero_telefono', models.CharField(max_length=20, verbose_name='Número de teléfono')),
                ('departamento', models.CharField(max_length=100, verbose_name='Departamento')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('codigo_postal', models.CharField(blank=True, max_length=10, null=True, verbose_name='Código Postal')),
                ('fecha_compra', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Compra')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='PagoEnLinea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tarjeta', models.CharField(max_length=20, verbose_name='Número de Tarjeta')),
                ('fecha_vencimiento', models.CharField(max_length=5, verbose_name='Fecha de Vencimiento (MM/AA)')),
                ('codigo_seguridad', models.CharField(max_length=4, verbose_name='Código de Seguridad (CVV)')),
                ('nombre_tarjeta', models.CharField(max_length=255, verbose_name='Nombre en la Tarjeta')),
                ('compra', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pago_en_linea', to='Tienda.compra')),
            ],
        ),
        migrations.CreateModel(
            name='TransferenciaBancaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_banco', models.CharField(max_length=255, verbose_name='Nombre del Banco')),
                ('numero_cuenta', models.CharField(max_length=20, verbose_name='Número de Cuenta')),
                ('titular_cuenta', models.CharField(max_length=255, verbose_name='Titular de la Cuenta')),
                ('monto_transferido', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto Transferido')),
                ('fecha_transferencia', models.DateField(verbose_name='Fecha de la Transferencia')),
                ('numero_referencia', models.CharField(max_length=50, verbose_name='Número de Referencia')),
                ('comprobante', models.ImageField(upload_to='comprobantes/', verbose_name='Comprobante de Transferencia')),
                ('compra', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='transferencia', to='Tienda.compra')),
            ],
        ),
    ]
