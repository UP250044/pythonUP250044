#Exercises: Level 1

Tupla_Vacia=()

sisters=('Luz maria','Damary Alexa','Dana Alexandra')
brothers=('Alan fernando','Oscar alejandro','Damian Fernando')

siblings=brothers + sisters

print(f"Cuantos hermanos tienes :  {len(siblings)} hermanos & hermanas\n")

parents=('Oscar solis acosta','Luz elena Rodriguez')
# Crear tupla family_members combinando
family_members = siblings + parents

#Exercises: Level 2

mother='Luz elena Rodriguez'
father='Oscar solis acosta'

# Desempaquetar
*siblings_unpacked,mother,father=family_members
print(f"Hermanos/Hermanas: {siblings_unpacked}\n")
print(f"mother: {mother}\n")
print(f"father: {father}\n")

frutas=('platano', 'naranja', 'mango', 'limon','Manzana')
verduras=('calabaza', 'zanahoria','papa','jitomate','tomate','cebolla')
Productos_Animales=('Leche','queso','yogurt','pollo',)

food_stuff_tp=frutas+verduras+Productos_Animales
print("Tupla completa de alimentos:", food_stuff_tp)

food_stuff_lt=list(food_stuff_tp)
print("Lista de alimentos:", food_stuff_lt)

middle_index = len(food_stuff_lt) // 2
print(f"Elemento del medio: {food_stuff_lt[middle_index]}")

primeros_tres_Elementos=food_stuff_lt[:3]
Ultimos_tres_Elementos=food_stuff_lt[-3:]

print(f"Los primero 3 elementos del inicio de la list: {food_stuff_lt} \n primero 3 lementos: {primeros_tres_Elementos} \n ltimos 3 elementos: {Ultimos_tres_Elementos} \n")

del food_stuff_tp

# del food_stuff_tp
# Si luego tratas de usarla, dará error 
# porque ya no existe.


nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print(f" comprobar si 'Estonia' es un pais nordico: {'Estonia' in nordic_countries}\n")  # False
print(f"comprobar si 'Icland' es un pais nordico:   {'Iceland' in nordic_countries}\n")  # True


"""
Separar el elemento o elementos del medio de la 
tupla food_stuff_tp o de la lista food_stuff_lt.
Separar los tres primeros y los tres últimos 
elementos de la lista food_staff_lt.
Eliminar la tupla food_staff_tp por completo.
Comprobar si un elemento existe en la tupla:
Comprobar si 'Estonia' es un país nórdico.

Comprobar si 'Islandia' es un país nórdico.
"""


