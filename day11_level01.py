# -------------------------------------------
# LEVEL 1
# -------------------------------------------

# Ejercicio 1: Sumar dos números
def sumar_dos_numeros(num1, num2):
    return num1 + num2

# Ejercicio 2: Calcular área de un círculo
import math

def area_circulo(radio):
    return math.pi * radio * radio

# Ejercicio 3: Sumar números arbitrarios
def sumar_todos(*numeros):
    suma = 0
    for n in numeros:
        if not isinstance(n, (int, float)):
            return "Error: Todos los valores deben ser números."
        suma += n
    return suma

# Ejercicio 4: Convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(grados_c):
    return (grados_c * 9/5) + 32

# Ejercicio 5: Checar estación del año
def checar_estacion(mes):
    mes = mes.lower()
    if mes in ['septiembre', 'octubre', 'noviembre']:
        return "Otoño"
    elif mes in ['diciembre', 'enero', 'febrero']:
        return "Invierno"
    elif mes in ['marzo', 'abril', 'mayo']:
        return "Primavera"
    elif mes in ['junio', 'julio', 'agosto']:
        return "Verano"
    else:
        return "Mes inválido"

# Ejercicio 6: Calcular pendiente
def calcular_pendiente(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Ejercicio 7: Resolver ecuación cuadrática
def resolver_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No tiene soluciones reales"
    elif discriminante == 0:
        x = -b / (2*a)
        return [x]
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return [x1, x2]

# Ejercicio 8: Imprimir elementos de una lista
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

# Ejercicio 9: Revertir lista con loop
def reversa_lista(lista):
    lista_invertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

# Ejemplo
print(reversa_lista([1,2,3,4,5]))
print(reversa_lista(["A", "B", "C"]))

# Ejercicio 10: Capitalizar elementos de una lista
def capitalizar_lista(lista):
    lista_mayusculas = []
    for item in lista:
        lista_mayusculas.append(str(item).capitalize())
    return lista_mayusculas

# Ejercicio 11: Agregar item a una lista
def agregar_item(lista, item):
    lista.append(item)
    return lista

# Ejemplo
comida = ['Papa', 'Tomate', 'Mango', 'Leche']
print(agregar_item(comida, 'Carne'))

numeros = [2,3,7,9]
print(agregar_item(numeros, 5))

# Ejercicio 12: Eliminar item de una lista
def eliminar_item(lista, item):
    if item in lista:
        lista.remove(item)
    return lista

# Ejemplo
comida = ['Papa', 'Tomate', 'Mango', 'Leche']
print(eliminar_item(comida, 'Mango'))

numeros = [2,3,7,9]
print(eliminar_item(numeros, 3))

# Ejercicio 13: Sumar números hasta n
def suma_de_numeros(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

# Ejemplo
print(suma_de_numeros(5))
print(suma_de_numeros(10))
print(suma_de_numeros(100))

# Ejercicio 14: Sumar impares hasta n
def suma_impares(n):
    suma = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            suma += i
    return suma

# Ejercicio 15: Sumar pares hasta n
def suma_pares(n):
    suma = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            suma += i
    return suma