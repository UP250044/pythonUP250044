#Level_03:

#Día 1: 30 días de programación en Python

import math

Datos="""
-------- EJERCICIOS DEL DIA NUMERO 1  --------
  Nombre: Damian Ezequiel Solis Rodriguez
  Fecha: 11/06/2025
  Materia: Progremacion Estructurada
  Unidad: U2
----------------------------------------------
"""

#Exercise: Level 3 (data types)

Integer=230
Float=46.64
Complex=37j
String='Hola , esto es una cadena de texto'
Boolean=False
#List and Tuple
List=['HOLA ESTO ES UNA LISTA',True,234,2.3467,'Dami']

#Uso de Listas y como utilizarlas (La lista si se pueden modificar una vez creadas)

#-----> SE ACCEDE A CADA UNO DE SUS ELEMENTOS INDICANDO LA POSICIÓN DE ESTE
print(f"Imprimir posición 3: {List[3]}") 

#-----> SE PUEDE INDICAR LA POSICIÓN AL REVÉS (índices negativos)
print(f"Imprimir posición -3: {List[-3]}") 

#-----> ESTO INDICA QUE QUIERO IMPRIMIR EL ÍNDICE 1 PERO TAMBIÉN EL 3
print(f"Imprimir posición 1 y 3: {List[1]} y {List[3]}")


"""
para modificar el elemento que esta dentro de unos de los
indices de la lista se deve hacer lo siguiente: 

List=['HOLA ESTO ES UNA LISTA',True,234,2.3467,'Dami']

depues :

List[2]='Hola , que tal estas?'
print(List[2])

"""

#TUPLAS,CONJUNTOS,DICIONARIOS 
#https://www.youtube.com/watch?v=v25-m1LOUiU

#LOS TUPLAS (NO SE PUEDEN MODIFICAR UNA VEZ CREADAS)
Tuple=('x',False,34.5,'¿la tierra es plana?')

# print(Tupe.caout(False)
# print(Tuple.index('x'))
"""
Para imprimir se usan [] al igual que 
las listas 

existen los metodos 
1) .index(indicar_pocision)
2) .append(indicar_pocision)
3) .caout(indicar_pocision)
4) .remove(indicar_pocision)

1) nos devuelbe la pocision de la primera aparicion de un elemento
2) nos permite agregar un elemento al final
3) nos devuelbe el numero de veces que se repite un elemento
4) nos elimina la primera aparicion de un elemento
"""
#set=Conjunto
"""
caracteristicas:
*No ordenados
*Heterogenios
*mutaples
*no repetitivos

Operadores (simbologia)
Union = A!B
diferencia= A-B
superconjunto= A>=B
Interseccion= A&B
Diferencia simetrica= A^B
Subconjunto= A<=B
"""
set_One= set([5,67,True,23.5,'HOLA ESTO ES UNA LISTA EN UN CONJUNTO'])
set_Two= set((2,45,34,False,2,56))
set_Tree= set("Esto es un String <str>") #se intepreta como un conjunto de char

#ejemplos de elementos repetitivos
conjunto=set([4,2,3,3,4,6,7])
print(conjunto)
"""
metodos de los cojuntos 

1) .add(indicar_lo que quieras añadir) = para añadir un elemento
2) .remove(indicar_el numero que deseas eliminar) = decir que elemento eliminar

Realizar operaciones de conjuntos:
conjunto_2=set([5,3,5,6])
conjunto_3=set([4,2])

print(conjunto,conjunto_2,conjunto_3)
# esto sirve para ver la intersecion entre conjuntos
print(conjunto.intersection(conjunto_2))
pero tambien puedes usar "&"
print(conjunto & conjunto_2)
imprime= {3}

#con (issubset) es para ver si los elementos de un conjunto
#estan incluidos en el otro arrojando valores bool

print(conjunto_2.issubset(conjunto))
imprime = False

"""
Dictionary={23:'pepe',21:'Damian',49:'Oscar',16:'Damary',20:'Dulce'}

"""

"""
#Find an Euclidian distance between (2, 3) and (10, 8)
"""
FORMULA :

Distancia=(sqrt((x_2-x_1)^2+(y_2-y_1)^2)

"""
# (2,3)
x_1=2
x_2=10

# (10,8)
y_1=3
y_2=8

Distancia=float((((x_2-x_1)**2)+((y_2-y_1)**2)))
Distancia=(math.sqrt(Distancia))

print(f"La distancia entre (2,3) y (10,8) es: {Distancia:.2f}")