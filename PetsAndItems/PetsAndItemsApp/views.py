from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario

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
    context = {
        "usuario": "",
    }
    return render(request, "catalogo.html", context)

def contacto(request):
    context = {
        "usuario": "",
    }
    return render(request, "contacto.html", context)

def pdp1(request):
    context = {
        "usuario": "",
    }
    return render(request, "pdp1.html", context)

def registro_inicio(request):
    context = {
        "usuario": "",
    }
    return render(request, "registro_inicio.html", context)

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

def admin_add(request):
    context = {
            "usuario": "usuarios",
            }
    if request.method == 'POST':
        if request.POST.get('nombre_completo') and request.POST.get('correo') and request.POST.get('contraseña'):
            user = Usuario()
            user.nombre_completo = request.POST.get('nombre_completo')
            user.correo = request.POST.get('correo')
            user.contraseña = request.POST.get('contraseña')
            user.save()
            return redirect('admin_listar')    
    else:
        return render(request, "crud_Admin/admin_add.html", context)


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





