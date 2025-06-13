#Día 4: 30 días de programación en Python

Datos="""
-------- EJERCICIOS DEL DIA NUMERO 4  --------
  Nombre: Damian Ezequiel Solis Rodriguez
  Fecha: 02/05/2025
  Materia: Progremacion Estructurada
  Unidad: U2
----------------------------------------------
"""

"""
agregar eso cuando no este aceptando tus archivos UTF-8

Escribir este comando en la terminal ya que si no esta usando UTF-8: chcp 65001

Agregar eso el archivo de python: # -- coding: utf-8 --

"""
#Exercises - Day 4

#concatenar la primera cadena 
Cadena1="TREINTA"+""+"DIAS"+""+"DE"+""+"PYTHON" 
print(f"Concatenar la primera cadena: {Cadena1}") #Resultado: Treinta Dias de Python

#Concatenar la segunda cadena
Cadena2="Coding"+""+"For"+""+"All"
print(f"Concatenar la segunda cadena: {Cadena2}") #Resultado: Codificacion para Todos

Company=Cadena2
#Ahora como se asigno el valor del Str a empresa
print(f"imprime la misma cadena 1 de la linea anterior pero almacenada en otra variable {Company} \n") #Resultado: Codificacion para Todos (Coding For All)

#ahora se imprimira lo que es la longitud de la 
#cadena "empresa"

print("La longitud de la cadena \"Empresa\" es de: ", len(Company) ,"Letras \n")
#Imprime la longitud de la cadena con el metodo len()

#Cambiar todos los elemntos a mayusculas 
print(f"Imprime Todo en Mayusculas: {Cadena2.upper()} \n")


#Cambiar todos los elemntos a minusculas
print(f"Imprime Todo en Minusccuas: {Cadena1.lower()} \n")

#------------------------------------------


# pone solo la primera letra en mayúscula de la cadena
print(f"ESTE ES EL METODO .CAPITALIZE: {Cadena2.capitalize()} \n")  # Resultado: "Codificación para todos"

# Pone la primera letra de cada palabra en mayúscula
print(f"ESTE ES EL METODO .TITLE: {Cadena2.title()} [pone las primeras letras en mayusculas] \n")       # Resultado: "Codificación Para Todos"


# Invierte las mayúsculas y minúsculas
print(f"ESTE ES EL METODO .SWAPCASE: {Cadena2.swapcase()} [pone las primeras letras en minusculas]\n")    # Resultado: "cODIFICACIÓN pARA tODOS"

# Metodo .slice() para recortar partes de String , list , tulpas 
"""
El slicing utiliza la notación [inicio:fin:paso], donde: 
inicio: El índice del primer elemento que se incluirá en la rebanada (por defecto es 0).
fin: El índice del primer elemento que NO se incluirá en la rebanada (por defecto es el final de la secuencia).
paso: El número de elementos que se saltarán entre cada elemento de la rebanada (por defecto es 1).

Example: 

cadena = "Hola, mundo!"
# Obtener los primeros 5 caracteres
CadenaNueva = cadena[0:5]  # o cadena[:5]
print(rebanada)  # Output: Hola,

# Obtener los caracteres desde el índice 7 hasta el final
CadenaNueva = cadena[7:]
print(rebanada)  # Output: mundo!

# Obtener cada segundo caracter de la cadena
CadenaNueva = cadena[::2]
print(rebanada)  # Output: Hla mndo!

# Obtener la cadena al revés
CadenaNueva = cadena[::-1]
print(rebanada)  # Output: !odnum ,aloH
"""
print(f"Utilizacion del metodo (.slice()) para imprimir solo la palabra 'Codificacion' de la cadena [Codificación para todos] = {Cadena2[0:12]}") 


#Metodo  CadenaIndex.index(Sub_cadenaIndez) = arroja el numero de la posicion del caracter(char)
CadenaIndex="Coding For All"
Sub_CadenaIndex="Coding"
four='Four'
print(f"la cadena [CadenaIndex] en que pocicion esta de la [Sub_CadenaIndex] arrojando un valor numerico entero: {CadenaIndex.index(Sub_CadenaIndex)} \n")
print("[CadenaIndex]=\"Coding For All\" [Sub_CadenaIndex]= \"Coding\" \n")

