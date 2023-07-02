from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.shortcuts import render
from APP.models import Curso



def saludo(request):
    return HttpResponse("SUMMERTAN BRONCEADO ORGANICO")

def segunda_vista(request):
    return HttpResponse("Organic Sunless Tanning Technique")


def hoy(request):
    dia = datetime.now()
    documento = f"Hoy es: <br>{dia}"
    return HttpResponse(documento)

def minombre(self, nombre):
    documento = f"Mi nombre es: {nombre}"
    return HttpResponse(documento)

def testingtemplate(self):
    nom = "Laura"
    ap = "Montoya"
    precio = "4000 - Cuerpo Completo"
    
    diccionario = {"nombre":nom, "apellido":ap, "hoy":datetime.now(), "precio":precio}
    mihtml = open('C:/Users/lauri/OneDrive/Desktop/BLOG2/weblog/weblog/templates/template1.html')
    plantilla = Template(mihtml.read())
    mihtml.close()
    contexto = Context(diccionario)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def curso(self):
    curso=Curso(nombre="Desarrollo Web", camada="19881")
    curso.save()
    documento=f"-----> Curso: {Curso.nombre}    Camada: {curso.camada}"
    return HttpResponse(documento)