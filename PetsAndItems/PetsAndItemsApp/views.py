from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "usuario": "",
    }
    return render(request, "templates/pages/index.html", context)

def carrito(request):
    context = {
        "usuario": "",
    }
    return render(request, "templates/pages/carrito.html", context)

def catalogo(request):
    context = {
        "usuario": "",
    }
    return render(request, "templates/pages/catalogo.html", context)

def contacto(request):
    context = {
        "usuario": "",
    }
    return render(request, "templates/pages/contacto.html", context)

def pdp1(request):
    context = {
        "usuario": "",
    }
    return render(request, "templates/pages/pdp1.html", context)

def registro_inicio(request):
    context = {
        "usuario": "",
    }
    return render(request, "templates/pages/registro_inicio.html", context)

def ubicacion(request):
    context = {
        "usuario": "",
    }
    return render(request, "templates/pages/ubicacion.html", context)



