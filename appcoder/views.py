from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

from appcoder.models import Posteo, Pais, Ciudad
from appcoder.forms import PosteoFormulario


# Create your views here.

def inicio(request):
    dict_ctx = {"title": "Inicio", "page": "Inicio"}
    return render(request, "appcoder/index.html", dict_ctx)

def paises(request):
    paises = Pais.objects.all()
    return render(request, "appcoder/paises.html", {"paises": paises, "title": "Pais", "page": "Pais"})

def ciudades(request):
    ciudades = Ciudad.objects.all()
    return render(request, "appcoder/ciudades.html", {"ciudades": ciudades, "title": "Ciudades", "page": "Ciudades"})

def posteos(request):

    posteos = Posteo.objects.all()

    if request.method == "POST":
        formulario = PosteoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            posteo = Posteo(data['titulo'], data['texto'])
            posteo.save()

            formulario = PosteoFormulario()
            return render(request, "appcoder/posteos.html", {"posteos": posteos, "title": "Posteos", "page": "Posteos", "formulario": formulario})
    else:   
        
        formulario = PosteoFormulario()
        return render(request, "appcoder/posteos.html", {"posteos": posteos, "title": "Posteos", "page": "Posteos", "formulario": formulario})

def buscar_posteo(request):

    data = request.GET.get('titulo', "")
    error = ""

    if data:
        try:
            posteo = Posteo.objects.get(titulo=data)
            return render(request, 'appcoder/busqueda_posteo.html', {"posteo": posteo, "id": data})

        except Exception as exc:
            print(exc)
            error = "No existe ese titulo"
    return render(request, 'appcoder/busqueda_posteo.html', {"error": error})