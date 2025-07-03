"""
# ================================================================
# 🚨 Reglas de la evaluación (LEER ANTES DE COMENZAR)
# ================================================================
# - La evaluación debe realizarse de forma individual.
# - Está estrictamente prohibido el plagio:
#     - No copies código de otros compañeros.
#     - No busques soluciones en internet.
#     - No uses IA como ChatGPT, Copilot u otras herramientas externas.
# - Solo puedes tener abierto:
#     - Este archivo en Codespaces (VS Code en el navegador)
#     - El repositorio de GitHub de esta tarea.
# - Si se detecta copia o incumplimiento de estas reglas,
#   la calificación será cero.
# ================================================================

# Ingresa el número del ejercicio que deseas ejecutar (del 1 al 10):
ejercicio = input().strip()

# --- Ejercicio 1 ---
if ejercicio == "1":
    # Imprime una línea de saludo usando concatenación de strings.
    # Debe decir exactamente: ¡Bienvenido, estudiante de Python!
    parte1 = "¡Bienvenido"
    parte2 = "estudiante de Python!"
    
    print(f"concatenación de strings: {parte1+parte2}")
    pass

# --- Ejercicio 2 ---
elif ejercicio == "2":
    # Calcula el cuadrado de la suma de 3 y 5.
    # Resultado esperado: 64
    a = 3
    b = 5
    Cuadrado=((a+b)**2)
    print(f"Resultado eperado: {cuadrado}")
    pass

# --- Ejercicio 3 ---
elif ejercicio == "3":
    # Convierte el texto "3.14" a tipo float y súmale 2.86
    # Resultado esperado: 6.0
    texto = "3.14"
    texto_dos=float(texto)
    suma = (texto_dos + 2.86)
    print(f"Resultado esperado: {suma}")
    pass

# --- Ejercicio 4 ---
elif ejercicio == "4":
    # Dado el texto "programación", imprime cuántas letras tiene
    # SIN contar vocales acentuadas (ó cuenta como o).
    texto = "programación"
    print(f"cuantas letras tiene texto: {len(texto)} letras")
    print(f"contar las vocales y tambien el str: {len(texto)}")
    pass

# --- Ejercicio 5 ---
elif ejercicio == "5":
    # Imprime el menor número entre -3, 0 y 2 multiplicado por -1
    # Resultado esperado: 3
    a = -3
    b = 0
    c = 2
    #numero_menor=()
    pass

# --- Ejercicio 6 ---
elif ejercicio == "6":
    # Dados los valores nombre = "Ana" y edad = 21,
    # imprime exactamente: Nombre: Ana - Edad: 21 años
    nombre = "Ana"
    edad = 21
    print(f"{nombre} - Edad: {edad}")
    pass

# --- Ejercicio 7 ---
elif ejercicio == "7":
    # Dado el booleano `acceso = True`, imprime:
    # Acceso permitido si acceso es True, o Acceso denegado si es False.
    acceso = True
    if acceso==True:
        print("Acceso permitido")
    else
        print("Acceso denegado")
    pass

# --- Ejercicio 8 ---
elif ejercicio == "8":
    # Dado el string "robot", imprime sus caracteres separados por comas.
    # Resultado esperado: r,o,b,o,t
    palabra = "robot"
    print(",".join(palabra))
    pass

# --- Ejercicio 9 ---
elif ejercicio == "9":
    # Dado el texto "  hola mundo  ", imprime la frase en mayúsculas
    # sin espacios al inicio ni al final.
    texto = "  hola mundo  "
    print((texto.upper()))
    pass

# --- Ejercicio 10 ---
elif ejercicio == "10":
    # Imprime exactamente el siguiente bloque de texto:
    # Línea 1:\tInicio
    # Línea 2:\tProceso
    # Línea 3:\tFin
    print("Linea 1:\tInicio")
    print("Linea 2:\tProceso")
    print("Linea 3:\tFin")
    pass

# --- Entrada inválida ---
else:
    print("Ejercicio inválido. Ingresa un número del 1 al 10.")

"""

# 'Day 2: 30 Days of python programming'

import math

Nombre='Damian'
Apellido='Solis'
Completo='Damian Ezequiel Solis'
pais='Mexico'
Ciudad='Aguascalientes'
año=2025
Casada=True
Luz_Encendida=False

Variable_una_Linea, float_uno, no= 12, 12.7, False

print(type(Nombre))
print(type(Apellido))
print(type(Completo))
print(type(pais))
print(type(Ciudad))
print(type(año))
print(type(Casada))
print(type(Luz_Encendida))
print(type(Variable_una_Linea))
print(type(float_uno))
print(type(no))

Longitud_Nombre=len(Nombre)
Longitud_Apellido=len(Apellido)

Comparacion_len=(Longitud_Nombre>Longitud_Apellido) or (Longitud_Apellido>Longitud_Nombre) or (Longitud_Nombre==Longitud_Apellido)
print(f"la mayor longitud entre el apellido y el nombre es = {Comparacion_len} \n")


num_one=5

num_two=4

#Respuesta 

total=num_one+num_two

diff=num_two-num_one

product=num_two*num_one

division=num_one/num_two

residuo=num_two%num_one

exp=num_one**num_two

floor_division=num_one//num_two

Radio_Circle=30.0
area_of_circle=math.pi*(Radio_Circle**2)

circum_of_circle=(2*math.pi)*Radio_Circle

Radio=float(input("Ingersa el Radio:"))

# Esta bien esto pero 
Calcula_Radio_Entrada_Usuario=(math.pi*Radio)**2
# Mejor utiliza esto para calculo de radio (para el calculo del area)
# Calcula_Radio_Entrada_Usuario = math.pi * (Radio ** 2)

Nombre = input("Ingresa tu nombre: ")
Apellido=input("Ingresa tu apellido:")
Pais=input("Ingresa tu pais:")
edad=input("Ingresa tu edad:")




# Dia 3

edad=21
float=1.87
coplex=5j

base=float(input("Ingresa la base:"))
Altura=float(input("Ingresa la altura:"))

area_triangulo=(0.5*base*Altura)
print(f"The area of the triangle is: {area_triangulo}")

a=float(input("Ingresa el lado a:"))
b=float(input("Ingresa el lado b:"))
c=float(input("Ingresa el lado c:"))

perimetro_traingulo=a+b+c
print(f"The perimeter of the triangle is: {perimetro_traingulo}")









