#Level 2

#Ejercicio 1: Suma de todos los números del 0 al 100
suma_total = 0

for numero in range(101):
    suma_total += numero

print("La suma de todos los números es:", suma_total)


#Ejercicio 2: Suma de pares e impares
suma_pares = 0
suma_impares = 0

for numero in range(101):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print("La suma de los pares es:", suma_pares)
print("La suma de los impares es:", suma_impares)



