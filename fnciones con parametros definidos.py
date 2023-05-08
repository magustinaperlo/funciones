
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