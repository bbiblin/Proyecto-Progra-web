from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Usuario
from .models import Producto
from .carro import Carro
from .models import Contacto
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.db import transaction
from django.contrib.auth import get_user_model
from .models import metodoPago, Orden, Producto, detalleOrden
from django.contrib import messages

User = get_user_model()

# Create your views here.
def index(request):
    context = {
        "usuario": "",
    }
    return render(request, "index.html", context)

@login_required
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

@login_required
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

@login_required
def pag_admin(request):
    context = {
        "usuario": "",
    }
    return render(request, "indexx.html", context)

def pag_buscar(request):
    if request.method == "POST":
        buscado = request.POST['buscado']  # Obtener el valor del campo 'buscado' del formulario POST
        buscado = Producto.objects.filter(nombre_producto__icontains=buscado)

        if not buscado:
            messages.success(request, "No encontramos ese producto...")
            return render(request, "buscar.html", {'buscado':buscado})
        else:
            return render(request, "buscar.html", {'buscado':buscado})
    else:
        return render(request, "buscar.html")



#CRUD USUARIOS-------------------------------------------------------------------------------------

@login_required
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

@login_required
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

@login_required
def admin_listar(request):
    users = Usuario.objects.all()
    datos = { 'usuarios' : users }
    context = {
        "usuario": "",
    }
    return render(request, "crud_Admin/admin_listar.html", datos)

@login_required
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

@login_required
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

@login_required
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

@login_required
def productos_listar(request):
    productos = Producto.objects.all()
    datos = { 'productos' : productos }
    context = {
        "usuario": "",
    }
    return render(request, "crud_productos/productos_listar.html", datos)

@login_required
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

@login_required
def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=producto_id)  # Cambiado de 'id' a 'id_producto'
    carro.agregar(producto=producto)
    return redirect("catalogo")

@login_required
def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=producto_id)  # Cambiado de 'id' a 'id_producto'
    carro.eliminar(producto=producto)
    return redirect("catalogo")

@login_required
def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=producto_id)  # Cambiado de 'id' a 'id_producto'
    carro.restar_producto(producto=producto)
    return redirect("catalogo")

@login_required
def limpiar_carro(request):

    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("catalogo")

#contacto---------------------------------------------------------------------------------------------

@login_required
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
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('index')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Orden, detalleOrden, Producto, metodoPago

@login_required
def procesar_pago(request):
    if request.method == 'POST':
        carro = request.session.get('carro', {})
        
        if not carro:
            messages.warning(request, "Tu carrito está vacío.")
            return redirect('index')
        
        try:
            total = sum(Decimal(str(item['precio'])) * int(item['cantidad']) for item in carro.values())
            total = round(total, 2)
        except (ValueError, KeyError, TypeError) as e:
            messages.error(request, f"Error al calcular el total: {str(e)}")
            return redirect('index')
        
        try:
            with transaction.atomic():
                usuario = request.user
                metodo_pago, created = metodoPago.objects.get_or_create(nombre='Efectivo')
                
                orden = Orden.objects.create(
                    usuario=usuario,
                    id_metodo_pago=metodo_pago,
                    total=total,
                    estado='pendiente'
                )
                
                for key, item in carro.items():
                    producto = Producto.objects.get(id_producto=key)
                    if producto.stock < int(item['cantidad']):
                        raise ValueError(f"Stock insuficiente para el producto {producto.nombre}")
                    
                    detalleOrden.objects.create(
                        id_orden=orden,
                        id_producto=producto,
                        cantidad=int(item['cantidad']),
                        precio=Decimal(str(item['precio']))
                    )
                    
                    producto.stock -= int(item['cantidad'])
                    producto.save()
                
                del request.session['carro']
                request.session.modified = True
                
                messages.success(request, f"Tu orden #{orden.id_orden} ha sido procesada correctamente.")
                return render(request, 'confirmacion_pago.html', {'orden': orden})
        
        except Producto.DoesNotExist:
            messages.error(request, "Uno o más productos en tu carrito ya no están disponibles.")
        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"Error inesperado: {str(e)}")
        
        return redirect('index')
    
    return redirect('index')