# el Try-except
"""
Es una estructura de control de errores. Se usa para evitar que tu 
programa se detenga cuando ocurre un error inesperado.

📌 ¿Por qué es útil?
Si usas un método como .index() que lanza un error si no encuentra algo, 
puedes "atrapar" ese error con try-except y mostrar un mensaje en lugar 
de que tu programa se caiga.

try: → Aquí pones el código que puede fallar.

Si ese código funciona, se ejecuta normalmente.

Si ocurre un error específico, como ValueError, 
entonces se ejecuta lo que esté dentro de except.

En este caso, si "Four" no está en "Coding For All", 
se lanza un ValueError.
"""
try:
    print(f"esto es una prueba para mostrar el error en la lectura buscando el str \"Four\" : {CadenaIndex.index(four)} \n")
    posicion = CadenaIndex.index(four)
    print(f"El índice de '{four}' en la cadena es: {posicion}")
except ValueError:
    print(f"La subcadena '{four}' no se encontro en la cadena.")


#Metodo CadenaFind.(Sub_cadena) = arroja como resultado la pocision de la comparativa de donde iniciara , Sub_cadena
"""
cadena = "Hola, mundo!"
posicion = cadena.find("mundo")
print(posicion)  # Imprimirá 6 (porque "mundo" comienza en la posición 6)

posicion_no_encontrada = cadena.find("Python")
print(posicion_no_encontrada)  # Imprimirá -1
"""
Cadenafind="Coding For All"
Sub_Cadenafind="Coding"
print(f"la cadena [CadenaFind] en que pocicion esta de la [Sub_CadenaFind] arrojando un valor numerico entero: {Sub_Cadenafind.find(Cadenafind)} \n")
print(f"esto es una prueba para mostrar el error en la lectura buscando el str \"Four\": {Cadenafind.find('Four')} \n")

#Metodo replace() se utiliza para remplazar la palabra de la cadena a la cual deseas ser modificada 
RemplazaCadenaIndex='coding'
Coding=RemplazaCadenaIndex
print(f"imprime coding en la nueva variable que se almacena en esta pero originaria de [RemplazaCadenaIndex]= {Coding}")
RemplazaCadenaPython="Python for Everyone"
print(f"Remplaza [Python for Everyone] por [Python for All] : {RemplazaCadenaPython.replace('Python for Everyone','Python for All')}\n")


#Metodo Split() este metodo se aplica para dividir una cadena 
print(f"Dividir una cadena [Coding For All] utilizando un espacio de separacion : {Cadenafind.split(' ')}\n")

#3 preguntas 
print(f"¿Cuál es el carácter en el índice 0 de la cadena 'coding for all'? = {Cadenafind[0]} \n")

print(f"¿Cuál es el último índice de la cadena 'coding for all'? = {len(Cadenafind) - 1} \n")

#Aun que me piden la pocicion o indice 10 utilizo el 9 ya que inicia desde 0 a contar
print(f"¿Qué carácter está en el índice 10 de la cadena 'coding for all'? = {Cadenafind[9]} \n")


#Crear un Acronimo para el nombre "Python For Everyone"
acronimo = "Python for Everyone"
"""
acronimo.split()
➜ Divide la frase en palabras: ["Python", "for", "Everyone"]

[palabra[0] for palabra in ...]
➜ Toma la primera letra de cada palabra: ["P", "f", "E"]

''.join(...)
➜ Une esas letras en una sola cadena: "PfE"

.upper()
➜ Convierte a mayúsculas: "PFE"
"""
print(f"El acrónimo para 'Python for Everyone' es: {' '.join([palabra[0] for palabra in acronimo.split()]).upper()} \n")

# metodo .rfinf() para ver la ultima aparicion de l caracter en el strg
print(f"determinar la pocicion de la primera aparicion de 'C' en la cadena 'Coding For All' : {Cadenafind.find('C')+1} \n") #Le sumo +1 ya que inicia el conteo desde 0

print(f"determinar la primera aparicion de 'F' en 'Coding For All' : {Cadenafind.find('F')} \n") #el metodo .find() es para ver la primera aparicion del caracter

ultima_aparicion="Coding For All People"
print(f"determinar la ultima aparicion de 'l' en 'Coding For All People': {ultima_aparicion.rfind('l')} \n") #el metodo rfind() es para ver la ultima aparicion del caracter

