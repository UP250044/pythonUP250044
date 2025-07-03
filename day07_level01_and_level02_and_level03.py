
# Exercises: Level 1

"""
Obtener la longitud de it_companies

Agregar 'Twitter'

Agregar múltiples empresas a la vez

Eliminar una empresa

¿Diferencia entre remove() y discard()?
"""
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

Longitud=len(it_companies)

agregar=it_companies.add('Twitter')

# Agregar varias empresas a la vez
it_companies.update(['Twitter', 'Netflix', 'Tesla'])

print(f"Se agrego multiples empresas ala vez: {it_companies} \n")

# Eliminar una empresa específica
Elimina_empresa=it_companies.remove('Apple')
print(f"se elimino 'Apple' de la lista: {Elimina_empresa} \n")

# remove() elimina un elemento, pero lanza error si no existe.
Remove=it_companies.remove('Microsoft')

# discard() elimina un elemento, pero no lanza error si no existe.
Discard=it_companies.discard('Oracle')

##########################################################################

# Exercises: Level 2

"""
Unir A y B

Intersección entre A y B

¿A es subconjunto de B?

¿A y B son disjuntos?

Unir A con B y B con A

Diferencia simétrica entre A y B

Eliminar todos los conjuntos
"""
# Unir A y B
union_ab = A.union(B)
print("Unión de A y B:", union_ab)

# Intersección entre A y B
interseccion_ab = A.intersection(B)
print("Intersección de A y B:", interseccion_ab)

# ¿A es subconjunto de B?
Sub_Conjunto=A.issubset(B)
print("¿A es subconjunto de B?:", Sub_Conjunto)

# ¿A y B son disjuntos?0lo
Dis_justos=A.isdisjoint(B)
print("¿A y B son conjuntos disjuntos?:", Dis_justos)

# Unir A con B y B con A
A.update(B)
print("(A unido con B) and (B unido con A) :", A)

# Restauramos A y B a su forma original para unir al revés
A = {19, 22, 24, 20, 25, 26}
B.update(A)
print("B unido con A:", B)

# Diferencia simétrica entre A y B
simetrica = A.symmetric_difference(B)
print("Diferencia simétrica entre A y B:", simetrica)

# Eliminar todos los conjuntos
del A
del B

##########################################################################

# Exercises: Level 3
"""
Convertir age en conjunto y comparar su 
longitud con la lista

Explica la diferencia entre: s
tring, list, tuple y set

Frase:
"I am a teacher and I love to inspire and teach people."
¿Cuántas palabras únicas tiene? Usa .split() y set().
"""
# Convertir age en conjunto y comparar su longitud con la lista
age_set = set(age)

print("Longitud de la lista age:", len(age))
print("Longitud del conjunto age_set:", len(age_set))
print("Diferencia de longitud:", len(age) - len(age_set))

# Diferencia entre string, list, tuple y set
print("\nDiferencias entre tipos de datos:")
print("string ➜ texto inmutable y ordenado. Ejemplo: 'Hola'")
print("list   ➜ colección mutable y ordenada. Ejemplo: [1, 2, 3]")
print("tuple  ➜ colección inmutable y ordenada. Ejemplo: (1, 2, 3)")
print("set    ➜ colección mutable, no ordenada y sin duplicados. Ejemplo: {1, 2, 3}")

# Palabras únicas en una frase
frase = "I am a teacher and I love to inspire and teach people."
palabras = frase.split()
palabras_unicas = set(palabras)

print("\nPalabras únicas:", palabras_unicas)
print("Cantidad de palabras únicas:", len(palabras_unicas))
