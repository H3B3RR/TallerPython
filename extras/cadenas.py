cadena1 = "Hola, mundo"
cadena2 = 'Python es genial'

cadena_concatenada = cadena1 + " " + cadena2
print(cadena_concatenada)

cadena_repetida = cadena1 * 3
print(cadena_repetida)

primer_caracter = cadena1[0]
print(primer_caracter)

subcadena = cadena1[1:5]
print(subcadena)

longitud = len(cadena1)
print(longitud)

mayusculas = cadena1.upper()
print(mayusculas)

minusculas = cadena2.lower()
print(minusculas)

cadena_reemplazada = cadena1.replace("Hola", "Adiós")
print(cadena_reemplazada)

lista_palabras = cadena2.split()
print(lista_palabras)

cadena_unida = " ".join(lista_palabras)
print(cadena_unida)

cadena_con_espacios = "   Hola, mundo   "
cadena_sin_espacios = cadena_con_espacios.strip()
print(cadena_sin_espacios)

contiene_python = "Python" in cadena2
print(contiene_python)

nombre = "Juan"
edad = 30
cadena_formateada = f"Me llamo {nombre} y tengo {edad} años"
print(cadena_formateada)
