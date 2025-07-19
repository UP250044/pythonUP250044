
# Exercises: Level 1

"""
Obtener la longitud de it_companies

Agregar 'Twitter'

Agregar múltiples empresas a la vez

Eliminar una empresa

¿Diferencia entre remove() y discard()?
"""
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

Longitud=len(it_companies)

agregar=it_companies.add('Twitter')

# Agregar varias empresas a la vez
it_companies.update(['Twitter', 'Netflix', 'Tesla'])

print(f"Se agrego multiples empresas ala vez: {it_companies} \n")

# Eliminar una empresa específica
Elimina_empresa=it_companies.remove('Apple')
print(f"se elimino 'Apple' de la lista: {Elimina_empresa} \n")

# remove() elimina un elemento, pero lanza error si no existe.
Remove=it_companies.remove('Microsoft')

# discard() elimina un elemento, pero no lanza error si no existe.
Discard=it_companies.discard('Oracle')

##########################################################################