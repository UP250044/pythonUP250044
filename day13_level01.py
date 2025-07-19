#Level 01

# -------------------------------------------
# Ejercicio 1: Filtrar solo negativos y ceros con list comprehension
# -------------------------------------------

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negativos_y_cero = [n for n in numbers if n <= 0]
print(negativos_y_cero)


# -------------------------------------------
# Ejercicio 2: Aplanar lista de listas de listas
# -------------------------------------------

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

lista_aplanada = [numero for sublista in list_of_lists for grupo in sublista for numero in grupo]
print(lista_aplanada)


# -------------------------------------------
# Ejercicio 3: Crear lista de tuplas con potencias
# -------------------------------------------

lista_tuplas = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(lista_tuplas)


# -------------------------------------------
# Ejercicio 4: Aplanar países a lista con formato especial
# -------------------------------------------

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

paises_formateados = [[pais.upper(), pais[:3].upper(), ciudad.upper()] 
                      for lista in countries 
                      for (pais, ciudad) in lista]

print(paises_formateados)


# -------------------------------------------
# Ejercicio 5: Convertir lista a lista de diccionarios
# -------------------------------------------

diccionarios_paises = [{'country': pais.upper(), 'city': ciudad.upper()} 
                        for lista in countries 
                        for (pais, ciudad) in lista]

print(diccionarios_paises)


# -------------------------------------------
# Ejercicio 6: Concatenar nombres en strings
# -------------------------------------------

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

nombres_completos = [f"{nombre} {apellido}" for lista in names for (nombre, apellido) in lista]
print(nombres_completos)


# -------------------------------------------
# Ejercicio 7: Lambda para pendiente o intersección en funciones lineales
# -------------------------------------------

# y = mx + b -> pendiente (m) = (y2 - y1) / (x2 - x1)
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# y-intercepto (b) = y - m*x
intercepto = lambda m, x, y: y - m * x

# Ejemplo de uso:
print("Pendiente:", pendiente(1, 2, 3, 6))  # m = 2.0
print("Intercepto:", intercepto(2, 1, 2))   # b = 0