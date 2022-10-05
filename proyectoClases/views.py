from configparser import ExtendedInterpolation
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template

def hola (request):
    return HttpResponse('<h1>Buenas clase!</h1>') #h1 sirve para que se vea como un titulo, formato HTML

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_y_hora}')

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento para tus {edad} años seria: {fecha}')

def mi_template(request):
    
    cargar_archivo = open(r'C:\Users\Maria Luz Obregon\Documents\Clases Python\proyecto\templates\template.html', 'r')
    template = Template(cargar_archivo.read()) 
    cargar_archivo.close() #con esto se genera el template del archivo de html
    
    contexto = Context()
    template_renderizado = template.render(contexto) #renderizar es dibujar
    
    return HttpResponse(template_renderizado)
