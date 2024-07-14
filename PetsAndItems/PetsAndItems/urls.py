from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from PetsAndItemsApp.views import VRegistro
from PetsAndItemsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('contacto', views.contacto, name='contacto'),
    path('registro_inicio', views.registro_inicio, name='registro_inicio'),
    path('inicio_sesion', views.iniciosesion, name='inicio_sesion'),
    path('ubicacion', views.ubicacion, name='ubicacion'),
    path('sign_up', VRegistro.as_view(), name='sign_up'),
    path('logout', views.cerrar_sesion, name='logout'),
    path('login', views.inicio_sesion, name='login'),
    path('buscar', views.pag_buscar, name='buscar'),

    # Rutas protegidas
    path('carrito', login_required(views.carrito), name='carrito'),
    path('pdp1/<int:producto_id>/', login_required(views.pdp1), name='pdp1'),
    path('admin_pag', login_required(views.pag_admin), name='pag_admin'),

    # CRUD usuarios (protegido)
    path('admin_add', login_required(views.admin_add), name='admin_add'),
    path('admin_eliminar', login_required(views.admin_eliminar), name='admin_eliminar'),
    path('admin_listar', login_required(views.admin_listar), name='admin_listar'),
    path('admin_modificar', login_required(views.admin_modificar), name='admin_modificar'),

    # CRUD productos (protegido)
    path('productos_add', login_required(views.productos_add), name='productos_add'),
    path('productos_eliminar', login_required(views.productos_eliminar), name='productos_eliminar'),
    path('productos_modificar', login_required(views.productos_modificar), name='productos_modificar'),
    path('productos_listar', login_required(views.productos_listar), name='productos_listar'),

    # Carro de compras (protegido)
    path('agregar/<int:producto_id>/', login_required(views.agregar_producto), name='agregar'),
    path('eliminar/<int:producto_id>/', login_required(views.eliminar_producto), name='eliminar'),
    path('restar/<int:producto_id>/', login_required(views.restar_producto), name='restar'),
    path('limpiar/', login_required(views.limpiar_carro), name='limpiar'),

    # Contacto
    path('guardar-mensaje/', views.guardar_mensaje, name='guardar_mensaje'),
    
    #pedidos
    path('procesar-pago/', views.procesar_pago, name='procesar_pago'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)