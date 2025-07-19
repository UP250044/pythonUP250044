#Level 1

#Ejercicio 1: For y While de 0 a 10
# Usando for
for numero in range(11):
    print(numero)

# Usando while
contador = 0
while contador <= 10:
    print(contador)
    contador += 1


#Ejercicio 2: For y While de 10 a 0
# Usando for
for numero in range(10, -1, -1):
    print(numero)

# Usando while
contador = 10
while contador >= 0:
    print(contador)
    contador -= 1


#Ejercicio 3: Triángulo de #
for fila in range(1, 8):
    print("#" * fila)

#Ejercicio 4: Cuadro de #
for fila in range(8):
    for columna in range(8):
        print("#", end=" ")
    print()




#Ejercicio 5: Tabla de multiplicar de cuadrados
for numero in range(11):
    print(f"{numero} x {numero} = {numero * numero}")

#Ejercicio 6: Iterar lista de tecnologías
tecnologias = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for tech in tecnologias:
    print(tech)


#Ejercicio 7: Números pares del 0 al 100
for par in range(0, 101):
    if par % 2 == 0:
        print(par)


#Ejercicio 8: Números impares del 0 al 100
for impar in range(0, 101):
    if impar % 2 != 0:
        print(impar)

