# Enunciado: Crea un programa que permita al usuario gestionar una lista de compras. Debe poder:

# Agregar un artículo.
# Eliminar un artículo (por nombre).
# Ver la lista actual.
# Salir.
# Usa un bucle while para mostrar el menú hasta que elija salir.

# Ayuda:
# Inicia con una lista vacía: lista_compras = [].
# Usa un bucle while True y un menú con print().
# Para agregar: lista_compras.append(articulo).
# Para eliminar: usa if articulo in lista_compras: y luego lista_compras.remove(articulo).
# Para ver la lista: for item in lista_compras: print(item).

#----------------------------------------------------------

lista_compras = []

while True:
    print('\nElija del menú la accion que quiera realizar: ')
    print('1 - Agregar un articulo')
    print('2 - Eliminar un articulo')
    print('3 - Ver la lista actual')
    print('4 - Salir')
    

    opcion = input('Elige una opcion del 1 al 4: ')

    if opcion == '1':
        #convertir solo primer letra en mayuscula
        articulo = input('Agrega a la lista el producto que quieres comprar: ').capitalize()
        lista_compras.append(articulo)
        print(f'{articulo} ha sido agregado a la lista de compras')
    elif opcion == '2':
        articulo = input('Ingresa el nombre del articulo que quieres eliminar de la lista: ').capitalize()
        if articulo in lista_compras:
            lista_compras.remove(articulo)
            print(f'{articulo} ha sido eliminado de la lista de compras')
        else:
            print(f'{articulo} no se encuentra en la lista de compras')  
    elif opcion == '3':
        print("Lista de Compras Actual:")
        if not lista_compras:
                print("La lista está vacía.")
        else:
            for articulo in lista_compras:
                print(articulo)          
    elif opcion == '4':
        print('has salido de la aplicacion de compras')
        break
    else:
        print('entrada no valida, ingrese una de las opciones recomendadas')

