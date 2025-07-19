#Level 3

#Ejercicio: Persona y habilidades

persona = {
    'primer_nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'pais': 'Finlandia',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion': {
        'calle': 'Space street',
        'codigo_postal': '02210'
    }
}

# Verificar si tiene habilidades y mostrar la habilidad del medio
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    habilidad_media = habilidades[len(habilidades)//2]
    print("La habilidad del medio es:", habilidad_media)

# Verificar si sabe Python
if 'habilidades' in persona:
    sabe_python = 'Python' in persona['habilidades']
    print("¿Sabe Python?", sabe_python)

# Determinar el tipo de desarrollador
if set(['JavaScript', 'React']) == set(persona['habilidades']):
    print("Es desarrollador Front End.")
elif set(['Node', 'Python', 'MongoDB']).issubset(persona['habilidades']):
    print("Es desarrollador Back End.")
elif set(['React', 'Node', 'MongoDB']).issubset(persona['habilidades']):
    print("Es desarrollador Full Stack.")
else:
    print("Título desconocido.")

# Verificar estado civil y país
if persona['casado'] and persona['pais'] == 'Finlandia':
    print(f"{persona['primer_nombre']} {persona['apellido']} vive en {persona['pais']}. Está casado.")


