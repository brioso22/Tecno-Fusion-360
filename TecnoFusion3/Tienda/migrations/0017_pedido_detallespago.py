# Generated by Django 5.1.2 on 2024-11-25 18:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0016_remove_productosguardados_is_selected_producto_stock'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('departamento', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('metodo_pago', models.CharField(choices=[('online', 'Pago en línea'), ('transfer', 'Transferencia'), ('cash', 'Pago contra entrega')], max_length=20)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('enviado', 'Enviado'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetallesPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('online', 'Pago en línea'), ('transfer', 'Transferencia bancaria'), ('cash', 'Pago contra entrega')], max_length=10)),
                ('detalles', models.JSONField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles_pago', to='Tienda.pedido')),
            ],
        ),
    ]
