# FUNCIÓN SIN PARÁMETROS
""" def fun():
    print("Hola mundo")
fun() """

#FUNCIÓN CON VARIABLE INPUT DE PARÁMETRO
""" def saludar(a):
    print(f"Hola {a}")

a=input("Ingrese su nombre: ")
saludar(a) """


#FUNCIÓN CON RETURN
""" def saludar(nombre):
    return "Hola, " + nombre + "!"

mensaje_saludo = saludar("Juan")
#QUE PASA SI NO USAMOS EL PRINT
print(mensaje_saludo) """

#FUNCIÓN CON VALOR PREDETERMINADO
""" 
#ESTO ES ÚTIL CUANDO NO SABEMOS SI EL USUARIO INGRESARÁ UN NOMBRE O NO
def saludar(nombre = "user"):
    print(f"Hola, {nombre}")

saludar()
saludar("Sergio")
"""

#FUNCIÓN DE SUMA
""" def sumar (a, b):
    return a + b
a = int(input("Ingrese el 1° número: "))
b = int(input("Ingrese el 2° número: "))
suma = sumar(a,b)
print(f"La suma es: {suma}") 

"""

#FUNCIÓN ANÓNIMA
""" cuadrado = lambda x: x*x
result = cuadrado(5)
print(f"El cuadrado es: {result}")

# SE USAN EN FUNCIONES SIMPLES
# NO TIENEN RETURN NI NOMBRE
# SON ÚTILES CUANDO NO QUEREMOS DEFINIR UNA FUNCIÓN COMPLETAW

 """