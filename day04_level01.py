
# 'Day 2: 30 Days of python programming'
 # -------------------------------------------
# Ejercicio 1: Concatenar cadenas
# -------------------------------------------

texto1 = 'Thirty'
texto2 = 'Days'
texto3 = 'Of'
texto4 = 'Python'

frase1 = texto1 + ' ' + texto2 + ' ' + texto3 + ' ' + texto4
print(frase1)

# -------------------------------------------
# Ejercicio 2: Concatenar 'Coding For All'
# -------------------------------------------

frase2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(frase2)

# -------------------------------------------
# Ejercicio 3: Declarar variable company
# -------------------------------------------

company = 'Coding For All'
print(company)

# -------------------------------------------
# Ejercicio 4: Longitud de company
# -------------------------------------------

print(len(company))

# -------------------------------------------
# Ejercicio 5: Cambiar a mayúsculas
# -------------------------------------------

print(company.upper())

# -------------------------------------------
# Ejercicio 6: Cambiar a minúsculas
# -------------------------------------------

print(company.lower())

# -------------------------------------------
# Ejercicio 7: Capitalize, title, swapcase
# -------------------------------------------

print(company.capitalize())
print(company.title())
print(company.swapcase())

# -------------------------------------------
# Ejercicio 8: Cortar la primera palabra
# -------------------------------------------

print(company[7:])

# -------------------------------------------
# Ejercicio 9: Comprobar si contiene "Coding"
# -------------------------------------------

print('Coding' in company)
print(company.index('Coding'))
print(company.find('Coding'))

# -------------------------------------------
# Ejercicio 10: Reemplazar 'Coding' por 'Python'
# -------------------------------------------

print(company.replace('Coding', 'Python'))

# -------------------------------------------
# Ejercicio 11: Reemplazar 'Python for Everyone' a 'Python for All'
# -------------------------------------------

frase3 = 'Python for Everyone'
print(frase3.replace('Everyone', 'All'))

# -------------------------------------------
# Ejercicio 12: Split con espacio
# -------------------------------------------

print(company.split())

# -------------------------------------------
# Ejercicio 13: Split con coma
# -------------------------------------------

empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(empresas.split(", "))

# -------------------------------------------
# Ejercicio 14: Primer caracter de 'Coding For All'
# -------------------------------------------

print(company[0])

# -------------------------------------------
# Ejercicio 15: Último índice de 'Coding For All'
# -------------------------------------------

print(len(company)-1)

# -------------------------------------------
# Ejercicio 16: Caracter en índice 10
# -------------------------------------------

print(company[10])

# -------------------------------------------
# Ejercicio 17: Acrónimo de 'Python For Everyone'
# -------------------------------------------

pfe = 'Python For Everyone'
acronimo_pfe = ''.join([palabra[0] for palabra in pfe.split()])
print(acronimo_pfe)

# -------------------------------------------
# Ejercicio 18: Acrónimo de 'Coding For All'
# -------------------------------------------

cfa = 'Coding For All'
acronimo_cfa = ''.join([palabra[0] for palabra in cfa.split()])
print(acronimo_cfa)

# -------------------------------------------
# Ejercicio 19: Posición de la primera C
# -------------------------------------------

print(company.index('C'))

# -------------------------------------------
# Ejercicio 20: Posición de la F
# -------------------------------------------

print(company.index('F'))

# -------------------------------------------
# Ejercicio 21: Última posición de 'l' en 'Coding For All People'
# -------------------------------------------

frase4 = 'Coding For All People'
print(frase4.rfind('l'))

# -------------------------------------------
# Ejercicio 22: Primera posición de 'because'
# -------------------------------------------

frase5 = 'You cannot end a sentence with because because because is a conjunction'
print(frase5.find('because'))

# -------------------------------------------
# Ejercicio 23: Última posición de 'because'
# -------------------------------------------

print(frase5.rindex('because'))

# -------------------------------------------
# Ejercicio 24: Cortar 'because because because'
# -------------------------------------------

inicio = frase5.find('because because because')
fin = inicio + len('because because because')
print(frase5[inicio:fin])

# -------------------------------------------
# Ejercicio 25: ¿Comienza con 'Coding'?
# -------------------------------------------

print(company.startswith('Coding'))

# -------------------------------------------
# Ejercicio 26: ¿Termina con 'coding'?
# -------------------------------------------

print(company.endswith('coding'))

# -------------------------------------------
# Ejercicio 27: Eliminar espacios en blanco
# -------------------------------------------

espacios = '   Coding For All      '
print(espacios.strip())

# -------------------------------------------
# Ejercicio 28: isidentifier
# -------------------------------------------

print('30DaysOfPython'.isidentifier())   # False
print('thirty_days_of_python'.isidentifier())  # True

# -------------------------------------------
# Ejercicio 29: Unir lista de librerías con #
# -------------------------------------------

librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(librerias))

# -------------------------------------------
# Ejercicio 30: Separar con nueva línea
# -------------------------------------------

print("I am enjoying this challenge.\nI just wonder what is next.")

# -------------------------------------------
# Ejercicio 31: Separar con tabulación
# -------------------------------------------

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# -------------------------------------------
# Ejercicio 32: Formateo área de un círculo
# -------------------------------------------

radio = 10
area = 3.14 * radio ** 2
print("The area of a circle with radius {} is {} meters square.".format(radio, int(area)))

# -------------------------------------------
# Ejercicio 33: Operaciones usando format
# -------------------------------------------

a = 8
b = 6

print("{} + {} = {}".format(a, b, a+b))
print("{} - {} = {}".format(a, b, a-b))
print("{} * {} = {}".format(a, b, a*b))
print("{} / {} = {:.2f}".format(a, b, a/b))
print("{} % {} = {}".format(a, b, a%b))
print("{} // {} = {}".format(a, b, a//b))
print("{} ** {} = {}".format(a, b, a**b))