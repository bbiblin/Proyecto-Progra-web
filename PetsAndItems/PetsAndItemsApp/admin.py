from django.contrib import admin
from .models import Usuario, Producto, Carrito, metodoPago, Orden, detalleOrden

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(metodoPago)
admin.site.register(Orden)
admin.site.register(detalleOrden)