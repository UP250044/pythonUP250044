# -------------------------------------------
# LEVEL 3
# -------------------------------------------

# Ejercicio 1: Comprobar si es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True

# Ejercicio 2: Comprobar si todos los elementos son únicos
def elementos_unicos(lista):
    return len(lista) == len(set(lista))

# Ejercicio 3: Comprobar si todos los elementos son del mismo tipo
def mismo_tipo(lista):
    tipo = type(lista[0])
    for item in lista:
        if type(item) != tipo:
            return False
    return True

# Ejercicio 4: Validar nombre de variable en Python
def es_variable_valida(nombre):
    return nombre.isidentifier()

# Ejercicio 5: Idiomas más hablados del mundo
from data.countries_data import countries_data
from collections import Counter

def idiomas_mas_hablados(top=10):
    contador_idiomas = Counter()
    for pais in countries_data:
        for idioma in pais['languages']:
            contador_idiomas[idioma] += 1
    return contador_idiomas.most_common(top)

# Ejemplo
print(idiomas_mas_hablados(10))

# Ejercicio 6: Países más poblados
def paises_mas_poblados(top=10):
    paises_ordenados = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return [(pais['name'], pais['population']) for pais in paises_ordenados[:top]]

# Ejemplo
print(paises_mas_poblados(10))