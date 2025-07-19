# -------------------------------------------
# LEVEL 3
# -------------------------------------------

# Ejercicio 1: Mezclar elementos de una lista
def shuffle_list(lista):
    lista_copia = lista.copy()
    random.shuffle(lista_copia)
    return lista_copia

# Ejemplo
print(shuffle_list([1,2,3,4,5,6,7,8,9]))

# Ejercicio 2: Generar 7 números únicos aleatorios entre 0 y 9
def unique_random_numbers():
    return random.sample(range(10), 7)

# Ejemplo
print(unique_random_numbers())