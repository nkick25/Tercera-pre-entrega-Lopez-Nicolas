from django.shortcuts import render
from django.http import HttpResponse
from Appcoder.models import *
from Appcoder.forms import *
import datetime

### Vista de paginas y sub-paginas

def inicio(request):

    return render(request, "Appcoder/inicio.html")
    
def curso(request):

    return render(request, "Appcoder/curso.html")

def estudiante(request):

    return render(request, "Appcoder/estudiante.html")

def profesor(request):

    return render(request, "Appcoder/profesor.html")

def entregable(request):

    return render(request, "Appcoder/entregable.html")

### Vista de formularios de carga

###
def curso_form(request):

    if request.method == "POST":

        formulario1 = curso_formulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            curso = Curso(nombre=info["curso"], camada=info["camada"])

            curso.save()
        
            return render(request, "Appcoder/inicio.html")
    
    else:

        formulario1 = curso_formulario()

    return render(request, "Appcoder/curso_formulario.html", {"form1":formulario1})
###
###
def estudiante_form(request):

    if request.method == "POST":

        formulario2 = estudiante_formulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            estudiante = Estudiante(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])

            estudiante.save()
        
            return render(request, "Appcoder/inicio.html")

    else:

        formulario2 = estudiante_formulario()

    return render(request, "Appcoder/estudiante_formulario.html", {"form2":formulario2})
###
###
def profesor_form(request):

    if request.method == "POST":

        formulario3 = profesor_formulario(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            profesor = Profesor(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], profesion=info["profesion"])

            profesor.save()
        
            return render(request, "Appcoder/inicio.html")

    else:

        formulario3 = profesor_formulario()

    return render(request, "Appcoder/profesor_formulario.html", {"form3":formulario3})
###
###
def entregables_form(request):

    if request.method == "POST":

        formulario4 = entregable_formulario(request.POST)

        if formulario4.is_valid():

            info = formulario4.cleaned_data

            entregables = Entregable(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])

            entregables.save()
        
            return render(request, "Appcoder/inicio.html")

    else:

        formulario4 = entregable_formulario()

    return render(request, "Appcoder/entregable_formulario.html", {"form4":formulario4})
###

### Vista de fromulario de busqueda
###
def busqueda_camada(request):

    return render (request, "Appcoder/busqueda_camada.html")
###
###
def resultados(request):
    if request.GET["camada"]:

        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "Appcoder/resultados_camada.html", {"cursos":cursos, "camada":camada})

    else:
        
        respuesta = "No ingresaste datos"

    return HttpResponse(respuesta)


""" def resultados(request):

    if request.method == "GET":

        formulario5 = busquedaxcamada(request.GET)

        if formulario5.is_valid():

            camada = request.GET["camada"]
            cursos = Curso.objects.filter(camada__icontains=camada)
        
            return render(request, "Appcoder/inicio.html")

    else:

        formulario5 = busquedaxcamada()

    return render(request, "Appcoder/resultados_camada.html", {"form5":formulario5}) """