mi_lista = [1, "Hola", 3.14, True, [1, 2, 3]]

print(mi_lista[0])
print(mi_lista[1])
print(mi_lista[4])

mi_lista[1] = "Mundo"
print(mi_lista)

mi_lista.append("Nuevo elemento")
print(mi_lista)

mi_lista.remove(3.14)
print(mi_lista)

print(len(mi_lista))
