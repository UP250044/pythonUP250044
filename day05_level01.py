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

# NIVEL 1

# 1. Declarar una lista vacía
Lista_Vacia = []
print(f"Imprimir la lista vacía = {Lista_Vacia}")

# 2. Declarar una lista con más de 5 elementos
Segunda_Lista = ['Damian', True, 1.86, 21, 2004, 'febrero', 'aprender nuevas cosas', ':)']
print(f"Lista: {Segunda_Lista}, longitud: {len(Segunda_Lista)}")

# 3. Obtener el primer, medio y último elemento
print(f"Primero: {Segunda_Lista[0]}")
print(f"Medio: {Segunda_Lista[len(Segunda_Lista)//2]}")
print(f"Último: {Segunda_Lista[-1]}")

# 4. mixed_data_types
tipos_de_datos_mixtos = ['Damian Ezequiel', 21, 1.86, 'soltero', 'paseos de santa monica , coto :paseos de san ambrosio #103 , int 28']
print(f"Lista mixed_data_types: {tipos_de_datos_mixtos}")
for i in range(len(tipos_de_datos_mixtos)):
    print(f"[{i}] = {tipos_de_datos_mixtos[i]}")

# 5. Lista de it_companies
empresas_modificada = ['Facebook', 'Samsung', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(f"Lista it_companies: {empresas_modificada}")

# 6. Número de empresas
print(f"Número de empresas: {len(empresas_modificada)}")

# 7. Imprimir primero, medio y último
print(f"Primero: {empresas_modificada[0]}")
print(f"Medio: {empresas_modificada[len(empresas_modificada)//2]}")
print(f"Último: {empresas_modificada[-1]}")

# 8. Modificar una empresa
empresas_modificada[1] = 'Samsung'  # Ya está en tu código
print(f"Lista modificada: {empresas_modificada}")

# 9. Agregar una empresa
empresas_modificada.append('Intel')
print(f"Agregar Intel: {empresas_modificada}")

# 10. Insertar en el medio
empresas_modificada.insert(len(empresas_modificada)//2, 'Spotify')
print(f"Insertar Spotify: {empresas_modificada}")

# 11. Convertir una empresa a mayúsculas (IBM excluida)
empresas_modificada[4] = empresas_modificada[4].upper()
print(f"Convertir a mayúsculas: {empresas_modificada}")

# 12. Unir empresas con '#; '
empresas_joined = '#; '.join(empresas_modificada)
print(f"Empresas unidas: {empresas_joined}")

# 13. Verificar si existe 'Google'
existe = 'Google' in empresas_modificada
print(f"'Google' existe: {existe}")

# 14. Ordenar la lista
empresas_modificada.sort()
print(f"Ordenada: {empresas_modificada}")

# 15. Invertir la lista
empresas_modificada.reverse()
print(f"Invertida: {empresas_modificada}")

# 16. Cortar las primeras 3
print(f"Primeras 3: {empresas_modificada[:3]}")

# 17. Cortar las últimas 3
print(f"Últimas 3: {empresas_modificada[-3:]}")

# 18. Cortar el/los del medio
long = len(empresas_modificada)
if long % 2 == 0:
    print(f"Empresas del medio: {empresas_modificada[long//2 -1: long//2 +1]}")
else:
    print(f"Empresa del medio: {empresas_modificada[long//2]}")

# 19. Eliminar primera, media y última
empresas_modificada.pop(0)  # primera
empresas_modificada.pop(len(empresas_modificada)//2)  # media
empresas_modificada.pop(-1)  # última
print(f"Después de eliminar: {empresas_modificada}")

# 20. Eliminar todas
empresas_modificada.clear()
print(f"Lista vacía: {empresas_modificada}")

# 21. Destruir la lista (solo si se hiciera con `del`)
# del empresas_modificada

# 22 y 23. Unir listas y modificar
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(f"Full stack: {full_stack}")

index_redux = full_stack.index('Redux')
full_stack[index_redux + 1:index_redux + 1] = ['Python', 'SQL']
print(f"Full stack final: {full_stack}")
