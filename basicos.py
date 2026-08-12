""" 
#CONCATENAR VARIABLES
name=input("Ingrese su nombre")
#para concatenar variables (juntar) con el texto que vamos a escribir hay dos formas posibles
#° la primera es agregando comas entre el texto y la variable (esta forma no es recomendada)
#° la segunda forma es anteponiendo al texto la letra f (en minúsculas) y agregando la variable
#directamente dentro del texto entre paréntesis de llave {}
#1° Ejemplo
print("Hola ", name,"bienvenido")

#2° Ejemplo 2
print(f"hola{name}")

"""

#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
""" 
print("hola mundo!")
 """
#_____________________________________________________________________________________

#Crear un programa que pida el nombre y edad de una persona y diga si es mayor de edad
""" 
name=input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad>=18:
    print(f"{name} eres mayor de edad")
else:
    print(f"{name} eres menor de edad")
 """
#_____________________________________________________________________________________

#EXPLICACIÓN DEL CICLO FOR
#for i in range (5):
#     print (i)
"""
para cada i en el rango de 5
acá partimos con que mi variable i, la cual es numérica, vale 0 por defecto
es decir i = 0 y este código se va ejecutar 5 veces
luego de la primera vez que se ejecute mi "i" ya no va a valer 0 sino 1
y asi sucesivamente hasta llegar al número solicitado
"""

#Imprimir los números del 1 al 10 usando for
"""
En este caso, piden que comience desde el 1 y no desde el 0 como lo realiza el ejercicio anterior, además debe llegar al 10. Por lo que ahora deberemos agregarle el rango que 
necesitamos que recorra nuestro ciclo for, entre los paréntesis de este.
Ahora dentro del paréntesis agregamos el número desde donde comenzará nuestro ciclo hasta uno más
del que necesitamos, como ahora comenzaremos del 1 y termina en el 10
Debemos poner 1 y 11 ya que es uno más que el que necesitamos

for i in range(1,11):
    print(i) 

"""


#_____________________________________________________________________________________

#Pide un número N y luego solicita N números. Muestra la suma total.
""" 
cant = int(input("Ingrese cuantos números va a sumar: "))
sumat=0
for i in range (cant):
    suma = int(input(f"ingrese el {i+1}° número: "))
    sumat = sumat + suma
    print(f"Luego del {i+1}° número esta es la suma total",sumat)
 """
#_____________________________________________________________________________________

#Pide 3 notas (como float) al usuario. Calcula el promedio y muestra si está aprobado (nota ≥ 4.0) o reprobado.
""" 
nota1 = float(input("Ingrese su nota1: "))
nota3 = float(input("Ingrese su nota2: "))
nota2 = float(input("Ingrese su nota3: "))
x = (nota1 + nota2 + nota3)/3

if x>=4:
    print(f"Usted ha aprobado con {x} de promedio")
else:
    print(f"Usted ha reprobado con {x} de promedio")

 """
#_____________________________________________________________________________________

#Pregunta la edad al usuario. Si tiene 18 años o más, indica que puede votar. Si no, muestra cuántos años le faltan.
""" 
edad = int(input("Ingrese su edad: "))
if edad>=18:
    print(f"usted puede votar ya que posee {edad} y es mayor de edad")
else:
    print(f"usted no puede votar, aún le faltan {18-edad} año(s)")
 """

#_____________________________________________________________________________________
#Pide al usuario que ingrese su nombre y apellido por separado, y luego muestra su nombre completo en una sola línea.
""" 
name=input("Ingrese su nombre: ")
lName=input("Ingrese su apellido: ")
print("usted se llama ",name,lName)
 """
#_____________________________________________________________________________________

#Pide la base y la altura de un rectángulo, y muestra su área. Usa float si es necesario
""" 
b=float(input("Ingrese la base del triángulo: "))
h=float(input("Ingrese la altura del triángulo: "))

a = (b*h)/2

print(f"El área del triangulo es: {a}")

 """#_____________________________________________________________________________________
