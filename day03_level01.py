#Día 3: 30 días de programación en Python

Datos="""
-------- EJERCICIOS DEL DIA NUMERO 3  --------
  Nombre: Damian Ezequiel Solis Rodriguez
  Fecha: 11/06/2025
  Materia: Programación Estructurada
  Unidad: U2
----------------------------------------------
"""

# Exercises - Day 3

import os
import math

Mi_Edad=int(21)
Mi_Estatura=float(1.86)
mi_numero_complejo = 34j


print("-------------------------------------------------------------------------------------------------- \n")
print(Datos, "\n")
print("-------------------------------------------------------------------------------------------------- \n")


input("Presiona \"ENTER\" para continuar en el programa (calculo del triangulo area)......")
os.system('cls' if os.name == 'nt' else 'clear')


#python mi_script.py (un "script" es un archivo que contiene un codigo ejecutable ".py")

base_Triangulo=float(input("Ingresa a continuacion la base del triangulo: "))
altura_Triangulo=float(input("Ingresa a continuacion la altura del traingulo: "))
print("\n")
print("!--------------------> Altura : ",altura_Triangulo ,"\n")
print("!  \"TRIANGULO\" \n")
print("!     *\n")
print("!    ***\n")
print("!   *****\n")
print("!  ********")
print("_____________ ---------> Base:  ",base_Triangulo,"\n")
print("formula para obtener el Area : a=(base*altura)/2 \n")


#formula para obtener area de un traingulo
# Area= (base*altura)/2
# Area= (base*altura)/2
Area_Triangulo = (base_Triangulo * altura_Triangulo) / 2
print(f"Cálculo: ({base_Triangulo} * {altura_Triangulo}) / 2 = {Area_Triangulo:.2f}")
print(f"EL AREA TOTAL DEL TRIANGULO ES: {Area_Triangulo:.2f}\n")

#(área = 0,5 x b x h).
"""
# Área conocida
area = 0.5

# Fórmula original: área = 0.5*b*h

# Paso 1: Despejar b*h
producto = area / 0.5  # Dividimos ambos lados entre 0.5

# Mostrar el resultado
print("Resultado de b*h:", producto)  # Esto debe dar 1.0

"""
input("Presiona \"ENTER\" para continuar en el programa (calculo del triangulo perimetro)......")
os.system('cls' if os.name == 'nt' else 'clear')


#Perimetro=math.sqrt((base_Triangulo / 2) ** 2 + altura_Triangulo ** 2)
lado = math.sqrt((base_Triangulo / 2) ** 2 + altura_Triangulo ** 2)
Perimetro_Triangulo = base_Triangulo + 2 * lado

print("!--------------------> Altura : ",altura_Triangulo ,"\n")
print("!  \"TRIANGULO\" \n")
print("!     *\n")
print("!    ***\n")
print("!   *****\n")
print("!  ********")
print("_____________ ---------> Base:  ",base_Triangulo,"\n")
print("formula para obtener el Perimetro : sqrt((base_Triangulo / 2) ** 2 + altura_Triangulo ** 2) \n")
print(f"EL PERIMETRO TOTAL DEL TRINGULO ES: {Perimetro_Triangulo:.2f}" ,"\n")

a=5; b=4; c=3
Calcula_Perimetro=a+b+c
print("Perimetro de tringulo de la suma de lados: ",Calcula_Perimetro , "\n\n")

#Get length and width of a rectangle 

"""
1) Área = largo * ancho
2) Perímetro = 2 * (largo + ancho)
"""

input("Presiona \"ENTER\" para continuar en el programa (calculo del rectangulo)......")
os.system('cls' if os.name == 'nt' else 'clear')


