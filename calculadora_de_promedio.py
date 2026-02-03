# Enunciado: Pide al usuario que ingrese una serie de números (puede ser cualquier cantidad)
# y calcula su promedio. El usuario debe indicar cuándo terminar de ingresar números
# (por ejemplo, escribiendo "fin").

# Ayuda:
# Usa un bucle while para pedir números continuamente.
# Acumula la suma en una variable y cuenta cuántos números ingresó.
# Si el usuario escribe "fin", sale del bucle.
# Calcula el promedio como suma / cantidad (evita división por cero).


def calcular_promedio():
    lista = []
    while True:
        num_ingresado = input('ingresa un numero: ')
        lista.append(num_ingresado)
        if num_ingresado == 'fin':
            lista.pop()
            break     
    print(f'los numeros ingresados son: {lista}')
    suma = 0
    for i in lista:
        suma += float(i)  
    promedio = suma / len(lista)
    print(f'suma total: {suma}')
    print(f'la cantidad de numeros ingresados es {len(lista)}')
    print(f'el promedio es: {suma} dividido {len(lista)} cuyo resultado es {promedio}')
    
calcular_promedio()        