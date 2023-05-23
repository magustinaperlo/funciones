
import math

#FUNCIONES CON PARAMETROS DEFINIDOS 

def division (a, b=5):                    #funcion para dividir por 5 (cinco)
    resultado = a//b 
    return resultado 

def promedio (a,b,c,d=3):                 #funcion para calcular promedio por 3 (tres)
    suma = a+b+c
    resultado = suma//d
    return resultado

def porcentaje (a,b=25,c=100):            #funcion para calcular el porcentaje de 25%
    resultado = b*a//c
    return resultado 

def perimetro_circulo (b,a=math.pi):          #funcion para calcular el perimetro de un circulo
    resultado = a*b
    return resultado

def volumen_cilindro (c,a=math.pi, b= 52):
    resultado = a*b**2*c
    return resultado

#sugerencia: 

import math

# FUNCIONES CON PARÁMETROS DEFINIDOS

def division(a, b=5):
    resultado = a / b
    return resultado

def promedio(a, b, c, d=3):
    suma = a + b + c
    resultado = suma / d
    return resultado

def porcentaje(a, b=25, c=100):
    resultado = (b * a) / c
    return resultado

def perimetro_circulo(radio, pi=math.pi):
    resultado = 2 * pi * radio
    return resultado

def volumen_cilindro(altura, radio=52, pi=math.pi):
    resultado = pi * radio**2 * altura
    return resultado
se reemplaza "//" por "/" para obtener mas decimales 
