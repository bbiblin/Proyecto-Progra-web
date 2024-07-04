from django.contrib import admin
from .models import Usuario, Producto, Carrito, metodoPago, Orden, detalleOrden, Contacto

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'descripcion', 'precio', 'stock', 'imagen')
    search_fields = ('nombre_producto', 'descripcion')

    fieldsets = (
        (None, {
            'fields': ('nombre_producto', 'descripcion', 'precio', 'stock', 'imagen')
        }),
    )

admin.site.register(Usuario)
# admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(metodoPago)
admin.site.register(Orden)
admin.site.register(detalleOrden)
admin.site.register(Contacto)