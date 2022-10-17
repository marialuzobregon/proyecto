from configparser import ExtendedInterpolation
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random

def hola (request):
    return HttpResponse('<h1>Buenas clase!</h1>') #h1 sirve para que se vea como un titulo, formato HTML

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_y_hora}')

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento para tus {edad} años seria: {fecha}')

def mi_template(request):
    
    cargar_archivo = open(r'C:\Users\Maria Luz Obregon\Documents\Clases Python\proyecto\templates\mi_template.html', 'r')
    template = Template(cargar_archivo.read()) 
    cargar_archivo.close() #con esto se genera el template del archivo de html
    
    contexto = Context()
    template_renderizado = template.render(contexto) #renderizar es dibujar, reestructurar como lo necesita django
    
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
    
    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'persona':nombre})
    
    return HttpResponse(template_renderizado)

def prueba_template(request):
    
    mi_contexto = {
        'rango': list(range(1, 11)),
        'valor_aleatorio': random.randrange(1,11)  
    }
    
    template = loader.get_template('prueba_template.html')
    template_renderizado = template.render(mi_contexto)
    
    return HttpResponse(template_renderizado)