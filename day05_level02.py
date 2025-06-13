#Día 5: 30 días de programación en Python

Datos="""
-------- EJERCICIOS DEL DIA NUMERO 5  --------
  Nombre: Damian Ezequiel Solis Rodriguez
  Fecha: 13/06/2025
  Materia: Programacion Estructurada
  Unidad: U2
----------------------------------------------
"""
print(f"\n{Datos}\n")

# NIVEL 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f"Edades ordenadas: {ages}")
print(f"Edad mínima: {min(ages)}")
print(f"Edad máxima: {max(ages)}")

# Añadir min y max
ages.extend([min(ages), max(ages)])
print(f"Edades con min y max añadidos: {ages}")

# Mediana
import statistics
mediana = statistics.median(ages)
print(f"Mediana: {mediana}")

# Promedio
promedio = sum(ages) / len(ages)
print(f"Promedio: {promedio:.2f}")

# Rango
rango = max(ages) - min(ages)
print(f"Rango: {rango}")

# Comparar diferencias con promedio
print(f"|min - promedio| = {abs(min(ages)-promedio):.2f}")
print(f"|max - promedio| = {abs(max(ages)-promedio):.2f}")

# Países
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
medio = len(countries) // 2
print(f"País del medio: {countries[medio]}")

primera_mitad = countries[:medio + 1]
segunda_mitad = countries[medio + 1:]
print(f"Primera mitad: {primera_mitad}")
print(f"Segunda mitad: {segunda_mitad}")

# Desempaquetar países
china, russia, usa, *scandic = countries
print(f"China: {china}, Russia: {russia}, USA: {usa}, Scandic: {scandic}")