largo = float(input("Ingresa el largo del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))
print("\n")
# figura del rectangulo
print(f"--------------------------> Alto :{largo}")
print("!  \"RECTÁNGULO\"  \n")
print("!  ***********     \n")
print("!  ***********     \n")
print("!  ***********     \n")
print("!  ***********     \n")
print(f"________________ ---------> Ancho:{ancho}\n")


# Área y perímetro de un rectángulo
area_rect = largo * ancho
perimetro_rect = 2 * (largo + ancho)

print(f"Área del rectángulo: {area_rect}")
print(f"Perímetro del rectángulo: {perimetro_rect}  \n")  

input("Presiona \"ENTER\" para continuar en el programa. (calculo del circulo).....")
os.system('cls' if os.name == 'nt' else 'clear')

print("----------------------------------------------------------------- \n")
# Área y circunferencia de un círculo
radio = float(input("Ingresa el radio del círculo: "))
pi = 3.14
area_circulo = pi * radio ** 2
circunferencia = 2 * pi * radio
print(f"Área del círculo: {area_circulo:.2f}")
print(f"Circunferencia del círculo: {circunferencia:.2f} \n")
print("----------------------------------------------------------------- \n\n")
input("Presiona \"ENTER\" para continuar en el programa......")
os.system('cls')
# Calcular la pendiente, la intersección con el eje x y la intersección con el eje y de y = 2x -2
m = 2
y_intercept = -2
x_intercept = 1  # Porque 0 = 2x - 2 → x = 1
print(f"Pendiente: {m}, x-intercept: {x_intercept}, y-intercept: {y_intercept}")


# Pendiente y distancia entre puntos (2,2) y (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Pendiente: {pendiente}, Distancia: {distancia}")

# 11 y 12

"""
Calcula el valor de y (y = x^2 + 6x + 9). Intenta usar 
diferentes valores de x y determina en qué valor de x y será 0.
Encuentra la longitud de "python" y "dragon" y haz una c
omparación falsa.
"""

for x in range(-10, 10):
    y = x**2 + 6*x + 9
    print(f"x={x}, y={y}")

input("Presiona \"ENTER\" para continuar en el programa......")
os.system('cls')

print("----------------------------------------------------------------- \n")
# Comparar longitud de 'python' y 'dragon'
print(len('python') != len('dragon')) 

# and para verificar si 'on' está en ambos
print('on' in 'python' and 'on' in 'dragon')

# Verificar si 'jargon' está en una oración:
print('jargon' in 'I hope this course is not full of jargon')


# No hay 'on' tanto en dragon como en python
print('on' not in 'dragon' and 'on' not in 'python')


# Longitud de ‘python’, convertir a float y luego a string
length = len('python')
print(float(length))
print(str(length))

print("----------------------------------------------------------------- \n\n")
# Verificar si número es par utilizando el operador aritmetico % (mod == modulo)
num = int(input("Ingresa un número para comprobar si es par o impar: "))
print(f"El numero que elejistes que fue [{num}] es == {num % 2 == 0}")
print("----------------------------------------------------------------- \n")

# Compruebe si la división del 7 por 3 es igual al valor convertido int de 2,7.
print(7 // 3 == int(2.7))


# Comprueba si el tipo de '10' es igual al tipo de 10
print(type('10') == type(10))  # False

# Comprueba si int('9.8') es igual a 10 ---> se utiliza float ya que es decimal
print(float('9.8') == 10)
print("----------------------------------------------------------------- \n\n")

# solicite al usuario ingresar las horas y la tarifa por hora. ¿Cómo calcular el salario de la persona?
horas = float(input("Horas trabajadas: "))
tarifa = float(input("Tarifa por hora: "))
pago = horas * tarifa
print(f"Tu ganancia semanal es: {pago}")
print("----------------------------------------------------------------- \n\n")

# igresar años vividos, calcular segundos vividos
anios = int(input("¿Cuántos años has vivido?: "))
segundos = anios * 365 * 24 * 60 * 60
print(f"Has vivido por {segundos} segundos.")
print("----------------------------------------------------------------- \n")

input("Presiona \"ENTER\" para continuar en el programa......")
os.system('cls' if os.name == 'nt' else 'clear')


# Escriba un script en Python que muestre la siguiente tabla
Ejemplo_tabla="""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
print(f"Escriba un script en Python que muestre la siguiente tabla : \n {Ejemplo_tabla} \n\n")

print("LA TABLA DE ABAJO MUESTRA LA REPLICA DE ORDEN DE LA TABLA SOLICITADA AL DE ARRIBA")
for i in range(1, 6):
    print(f"{i} {1} {i} {i**2} {i**3}")
