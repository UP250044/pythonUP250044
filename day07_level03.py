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
