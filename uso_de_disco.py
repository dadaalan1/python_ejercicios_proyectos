#automatizar el uso de disco de datos
import shutil 

def uso_de_disco():
    disk_usage = shutil.disk_usage('/')
    #espacio total, espacio usado, espacio libre y porcentaje de uso
    print()
    print('Uso de disco de datos:')
    print(f"Espacio total: {disk_usage.total / (1024 ** 3):.2f} GB")    
    print(f"Espacio usado: {disk_usage.used / (1024 ** 3):.2f} GB")
    print(f"Espacio libre: {disk_usage.free / (1024 ** 3):.2f} GB")
    #imprimir porcentaje de uso
    porcentaje_uso = (disk_usage.used / disk_usage.total) * 100
    print(f"Porcentaje de uso: {porcentaje_uso:.2f}%")
    #imprimir salto de linea
    print() 
    
if __name__ == "__main__":    
    uso_de_disco()

#automatizar el uso de la unidad c: 
import shutil
def uso_de_disco_c():
    disk_usage = shutil.disk_usage('C:/')
    #espacio total, espacio usado, espacio libre y porcentaje de uso
    print('Uso de disco de la unidad C:')
    print(f"Espacio total: {disk_usage.total / (1024 ** 3):.2f} GB")    
    print(f"Espacio usado: {disk_usage.used / (1024 ** 3):.2f} GB")
    print(f"Espacio libre: {disk_usage.free / (1024 ** 3):.2f} GB")
    #imprimir porcentaje de uso
    porcentaje_uso = (disk_usage.used / disk_usage.total) * 100
    print(f"Porcentaje de uso: {porcentaje_uso:.2f}%")
    #imprimir salto de linea
    print() 
    
if __name__ == "__main__":    
    uso_de_disco_c()
