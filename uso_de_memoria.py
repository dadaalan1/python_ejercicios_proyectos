# crear script que controle el uso de la memoria ram en español
# El script debe mostrar el uso actual de la memoria ram, el porcentaje de uso y el 
# total de memoria disponible. Además, debe permitir al usuario establecer 
# un límite de uso de memoria y mostrar una alerta si se supera ese límite.


import psutil

def mostrar_uso_memoria():
    memoria = psutil.virtual_memory()
    uso_actual = memoria.used / (1024 ** 3)  # Convertir a GB
    porcentaje_uso = memoria.percent
    total_memoria = memoria.total / (1024 ** 3)  # Convertir a GB
    print()
    print(f"Uso actual de memoria RAM: {uso_actual:.2f} GB")
    print(f"Porcentaje de uso: {porcentaje_uso: .2f}%")
    print(f"Total de memoria disponible: {total_memoria:.2f} GB")
    print()
# def establecer_limite_memoria():
#     limite = float(input("Ingrese el límite de uso de memoria en GB: "))
#     return limite

def verificar_limite_memoria(limite):
    memoria = psutil.virtual_memory()
    uso_actual = memoria.used / (1024 ** 3)  # Convertir a GB

    if uso_actual > limite:
        print("¡Alerta! Se ha superado el límite de uso de memoria.")
    else:
        print("El uso de memoria está dentro del límite establecido.")

if __name__ == "__main__":
    mostrar_uso_memoria()
    # limite = establecer_limite_memoria()
    # verificar_limite_memoria(limite)



#-----------------------------------------
