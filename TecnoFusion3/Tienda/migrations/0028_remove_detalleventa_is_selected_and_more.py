# Generated by Django 5.1.2 on 2024-11-26 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0027_detalleventa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleventa',
            name='is_selected',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='precio_total',
        ),
        migrations.AlterField(
            model_name='compra',
            name='nombre_completo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='cantidad',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
