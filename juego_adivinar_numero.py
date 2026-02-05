# Enunciado: Crea el clásico juego pero con estas características:

# El programa elige un número aleatorio entre 1-100
# El usuario tiene máximo 7 intentos
# Después de cada intento, da pistas ("muy alto", "muy bajo")
# Al final, muestra estadísticas: intentos usados, si ganó/perdió

# Ayuda:
# Usa import random y random.randint(1, 100)
# Lleva contador de intentos con variable intentos = 0
# Usa while intentos < 7: para el bucle principal
# Considera crear funciones para: generar número, validar entrada, dar pistas

import random
def generar_numero_aleatorio():
        return random.randint(1, 100)

def validar_entrada(entrada):
    try:
        numero = int(entrada)
        if 1 <= numero <= 100:
            return numero
        else:
            print("Por favor, ingresa un número entre 1 y 100.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
        return None
    
def dar_pistas(numero_usuario, numero_secreto):
    if numero_usuario < numero_secreto:
        print("Muy bajo.")
    elif numero_usuario > numero_secreto:
        print("Muy alto.")
    else:
        print("¡Correcto! Has adivinado el número.")

def juego_adivinar_numero():
    numero_secreto = generar_numero_aleatorio()
    intentos = 0
    max_intentos = 7
    gano = False

    print("¡Bienvenido al juego de adivinar el número!")
    print("He elegido un número entre 1 y 100. Tienes 7 intentos para adivinarlo.")

    while intentos < max_intentos:
        entrada = input(f"Intento {intentos + 1}: Ingresa tu número: ")
        numero_usuario = validar_entrada(entrada)

        if numero_usuario is not None:
            intentos += 1
            if numero_usuario == numero_secreto:
                dar_pistas(numero_usuario, numero_secreto)
                gano = True
                break
            else:
                dar_pistas(numero_usuario, numero_secreto)

    if gano:
        print(f"¡Felicidades! Has ganado en {intentos} intentos.")
    else:
        print(f"Lo siento, has perdido. El número era {numero_secreto}. Has usado {intentos} intentos.")

juego_adivinar_numero()
