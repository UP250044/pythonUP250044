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