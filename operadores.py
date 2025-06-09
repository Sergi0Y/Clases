# OPERADORES ARITMÉTICOS

""" 
a = 2
b = 3
print("2 + 3 = ",a + b)
print("2 - 3 = ", a - b)
print("2 * 3 = ",a * b)
print("2 / 3 = ",a / b)
print("2 ** 3 = ",a ** b)
"""


""" 
print("división normal",14/5)
print("división truncada",14//5)
print("resto de la división",14%5)
"""

# OPERADORES DE COMPARACIÓN

""" 
a = 2
b = 3
print("\n2 < 3" ,a < b)
print("2 > 3" ,a > b)
print("2 == 3" ,a == b)
print("2 != 3" ,a != b)
print("2 <= 3" ,a <= b)
print("2 >= 3" ,a >= b,"\n")
"""

# OPERADORES LÓGICOS
""" 
a = True 
b = False
print("\na and b ",a and b)
print("a or b ",a or b)
print ("not a ",not a)
print ("not b ",not b, "\n")

"""

# OPERADORES DE ASIGNACIÓN
""" 
a = 10
b = a
print(b)

b += a
print("b += a")
print("es decir: b = b + a")
print("b vale 10, a vale 10, entonces:")
print("b = 10 + 10 = 20")
print("ahora b = 20")
print(b)

print("")
print ("\n1")


b -= a
print("b -= a")
print("es decir: b = b - a")
print("b vale 20, a vale 10, entonces:")
print("b = 20 - 10 = 10")
print("ahora b = 10")
print(b)

print("")
print("\n2")

b *= a
print("b *= a")
print("es decir b = b * a")
print("b vale 10, a vale 10, entonces:")
print("b = 10 * 10 = 100")
print("ahora b = 100")
print(b)

print("")

b <<= a
print("b <<= a")
print ("es equivalente a: b = b * (2 ** a)")
print(b)

"""


# BUCLE WHILE
""" 
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hola mundo")

cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hola mundo")
else:
    print("Bloque else")
 """    

# BUCLE DO WHILE

while True:
    numero = int(input("Ingresa un número mayor que 0: "))
    if numero > 0:
        break  # salimos del ciclo si la condición se cumple

# BUCLE FOR

""" n = 5
for i in range(0, n):
    print(i)

for e in range(1,6):
    print(e)
 """

for x in range(7):
    print (x)
    if x>4:
        break



# SWITCH O MATCH CASE

opcion = input("Elige una opción (1, 2, 3): ")

match opcion:
    case "1":
        print("Elegiste uno")
    case "2":
        print("Elegiste dos")
    case "3":
        print("Elegiste tres")
    case _:
        print("Opción no válida")


opcion = input("Elige una opción (1, 2, 3): ")

if opcion == "1":
    print("Elegiste uno")
elif opcion == "2":
    print("Elegiste dos")
elif opcion == "3":
    print("Elegiste tres")
else:
    print("Opción no válida")
