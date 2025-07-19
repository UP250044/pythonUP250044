# Ejercicio 1: Sistema de calificaciones

calificacion = int(input("Ingresa tu puntuación: "))

if calificacion >= 80 and calificacion <= 100:
    print("A")
elif calificacion >= 70 and calificacion <= 79:
    print("B")
elif calificacion >= 60 and calificacion <= 69:
    print("C")
elif calificacion >= 50 and calificacion <= 59:
    print("D")
elif calificacion >= 0 and calificacion <= 49:
    print("F")
else:
    print("Puntuación inválida.")


#Ejercicio 2: Determinar estación del año
mes = input("Ingresa un mes: ").lower()

if mes in ['septiembre', 'octubre', 'noviembre']:
    print("Es otoño.")
elif mes in ['diciembre', 'enero', 'febrero']:
    print("Es invierno.")
elif mes in ['marzo', 'abril', 'mayo']:
    print("Es primavera.")
elif mes in ['junio', 'julio', 'agosto']:
    print("Es verano.")
else:
    print("Mes inválido.")



# Ejercicio 3: Agregar fruta a la lista
frutas = ['banana', 'naranja', 'mango', 'limón']

nueva_fruta = input("Ingresa el nombre de una fruta: ").lower()

if nueva_fruta in frutas:
    print("Esa fruta ya existe en la lista.")
else:
    frutas.append(nueva_fruta)
    print("Fruta añadida. La lista actualizada es:", frutas)
