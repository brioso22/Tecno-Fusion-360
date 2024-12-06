# Generated by Django 5.1.2 on 2024-11-11 07:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(default='Empresa desconocida', max_length=255)),
                ('rubro_empresa', models.CharField(default='rubro desconocida', max_length=255)),
                ('descripcion_equipo', models.TextField(default='Sin descripción')),
                ('fecha_entrega', models.DateField(blank=True, null=True)),
                ('ubicacion_donante', models.CharField(default='Ubicación desconocida', max_length=255)),
                ('comentarios_adicionales', models.TextField(blank=True, null=True)),
                ('terminos', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]