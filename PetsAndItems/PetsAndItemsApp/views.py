from django.shortcuts import render

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



