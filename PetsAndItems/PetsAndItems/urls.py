"""
URL configuration for PetsAndItems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from PetsAndItemsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('carrito', views.carrito, name='carrito'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('contacto', views.contacto, name='contacto'),
    path('pdp1/<int:producto_id>/', views.pdp1, name='pdp1'),
    path('registro_inicio', views.registro_inicio, name='registro_inicio'),
    path('ubicacion', views.ubicacion, name='ubicacion'),
    path('admin_pag', views.pag_admin, name='pag_admin'),

    #crud usuarios
    path('admin_add', views.admin_add, name='admin_add'),
    path('admin_eliminar', views.admin_eliminar, name='admin_eliminar'),
    path('admin_listar', views.admin_listar, name='admin_listar'),
    path('admin_modificar', views.admin_modificar, name='admin_modificar'),

    #crud productos
    path('productos_add', views.productos_add, name='productos_add'),
    path('productos_eliminar', views.productos_eliminar, name='productos_eliminar'),
    path('productos_modificar', views.productos_modificar, name='productos_modificar'),
    path('productos_listar', views.productos_listar, name='productos_listar'),

    #carro de compras
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar'),
    path('limpiar/', views.limpiar_carro, name='limpiar'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)