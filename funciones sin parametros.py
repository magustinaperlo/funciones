import math
#FUNCIONES SIN PARAMETROS

def  programacion_2023 ():               #funcion que imprime una frase 
    print ("programacion 2023")

def hola ():                            #funcion que imprime un saludo
    print ("hola")

def concepto_programacion ():           #funcion que imprime un concepto de programación
    print ("Programación es la acción de programar que implica ordenar, estructurar o componer una serie de acciones cronológicas para cumplir un objetivo.")

def chiste ():                          #funcion que imprime un chiste
    print ("¿Cómo va Batman a su funeral? Batieso.")

def frase_libro_famoso():               #funcion que imprime una frase de un libro famoso
    print ("Nuestras vidas se definen por las oportunidades, incluso las que perdemos.")
    print ("'El curioso caso de Benjamin Button', de F. Scott Fitzgerald.")


#FUNCIONES CON PARAMETROS

def nombre_edad (nombre,edad):    #funcion para presentar con nombre y edad
    print (f"soy {nombre} y tengo {edad} años")

def saludo (nombre):              #funcion para saludar
    print (f"hola {nombre}!")

def resta ( valor1, valor2):        #funcion para restar
    resultado = valor1 - valor2
    return resultado

def multiplicacion (valor1,valor2):         #funcion para multiplicar
    resultado = valor1 * valor2
    return resultado

def perimetro_triangulo_equilatero(a):      #funcion para calcular el perimetro de un triangulo equilatero
    resultado = a*3
    return resultado

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

resultado = frase_libro_famoso ()
print (resultado)



