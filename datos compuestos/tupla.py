mi_tupla = (1, 2, 3, 4, 5)
print("Tupla original:", mi_tupla)

print("Primer elemento:", mi_tupla[0])
print("Último elemento:", mi_tupla[-1])

try:
    mi_tupla[0] = 10
except TypeError as e:
    print("Error al intentar modificar la tupla:", e)

mi_lista = list(mi_tupla)
mi_lista[0] = 10
print("Lista modificada:", mi_lista)

mi_tupla_modificada = tuple(mi_lista)
print("Tupla modificada:", mi_tupla_modificada)

otra_tupla = (6, 7, 8)
tupla_concatenada = mi_tupla + otra_tupla
print("Tupla concatenada:", tupla_concatenada)

a, b, c, d, e = mi_tupla
print("Desempaquetado:", a, b, c, d, e)
tupla_varios_tipos = ("Hola", 42, 3.14, True)
print("Tupla con diferentes tipos de datos:", tupla_varios_tipos)

print("String:", tupla_varios_tipos[0])
print("Integer:", tupla_varios_tipos[1])
print("Float:", tupla_varios_tipos[2])
print("Boolean:", tupla_varios_tipos[3])