from django.db import models

class Persona(models.Model): #entre parentesis de donde hereda
    nombre = models.CharField(max_length = 30) #necesita que le pasemos el max_length si o si
    apellido = models.CharField(max_length = 30) #cantidad de caracteres que peude tomar
    edad = models.IntegerField()
