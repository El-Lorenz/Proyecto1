from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


def saludo (request): # primera vista
    p1=Persona("Profesor Juan","Diaz")
    
    #nombre="Juan"
    #apellido="Diaz"

    temasDelCurso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]

    ahora=datetime.datetime.now()
    
    #doc_externo=open("C:/Users/Lorenzo/Documents/GitHub/Django/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    #plt=Template(doc_externo.read())

    #doc_externo.close()

    #doc_externo=loader.get_template('miplantilla.html')

    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora, "temas":temasDelCurso})

    #documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora, "temas":temasDelCurso})


    #return HttpResponse(documento)
    return render(request,"miplantilla.html",{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora, "temas":temasDelCurso})

def damefecha(request):
    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    fecha y hora actuales %s
    </h1>
    </body>
    </html>"""%fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, anio):
    edadActual=18
    periodo=anio-2023
    edadFutura=edad+periodo
    documento="<html><body><h2>Ene el año %s tendras %s años" %(anio,edadFutura)

    return HttpResponse(documento)

def cursoC(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "CursoC.html",{"damefecha":fecha_actual})

def cursoCss(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "CursoCss.html",{"damefecha":fecha_actual})