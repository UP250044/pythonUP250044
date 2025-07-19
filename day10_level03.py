#Level 3

#Ejercicio 1: Países que contienen 'land'
from data.countries import countries

paises_con_land = []

for pais in countries:
    if 'land' in pais:
        paises_con_land.append(pais)

print("Países que contienen 'land':", paises_con_land)

#Ejercicio 2: Revertir lista de frutas
frutas = ['banana', 'orange', 'mango', 'lemon']

frutas_reversa = []

for i in range(len(frutas)-1, -1, -1):
    frutas_reversa.append(frutas[i])

print("Lista al revés:", frutas_reversa)


#Ejercicio 3: Total de lenguajes únicos
from data.countries_data import countries_data

lenguajes = set()

for pais in countries_data:
    for idioma in pais['languages']:
        lenguajes.add(idioma)

print("Total de lenguajes únicos:", len(lenguajes))


#Ejercicio 4: 10 idiomas más hablados
from collections import Counter

contador_idiomas = Counter()

for pais in countries_data:
    for idioma in pais['languages']:
        contador_idiomas[idioma] += 1

top_10_idiomas = contador_idiomas.most_common(10)

print("Los 10 idiomas más hablados:")
for idioma, cantidad in top_10_idiomas:
    print(f"{idioma}: {cantidad} países")


#Ejercicio 5: 10 países más poblados
paises_ordenados = sorted(countries_data, key=lambda x: x['population'], reverse=True)

print("Los 10 países más poblados:")
for pais in paises_ordenados[:10]:
    print(f"{pais['name']}: {pais['population']} habitantes")
