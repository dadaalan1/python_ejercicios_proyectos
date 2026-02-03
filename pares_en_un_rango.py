# Enunciado: Pide al usuario dos números enteros (inicio y fin) y muestra 
# todos los números pares entre ellos (incluyendo los extremos si son pares).

# Ayuda:
# Usa range() para generar la secuencia de números entre inicio y fin+1.
# Dentro del bucle, verifica si el número es par (if num % 2 == 0).
# Imprime cada número par encontrado.

# Solicitar al usuario los números de inicio y fin
inicio = int(input("Introduce el número de inicio: "))
fin = int(input("Introduce el número de fin: "))
print(f"Números pares entre {inicio} y {fin}:")

# Recorrer el rango de números desde inicio hasta fin (inclusive)
for num in range(inicio, fin + 1):
    # Verificar si el número es par
    if num % 2 == 0:
        # Imprimir el número par
        print(num)  


