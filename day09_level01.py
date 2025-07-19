#Ejercicio 1: Edad para manejar

mi_edad = 25  # Tu edad real o la que tú quieras

edad_usuario = int(input("Ingresa tu edad: "))

if edad_usuario >= 18:
    print("Eres lo suficientemente mayor para aprender a conducir.")
else:
    años_faltantes = 18 - edad_usuario
    print(f"Necesitas esperar {años_faltantes} años más para aprender a conducir.")

#Ejercicio 2: Comparar edades

mi_edad = 25  # Aquí pones tu edad real o ficticia

edad_usuario = int(input("Ingresa tu edad: "))

if edad_usuario > mi_edad:
    diferencia = edad_usuario - mi_edad
    if diferencia == 1:
        print("Eres 1 año mayor que yo.")
    else:
        print(f"Eres {diferencia} años mayor que yo.")
elif edad_usuario < mi_edad:
    diferencia = mi_edad - edad_usuario
    if diferencia == 1:
        print("Soy 1 año mayor que tú.")
    else:
        print(f"Soy {diferencia} años mayor que tú.")
else:
    print("Tenemos la misma edad.")


#Ejercicio 3: Comparar dos números

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")

