from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Usuario
from .models import Producto
from .carro import Carro
from .models import Contacto
from django.utils import timezone
from django.views.generic import View

# Create your views here.
def index(request):
    context = {
        "usuario": "",
    }
    return render(request, "index.html", context)

def carrito(request):
    context = {
        "usuario": "",
    }
    return render(request, "carrito.html", context)

def catalogo(request):
    productos = Producto.objects.all()
    context = {
        "usuario": "",
    }
    return render(request, 'catalogo.html', {'productos': productos})

def contacto(request):
    context = {
        "usuario": "",
    }
    return render(request, "contacto.html", context)

def pdp1(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    producto.descripcion = producto.descripcion.replace('.', '.\n').replace(':', ':\n')
    context = {
        'producto': producto
    }
    return render(request, "pdp1.html", context)

def registro_inicio(request):
    context = {
        "usuario": "",
    }
    return render(request, "registro_inicio.html", context)

def iniciosesion(request):
    context = {
        "usuario": "",
    }
    return render(request, "inicio_sesion.html", context)

def ubicacion(request):
    context = {
        "usuario": "",
    }
    return render(request, "ubicacion.html", context)

def pag_admin(request):
    context = {
        "usuario": "",
    }
    return render(request, "indexx.html", context)


#CRUD USUARIOS-------------------------------------------------------------------------------------
def admin_add(request):
    if request.method == 'POST':
        nombre_completo = request.POST.get('nombre_completo')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')

        if nombre_completo and correo and contraseña:
            user = Usuario(nombre_completo=nombre_completo, correo=correo, contraseña=contraseña)
            user.save()
            return redirect('admin_listar')  # Redirige a la lista de usuarios después de guardar
        else:
            messages.error(request, "Por favor, completa todos los campos.")
    
    return render(request, "crud_Admin/admin_add.html")


def admin_eliminar(request):
    context = {
        "usuario": "",
    }
    if request.method == 'POST':
        if  request.POST.get('id'):
            id_borrar = request.POST.get('id')
            tupla = Usuario.objects.get(id_usuario = id_borrar)
            tupla.delete()
            return redirect('admin_listar')
    else:
        users = Usuario.objects.all()
        datos = { 'usuarios' : users }
        return render(request, "crud_Admin/admin_eliminar.html", datos)

def admin_listar(request):
    users = Usuario.objects.all()
    datos = { 'usuarios' : users }
    context = {
        "usuario": "",
    }
    return render(request, "crud_Admin/admin_listar.html", datos)

def admin_modificar(request):
    context = {
        "usuario": "",
    }
    if request.method == 'POST':
        if  request.POST.get('id') and request.POST.get('nombre_completo') and request.POST.get('correo') and request.POST.get('contraseña'):
            user = Usuario()
            user.id_usuario = request.POST.get('id')
            user.nombre_completo = request.POST.get('nombre_completo')
            user.correo = request.POST.get('correo')
            user.contraseña = request.POST.get('contraseña')
            user.save()
            return redirect('admin_listar')    
    else:
        users = Usuario.objects.all()
        datos = { 'usuarios' : users }
        return render(request, "crud_Admin/admin_modificar.html", datos)

#CRUD PRODUCTOS---------------------------------------------------------------------------------------

def productos_add(request):
    context = {
        "usuario": "usuarios",
    }
    
    if request.method == 'POST':
        if request.POST.get('nombre_producto') and request.POST.get('descripcion') and request.POST.get('precio') and request.POST.get('stock'):
            producto = Producto()
            producto.nombre_producto = request.POST.get('nombre_producto')
            producto.descripcion = request.POST.get('descripcion')
            producto.precio = request.POST.get('precio')
            producto.stock = request.POST.get('stock')
            producto.imagen = request.POST.get('imagen')
            producto.save()
            return redirect('productos_listar')    
    else:
        return render(request, "crud_productos/productos_add.html", context)

def productos_eliminar(request):
    context = {
        "usuario": "",
    }
    if request.method == 'POST':
        if  request.POST.get('id'):
            id_borrar = request.POST.get('id')
            tupla = Producto.objects.get(id_producto = id_borrar)
            tupla.delete()
            return redirect('productos_listar')
    else:
        productos = Producto.objects.all()
        datos = { 'productos' : productos }
        return render(request, "crud_productos/productos_eliminar.html", datos)

def productos_listar(request):
    productos = Producto.objects.all()
    datos = { 'productos' : productos }
    context = {
        "usuario": "",
    }
    return render(request, "crud_productos/productos_listar.html", datos)

def productos_modificar(request):
    context = {
        "usuario": "",
    }
    if request.method == 'POST':
        if  request.POST.get('id_product') and request.POST.get('nombre_product') and request.POST.get('descripcion_product') and request.POST.get('precio_product')  and request.POST.get('stock_product'):
            producto = Producto()
            producto.id_producto = request.POST.get('id_product')
            producto.nombre_producto = request.POST.get('nombre_product')
            producto.descripcion = request.POST.get('descripcion_product')
            producto.precio = request.POST.get('precio_product')
            producto.stock = request.POST.get('stock_product')
            producto.save()
            return redirect('productos_listar')    
    else:
        productos = Producto.objects.all()
        datos = { 'productos' : productos }
    return render(request, "crud_productos/productos_modificar.html", datos)


#carro de compras-------------------------------------------------------------------------------------

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=producto_id)  # Cambiado de 'id' a 'id_producto'
    carro.agregar(producto=producto)
    return redirect("catalogo")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=producto_id)  # Cambiado de 'id' a 'id_producto'
    carro.eliminar(producto=producto)
    return redirect("catalogo")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=producto_id)  # Cambiado de 'id' a 'id_producto'
    carro.restar_producto(producto=producto)
    return redirect("catalogo")

def limpiar_carro(request):

    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("catalogo")

#contacto---------------------------------------------------------------------------------------------


def guardar_mensaje(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        contacto = Contacto(email=email, mensaje=mensaje, fecha_envio=timezone.now())
        contacto.save()
        return redirect('contacto') 

    return render(request, 'contacto.html')  


#AUTENTICACION----------------------------------------------------------------------------------------

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

class VRegistro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request,"sign_up.html",{"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)

        if form.is_valid():

            usuario=form.save()

            login(request, usuario)

            return redirect('index')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request,"sign_up.html",{"form":form})


def cerrar_sesion(request):
    logout(request)

    return redirect('index')


def inicio_sesion(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('index')
            else:
                messages.error(request, "usuario no válido")
        else:
            messages.error(request, "información incorrecta")

    form=AuthenticationForm()
    return render(request,"login.html",{"form":form})
