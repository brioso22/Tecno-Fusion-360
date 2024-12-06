# Generated by Django 5.1.2 on 2024-11-12 16:07

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0011_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Tienda.producto')),
            ],
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]