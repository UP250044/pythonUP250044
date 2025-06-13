#Level_01 

# Día 2: 30 días de programación en Python

import os
import math

# Información del estudiante
Datos = """
-------- EJERCICIOS DEL DIA NUMERO 2  --------
  Nombre: Damian Ezequiel Solis Rodriguez
  Fecha: 11/06/2025
  Materia: Progremacion Estructurada
  Unidad: U2
----------------------------------------------
"""

# Variables con valores ingresados por el usuario
Primer_Nombre = input("ASIGNA UN VALOR A LA VARIABLE PRIMER_NOMBRE: ")
Apellido = input("ASIGNA UN VALOR A LA VARIABLE Apellido: ")
Nombre_Completo = input("Dime tu nombre completo: ")
Pais = input("ASIGNA UN VALOR A LA VARIABLE Pais: ")
Ciudad = input("ASIGNA UN VALOR A LA VARIABLE Ciudad: ")
Edad_Persona = int(input("ASIGNA UN VALOR A LA VARIABLE Edad_Persona: "))
Año = int(input("ASIGNA UN VALOR A LA VARIABLE AÑO: "))

is_married = False
is_true = True
is_light_on = False


print("\n\n\n")


input("Presiona \"ENTER\" para Continuar ejecucion del programa (level 02).....")
os.system('cls' if os.name == 'nt' else 'clear') #Limpia la consola 

# Variables booleanas y de cadena
Verdadero = False
Luz_Encendida = '"IMPORTANTE" LA LUZ SE ENCUENTRA APAGADA EN ESTOS MOMENTOS'

# Múltiples variables en una sola línea
Nombre, apellido, edad, dia, mes, año = 'Damian', 'Solis', 21, 2, 'Febrero', 2004

# Impresión de datos y tipos
print("-------------------------------------------------------------------------------------------------- \n")
print(Datos, "\n")
print("-------------------------------------------------------------------------------------------------- \n")
print("Mi primer nombre es: ", Primer_Nombre, "es un tipo de dato", type(Primer_Nombre), "\n")
print("Mi primer apellido es:", Apellido, "es un tipo de dato", type(Apellido), "\n")
print("Mi nombre completo: ", Nombre_Completo, "es un tipo de dato", type(Nombre_Completo), "\n")
print("Mi ciudad es: ", Ciudad, "es un tipo de dato", type(Ciudad), "\n")
print("Mi pais es: ", Pais, "es un tipo de dato", type(Pais), "\n")
print("Mi edad es: ", Edad_Persona, "es un tipo de dato", type(Edad_Persona), "\n")
print("Mi año es :", Año, "es un tipo de dato", type(Año), "\n")
print("--------------------------------------------------------------------------------------------------\n")
print("--------------------------------------------------------------------------------------------------\n")
print("#Variable de verdadero\n")
print("Verdadero =", Verdadero, "es un tipo de dato", type(Verdadero), "\n\n")
print("#Variable de luz encendida [es un tipo de dato", type(Luz_Encendida), "] \n")
print("Luz_Encendida = [", Luz_Encendida, "] es un tipo de dato", type(Luz_Encendida), "\n\n")
print("#Variables en una sola linea\n")
print("!--- Nombre,apellido,edad,dia,mes,año:")
print("! Hola me llamo:", Nombre, apellido, " mi fecha de nacimiento es: ", dia, "/", mes, "/", año, "\n")
print("------------------------------------------------------------------------------------------------ \n")

###############################################################################################################
input("Presiona \"ENTER\" para Continuar ejecucion del programa (level 02).....")
os.system('cls' if os.name == 'nt' else 'clear')


#Level_02

# Día 2: 30 días de programación en Python


# Información del estudiante
Datos = """
-------- EJERCICIOS DEL DIA NUMERO 2  --------
  Nombre: Damian Ezequiel Solis Rodriguez
  Fecha: 11/06/2025
  Materia: Progremacion Estructurada
  Unidad: U2
----------------------------------------------
"""

# Exercises: Level 2
print("----------------------------------------------------------------- \n")
# Longitud de nombre y apellido
print("La longitud del nombre: ", Primer_Nombre, "es de ", len(Primer_Nombre), "letras \n")
print("La longitud del apellido: ", Apellido, "es de ", len(Apellido), "letras \n\n")

# Comparación de longitud
print("# Comparación de la longitud del \"NOMBRE\" y \"APELLIDO\"")
if len(Primer_Nombre) > len(Apellido):
    print("\"EL NOMBRE ES MAYOR\" \n")
elif len(Primer_Nombre) < len(Apellido):
    print("\"EL APELLIDO ES MAYOR\" \n")
else:
    print("\"NOMBRE Y APELLIDO TIENEN LA MISMA LONGITUD\"\n")
print("----------------------------------------------------------------- \n")

input("Presiona \"ENTER\" para continuar.....")
os.system('cls' if os.name == 'nt' else 'clear')

# Operaciones matemáticas
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
divicion = num_one / num_two
modulus = num_one % num_two
Exp = num_one ** num_two
floor_division = num_one // num_two

# Cálculo del área y circunferencia de un círculo
Radio_Circulo = 30
area_of_circle = math.pi * (Radio_Circulo ** 2)

# Cálculo con input del usuario
Radio_two = float(input("Dime el valor del Radio del Circulo: "))
area_of_circle2 = math.pi * (Radio_two ** 2)
circunferencia = ((2 * math.pi) * Radio_two)

print(f"Radio: {Radio_two:.2f} m | Área: {area_of_circle2:.2f} m² | Circunferencia: {circunferencia:.2f} m \n")

input("Presiona \"ENTER\" para continuar.....")
os.system('cls' if os.name == 'nt' else 'clear')

# Inputs de datos del usuario
nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 22]
print(" esta  es la listab original = ['Ana', 'LIUS, 'CARLOS'] \n")
print(f"esta es la lista ordenada con [list(zip(nombres, edades))] == {list(zip(nombres, edades))} \n\n")

# Palabras clave de Python
input("Presiona \"ENTER\" para Finalizar ejecucion del programa.....")
os.system('cls' if os.name == 'nt' else 'clear')
print("\t--------------------> keywords\n")
help('keywords')