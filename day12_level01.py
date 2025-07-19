# -------------------------------------------
# LEVEL 1
# -------------------------------------------

# Ejercicio 1: Generar un ID de usuario aleatorio de 6 caracteres
import random
import string

def random_user_id():
    caracteres = string.ascii_letters + string.digits
    id_generado = ''.join(random.choice(caracteres) for _ in range(6))
    return id_generado

# Ejemplo
print(random_user_id())

# Ejercicio 2: Generar varios IDs personalizados
def user_id_gen_by_user():
    cantidad_caracteres = int(input("Ingresa la cantidad de caracteres por ID: "))
    cantidad_ids = int(input("Ingresa cuántos IDs quieres generar: "))
    caracteres = string.ascii_letters + string.digits
    for _ in range(cantidad_ids):
        id_generado = ''.join(random.choice(caracteres) for _ in range(cantidad_caracteres))
        print(id_generado)

# Ejemplo
# user_id_gen_by_user()

# Ejercicio 3: Generar un color RGB aleatorio
def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return f"rgb({r},{g},{b})"

# Ejemplo
print(rgb_color_gen())