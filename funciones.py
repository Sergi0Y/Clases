# FUNCIÓN SIN PARÁMETROS
""" def fun():
    print("Hola mundo")
fun() """

#FUNCIÓN CON VARIABLE INPUT DE PARÁMETRO
""" def saludar(a):
    print(f"Hola {a}")

a=input("Ingrese su nombre: ")
saludar(a) """



def sumar (x):    
    n_suma=0
    for i in range(x):        
        suma = int(input(f"Ingrese el valor número {i+1}°: "))
        n_suma = n_suma + suma
    return n_suma

x = int(input("Ingrese cuantos números desea sumar: "))
resultado = sumar(x)
print(f"la suma es {resultado}")


""" 
def sumar(x):    
    n_suma = 0  # Inicializar la suma en 0
    for i in range(x):        
        numero = int(input(f"Ingrese el valor número {i+1}°: "))
        n_suma += numero  # Sumar al total
    return n_suma  # Retornar el resultado

# Pedir al usuario cuántos números desea sumar
x = int(input("Ingrese cuántos números desea sumar: "))
resultado = sumar(x)
print(f"La suma total es: {resultado}")
 """

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