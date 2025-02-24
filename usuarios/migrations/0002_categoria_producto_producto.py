# Generated by Django 5.1.5 on 2025-02-23 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_minimo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('categoria_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='usuarios.categoria_producto')),
            ],
        ),
    ]