#Encontarr ya sea con el indice o empleando el metodo .find() para la palabra 'Because'
Because="No se puede terminar una oracion con \"because\" porque es una conjuncion"

print(f"\nImprimir la oracion sobre la cual se aplicara el metodo 'find' para localizar la palabra 'because':\n ESTO ES EL TEXTO== {Because}\n")
print("Aplicando el metodo 'find' para encontrar la primera aparicion de la palabra 'because':")

print(f"Emplear el metodo para encontar la primera apaicion de la palabra 'beause' e imprimir la pocicion inicial de dicha palabra correspondiente: {(Because.find('because'))}")
 
# Usar el metodo .rindex("porque") busca la última vez que aparece "porque" y devuelve su posición (índice) en la cadena.
Frase_rindex="No se puede terminar una oración con \"porque\", porque \"porque\" es una conjunción."
print(f"busca la última vez que aparece \"porque\" con el metodo [.rindex('porque')] = {Frase_rindex.rindex("porque")} numero de la pocision\n")


# Elimina la frace de los 'because' de You cannot end a sentence with because because because is a conjunction
CadenaEliminar="You cannot end a sentence with because because because is a conjunction"
"""
frase[inicio:fin] → esto recorta una porción específica del string, 
desde el índice inicio hasta justo antes del índice fin.

.strip() → se aplica después del slicing, y sirve únicamente para 
eliminar espacios en blanco (u otros caracteres opcionales) al inicio 
y final del texto recortado.

"""
inicioCadena=CadenaEliminar.find('because')
FinCadena=CadenaEliminar.find('is')
print(f" Recortar las palbras [because, because, because] de la oracion :  You cannot end a sentence with because because because is a conjunction \n --> Esta es la oracion eliminando la palabra 'Because' == {(CadenaEliminar[:inicioCadena] + CadenaEliminar[FinCadena:]).strip()} \n")

# Encontra la primera ocurrencia de la aparicion de la palabra Because
print(f"Encontrar la pocicion de la pimera apaicion de la palabra 'because' :{CadenaEliminar.find('because')}")

# Eliminar una frace de una oracion para esto es el metodo .replace()
print(f"Elimina la frase 'because because because' de la oración: \n Original: {CadenaEliminar}")
print(f"Modificada: {CadenaEliminar.replace('because because because','').strip()}\n")

# ¿'Coding For All' comienza con una subcadena Codificación?
print ("¿Empieza con 'Coding'? →", "Coding For All".startswith("Coding"))

# ¿'Coding For All' termina con una subcadena de codificación?
print("¿Termina con 'coding'? →", "Coding For All".endswith("coding"))

# Eliminar espacios finales: 'Codificación para todos'
cadena_con_espacios = '   Coding For All      '
print("Sin espacios al inicio y final:", cadena_con_espacios.strip())

# isidentifier() verificar si una cadena de texto es un identificador válido.
"""
print("nombre_variable".isidentifier())  # True
print("1variable".isidentifier())        # False (empieza con número)
print("variable-1".isidentifier())       # False (contiene un guion)
print("def".isidentifier())              # True (es válido, pero es palabra clave)
print("_oculto".isidentifier())          # True
"""
print("¿'30DaysOfPython' es un identificador válido?", "30DaysOfPython".isidentifier())
print("¿'thirty_days_of_python' es un identificador válido?", "thirty_days_of_python".isidentifier())


# .join() unir todos los elementos de una lista de cadenas (strings) 
# en una sola cadena, usando un separador que tú eliges
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("Unidas con '# ':", '# '.join(librerias))


# New line escape (\n) ==> Nueva línea de escape
print("I am enjoying this challenge.\nI just wonder what is next.")


# secuencia de escape de tabulación (\t)
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")


# Formato de cadena (área del círculo)
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))

"""
{} inserta el valor de radius tal cual.

{:.0f} inserta area como número decimal con 0 decimales (redondeado).

.format(radius, area) reemplaza esos marcadores con las variables.

Ejemplo si radius = 5 y area = 78.54, la salida será:


a)  la explicación resumida de .format():

.format() es un método de cadenas en Python que te permite 
insertar valores dentro de un texto, reemplazando los {} por los 
argumentos que pases.

Por ejemplo:

python
Copiar
Editar
"Hola, {}".format("Mundo")
produce:

Copiar
Editar
Hola, Mundo
"""

# Operaciones matemáticas con formato de cadena
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")