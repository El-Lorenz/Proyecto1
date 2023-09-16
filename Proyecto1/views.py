from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo (request):
    nombre="Juan"
    apellido="Diaz"
    ahora=datetime.datetime.now()
    
    doc_externo=open("C:/Users/Lorenzo/Documents/GitHub/Django/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":nombre,"apellido_persona":apellido,"momento_actual":ahora})

    documento=plt.render(ctx)


    return HttpResponse(documento)

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

