
import random

def tirar_dados():  
    dado1 = int(random.random()*10)%6 + 1
    dado2 = int(random.random()*10)%6 + 1

    print(f'El número del primer dado es: {dado1}')
    print(f'El número del segundo dado es: {dado2}')

    suma = dado1 + dado2
    print(f'La suma de los números de los dos dados de {nombre} es: {suma}')

def consulta():
    return input('¿Desea volver a tirar los dados? (s/n): ')


while True:
    nombre = input('Ingresa tu nombre: ')
    tirar_dados()
    
    while True:
        #se guarda la respuesta en una variable para no llamar varias veces a la función
        respuesta = consulta().lower()# Convierte la respuesta a minúsculas
        if respuesta == 'n':
            print('Gracias por jugar. ¡Hasta luego!')
            exit() # Sale del programa
        elif respuesta == 's':
            break  # Rompe el bucle interno para volver a tirar dados
        else:
            print('Entrada no válida. Por favor, ingrese "s" o "n".')
            # Continúa en el bucle interno hasta obtener respuesta válida