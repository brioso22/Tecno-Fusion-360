# Generated by Django 5.1.2 on 2024-11-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_alter_producto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[('nuevo', 'Nuevo'), ('usado', 'Usado')], default='nuevo', max_length=10),
        ),
    ]
