# -------------------------------------------
# LEVEL 2
# -------------------------------------------

# Ejercicio 1: Contar pares e impares
def pares_e_impares(n):
    pares = 0
    impares = 0
    for i in range(n+1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"El número de pares es {pares}")
    print(f"El número de impares es {impares}")

# Ejemplo
pares_e_impares(100)

# Ejercicio 2: Factorial
def factorial(num):
    resultado = 1
    for i in range(1, num+1):
        resultado *= i
    return resultado

# Ejercicio 3: Checar si está vacío
def esta_vacio(valor):
    return not bool(valor)

# Ejercicio 4: Funciones estadísticas
def calcular_media(lista):
    return sum(lista)/len(lista)

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista)
    medio = n // 2
    if n % 2 == 0:
        return (lista_ordenada[medio-1] + lista_ordenada[medio])/2
    else:
        return lista_ordenada[medio]

def calcular_moda(lista):
    from collections import Counter
    contador = Counter(lista)
    return contador.most_common(1)[0][0]

def calcular_rango(lista):
    return max(lista) - min(lista)

def calcular_varianza(lista):
    media = calcular_media(lista)
    return sum((x - media) ** 2 for x in lista) / len(lista)

def calcular_desviacion(lista):
    import math
    return math.sqrt(calcular_varianza(lista))