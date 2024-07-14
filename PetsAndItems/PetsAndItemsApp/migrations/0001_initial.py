# Generated by Django 5.0.6 on 2024-07-14 22:20

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
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='metodoPago',
            fields=[
                ('id_metodo_pago', models.AutoField(db_column='id_metodo_pago', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='nombre_metodo_pago', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(db_column='nombre_producto', max_length=50)),
                ('descripcion', models.CharField(db_column='descripcion', max_length=100)),
                ('precio', models.IntegerField(db_column='precio')),
                ('stock', models.IntegerField(db_column='stock')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(db_column='id_usuario', primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(db_column='nombre_completo', max_length=50)),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('contraseña', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(db_column='id_orden', primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(default='Pendiente', max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('id_metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PetsAndItemsApp.metodopago')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='detalleOrden',
            fields=[
                ('id_detalle_orden', models.AutoField(db_column='id_detalle_orden', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(db_column='cantidad')),
                ('precio', models.IntegerField(db_column='total')),
                ('id_orden', models.ForeignKey(db_column='id_orden', on_delete=django.db.models.deletion.CASCADE, to='PetsAndItemsApp.orden')),
                ('id_producto', models.ForeignKey(db_column='id_producto', on_delete=django.db.models.deletion.CASCADE, to='PetsAndItemsApp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_carro', models.AutoField(db_column='id_carro', primary_key=True, serialize=False)),
                ('id_producto', models.ForeignKey(db_column='id_producto', on_delete=django.db.models.deletion.CASCADE, to='PetsAndItemsApp.producto')),
                ('id_usuario', models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.CASCADE, to='PetsAndItemsApp.usuario')),
            ],
        ),
    ]
