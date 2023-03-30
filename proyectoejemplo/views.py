from django.http import HttpResponse
from django.template import Template,Context 
import datetime


def saludar(request):
    return HttpResponse("Hola Mundo!")


def segunda_vista(request):
    return HttpResponse("YA ENTENDI COMO FUNCIONA!!!")


def dia_de_hoy(request):
    dia= datetime.datetime.today()
    cadena= f"Hoy es {dia}"
    return HttpResponse(cadena) 


def saludo_con_nombre(request, nombre):
    return HttpResponse(f"Hola {nombre} como estas? La comisión 51325 te da la Bienvenida!")


def calcula_anio_nacimiento(request, edad):
    anio_actual = datetime.datetime.today().year
    anio_nacimiento = anio_actual- int(edad)
    return HttpResponse(f"Usted nacio en el año {anio_nacimiento}")

def probandoHtml(request):
    archivo = open(r"C:\Users\cti7860\Desktop\ARCHIVOS PERSONALES\Capacitación\CURSO PYTHON - CODERHOUSE\DJANGO\proyectoejemplo\Plantillas\template1.html")
    texto = archivo.read()
    archivo.close()
    #template = Template(archivo.read())
    #archivo.close()


    template = Template(texto)
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento) 
