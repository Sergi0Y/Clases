
# EJEMPLO DE LISTA
""" 
nombreDeLista = ["String",int,bool,float]
lista = {"texto",4,True,5.7}
"""
#IMPRIMIR UNA LISTA
""" 
nombreLista = [1,2,3,4,5,1,2,3]
print(nombreLista[5]) """

#MÉTODOS
#----------SIZE------------
#LEN
""" 
list = [1,2,3,4,5]
x = len(list)
print(f"La cantidad de elementos de mi lista es {x}\n") """

#------------ ADD -------------------
#APPEND
"""
frutas = ["Manzana","Pera","Naranja"]
frutas.append("Piña")
print(frutas)
"""
#INSERT
"""
frutas = ["Manzana","Plátano","Pera","Naranja"]
print(frutas)
frutas.insert(1,"Piña")
print(frutas)
"""

# EXTEND
""" 
frutas = ["Manzana"]
print(frutas)
frutas.extend(["Plátano","Pera","Naranja"])
print(frutas)


a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)  # [1, 2, 3, 4]

"""

# --------------REMOVE-----------------
#DEL

"""
frutas = ["Manzana","Plátano","Pera","Naranja"]
print(frutas)
del frutas[1]
print(frutas)
"""

#BUCLE DEL
""" 
frutas = ["Manzana","Plátano","Pera","Naranja"]
print(frutas)
while frutas:
    del frutas[0]
    print(frutas)
"""

#REMOVE
""" 
frutas = ["Manzana","Plátano","Pera","Naranja"]
frutas.remove("Pera")
print("\n",frutas,"\n")
frutas.remove("Pera") #error no existe
"""

#POP

""" 
frutas = ["Manzana","Plátano","Pera","Naranja"]
frutas.pop()
print(frutas)

frutas = ["Manzana","Plátano","Pera","Naranja"]
x=frutas.pop()
papalera = [x]
print(papalera)
print("\n",frutas,"\n")
"""

#CLEAR
""" 
frutas = ["Manzana","Plátano","Pera","Naranja"]
frutas.clear()
print("\n",frutas,"\n")
"""

#SLICE

""" 
lista=["I","P","C","H","I","L","E"]
print(lista)
#primeros 3 elementos
print(lista[:3])

#desde el 4 hasta el final
print(lista[4:])


#desde el 1 hasta el 5
print(lista[1:5])

#orden inverso
print(lista[::-1])
"""

""" 

# 1. Lista completa

print("Lista completa:", lista[:])

# 2. Primeros cinco elementos

print("Primeros cinco elementos:", lista[:5])

# 3. Desde el índice 4 hasta el final

print("Desde el índice 4 hasta el final:", lista[4:])

# 4. Elementos desde el índice 2 al 6

print("Elementos desde el índice 2 al 6:", lista[2:7])

# 5. Cada segundo elemento

print("Cada segundo elemento:", lista[::2])

# 6. Cada tercer elemento

print("Cada tercer elemento:", lista[::3])

# 7. Lista en orden inverso

print("Lista en orden inverso:", lista[::-1])

# 8. Lista inversa tomando cada segundo elemento

print("Inversa, cada segundo elemento:", lista[::-2])

# 9. Desde el quinto elemento contado hasta el final

print("Últimos cinco elementos:", lista[-5:])

# 10. Elementos desde el índice -7 hasta el -3 (sin incluir)

print("Elementos desde -7 hasta -3:", lista[-7:-2])

# 11. Inversa desde el tercer elemento desde el final hasta el inicio

print("Inversa desde el índice -3 al inicio:", lista[-3::-1])

# 12. Inversa desde el índice -2 tomando cada segundo elemento

print("Inversa desde -2, cada segundo elemento:", lista[-2::-2])

# 13. Primeros tres elementos

print("Primeros tres elementos:", lista[:3])

# 14. Últimos tres elementos

print("Últimos tres elementos:", lista[-3:])

 """


# RECORRIENDO LISTAS
#FOR
""" list = [1,2,3,4,5]
x = len(list)

print("Imprimir lista con for simple")
for val in list:
    print(val)

print("Imprimir lista con for y len")

list = [1,2,3,4,5]

for i in range(x):
    print(list[i])

"""

#WHILE
""" while i<len(list):
    print(list[i])
    i+=1 """


#-----------MÉTODOS----------

#APPEND
""" 
frutas = ["Manzana", "Plátano"]
frutas.append("Pera")
print(frutas)  # ['Manzana', 'Plátano', 'Pera']
"""

#SORTED
""" list = [3,6,2,8,4,0,5]
x=sorted(list)
order_list =[]
for i in list:
    order_list.extend([i])
print(order_list)
print(x)
i=0

"""

#DEEPCOPY
""" 
import copy
lista = [1,2,3,4,5,6]

x = copy.deepcopy(lista)

print(x)
 """

#CLEAR
""" 
nombres = ["Ana", "Luis", "Pedro"]
nombres.clear()
print(nombres)  # []
"""

#COUNT
""" 
numeros = [1, 2, 2, 3, 2, 4]
veces = numeros.count(2)
print(veces)  # 3
"""

#EXTEND
""" 
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)  # [1, 2, 3, 4] 
"""

#INDEX
""" 
letras = ['a', 'b', 'c', 'd']
pos = letras.index('c')
print(pos)  # 2
"""

#INSERT
""" 
nombres = ['Ana', 'Pedro']
nombres.insert(1, 'Luis')
print(nombres)  # ['Ana', 'Luis', 'Pedro'] 
"""

#POP
""" 
colores = ['rojo', 'verde', 'azul']
x = colores.pop()
print(x)        # azul
print(colores)  # ['rojo', 'verde']
"""

#REMOVE
""" 
nombres = ['Ana', 'Luis', 'Luis', 'Pedro']
nombres.remove('Luis')
print(nombres)  # ['Ana', 'Luis', 'Pedro']
"""

#REVERSE

""" nums = [1, 2, 3]
nums.reverse()
print(nums)  # [3, 2, 1]
"""

