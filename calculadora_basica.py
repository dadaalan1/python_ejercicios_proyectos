#  Crea un programa que pida al usuario dos números y luego permita elegir 
#  entre sumar, restar, multiplicar o dividir. Muestra el resultado de la 
#  operación seleccionada.

def main():
    # Pedir al usuario dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Mostrar opciones de operaciones
    print("Seleccione la operación que desea realizar:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    # Pedir al usuario que elija una operación
    opcion = input("Ingrese el número de la operación (1/2/3/4): ")

    # Realizar la operación seleccionada y mostrar el resultado
    if opcion == '1':
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == '2':
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == '3':
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()

