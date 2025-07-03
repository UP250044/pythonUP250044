# 1. Crear un diccionario vacío llamado dog
dog = {}

# 2. Agregar name, color, breed, legs, age al diccionario dog
dog['name'] = 'Max'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

# 3. Crear un diccionario student con varias claves
student = {
    'first_name': 'Damian',
    'last_name': 'Solis',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'HTML'],
    'country': 'Mexico',
    'city': 'CDMX',
    'address': 'Calle Falsa 123'
}

# 4. Obtener la longitud del diccionario student
print("Longitud del diccionario student:", len(student))

# 5. Obtener el valor de 'skills' y verificar el tipo de dato
skills_value = student['skills']
print("Skills:", skills_value)
print("Tipo de dato de 'skills':", type(skills_value))

# 6. Modificar los valores de 'skills' agregando uno o dos más
student['skills'].append('CSS')
student['skills'].append('JavaScript')
print("Skills actualizados:", student['skills'])

# 7. Obtener las claves del diccionario como lista
keys = list(student.keys())
print("Claves del diccionario student:", keys)

# 8. Obtener los valores del diccionario como lista
values = list(student.values())
print("Valores del diccionario student:", values)

# 9. Convertir el diccionario a una lista de tuplas usando items()
student_items = list(student.items())
print("Diccionario como lista de tuplas:", student_items)

# 10. Eliminar uno de los ítems del diccionario
del student['marital_status']
print("Diccionario student después de eliminar 'marital_status':", student)

# 11. Eliminar uno de los diccionarios (el de dog)
del dog
# print(dog)  # Esto causará error si se descomenta, porque ya no existe

