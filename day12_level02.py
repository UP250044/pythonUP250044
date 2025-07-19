# -------------------------------------------
# LEVEL 2
# -------------------------------------------

# Ejercicio 1: Generar lista de colores hexadecimales
def list_of_hexa_colors(cantidad):
    colores = []
    for _ in range(cantidad):
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        colores.append(color)
    return colores

# Ejercicio 2: Generar lista de colores RGB
def list_of_rgb_colors(cantidad):
    colores = []
    for _ in range(cantidad):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        colores.append(f"rgb({r},{g},{b})")
    return colores

# Ejercicio 3: Generar colores hexa o rgb según lo que el usuario pida
def generate_colors(tipo, cantidad):
    if tipo == 'hexa':
        return list_of_hexa_colors(cantidad)
    elif tipo == 'rgb':
        return list_of_rgb_colors(cantidad)
    else:
        return "Tipo inválido. Usa 'hexa' o 'rgb'."

# Ejemplo
print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))