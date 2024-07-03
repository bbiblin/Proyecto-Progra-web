from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='id_usuario', primary_key=True)
    nombre_completo = models.CharField(db_column='nombre_completo' , max_length=50)
    correo = models.EmailField(unique=True, max_length=100, blank=False, null=False)
    contraseña = models.CharField(unique=True, max_length=100, null=False , blank=False)

def __str__(self):
    return str(self.nombre_completo)


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(db_column='nombre_producto', max_length=50, null=False,blank=False)
    descripcion = models.CharField(db_column='descripcion', max_length=100 ,null=False ,blank=False)
    precio = models.IntegerField(db_column='precio', null=False ,blank=False)
    stock = models.IntegerField(db_column='stock' ,null=False, blank=False)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

def __str__(self):
    return str(self.nombre_producto)

class Carrito(models.Model):
    id_carro = models.AutoField(db_column='id_carro' ,primary_key=True)
    id_usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE, db_column='id_usuario')
    id_producto = models.ForeignKey('Producto',on_delete=models.CASCADE, db_column='id_producto')

def __str__(self):
        return str(self.id_carro)

class metodoPago(models.Model):
     id_metodo_pago = models.AutoField(db_column='id_metodo_pago', primary_key=True)
     nombre = models.CharField(db_column='nombre_metodo_pago', max_length=20 ,null=False, blank=False)

def __str__(self):
     return str(self.nombre)

class Orden(models.Model):
     id_orden = models.AutoField(db_column='id_orden', primary_key=True)
     id_usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE, db_column='id_usuario')
     id_metodo_pago = models.ForeignKey('metodoPago',on_delete=models.CASCADE, db_column='id_metodo_pago')
     total = models.IntegerField(db_column='total', null=False ,blank=False)

def __str__(self):
     return str(self.id_orden)


class detalleOrden(models.Model):
     id_detalle_orden = models.AutoField(db_column='id_detalle_orden' ,primary_key=True)
     id_orden = models.ForeignKey('Orden',on_delete=models.CASCADE, db_column='id_orden')
     id_producto = models.ForeignKey('Producto',on_delete=models.CASCADE, db_column='id_producto')
     cantidad = models.IntegerField(db_column='cantidad' ,null=False, blank=False)
     precio = models.IntegerField(db_column='total' ,null=False, blank=False)

def __str__(self):
     return str(self.id_detalle_orden)
    







