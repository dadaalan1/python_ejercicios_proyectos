# Enunciado: Pide al usuario que ingrese una frase y cuenta cuántas vocales 
# (a, e, i, o, u) hay en total, sin diferenciar mayúsculas/minúsculas.

# Ayuda:
# Convierte la frase a minúsculas con .lower().
# Recorre cada carácter de la cadena con un bucle for.
# Usa una variable acumuladora para contar.
# Puedes verificar si un carácter está en una cadena de vocales: if char in "aeiou".

input_frase = input('Ingresa una frase: ')
frase_minuscula = input_frase.lower()

# omitir el acento
frase_minuscula = frase_minuscula.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
vocales = ['a', 'e', 'i', 'o', 'u']

contador_vocales = 0

for vocal in frase_minuscula:
    if vocal in vocales:
        contador_vocales += 1

print(f"La cantidad total de vocales es: {contador_vocales}")
# otra solución:
# input_frase = input('Ingresa una frase: ')
# frase_minuscula = input_frase.lower() 
# contador_vocales = 0
# for char in frase_minuscula:
#     if char in "aeiou":
#         contador_vocales += 1
# print(f"La cantidad total de vocales es: {contador_vocales}")

