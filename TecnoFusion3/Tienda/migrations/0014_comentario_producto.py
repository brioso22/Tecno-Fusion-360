# Generated by Django 5.1.2 on 2024-11-14 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0013_comentario_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Tienda.producto'),
        ),
    ]
