"""
Registrar productos con su nombre, precio y cantidad en un programa simple.
Calcular operaciones básicas como total de unidades y costo aproximado.
Aplicar fundamentos de programación: entrada de datos, variables, operaciones matemáticas y salidas en consola.
"""
# Declaro una variable para almacenar los productos nuevos
products = []
# Se crea un bucle para mostrar el menú y manejar las opciones del usuario
while True:
    # Mostrar el menú de opciones
        print('')
        print('*** BIENVENIDO AL MENU DE INGRESO DE INVENTARIO ***')
        print('')
        print('1. Ver Productos')
        print('---------------------------')
        print('2. Agregar Producto')
        print('---------------------------')
        print('9. Salir')
        print('---------------------------')
        print('¿Cuál es su opción?: ')
        # Solicitar la opción del usuario y la almacenamos en la variable (desicion)
        desicion = input('Use solamente números: ')
        # Inicio de manejo de excepciones
        try:
            # Si la opción es 1 y products tiene una longitud mayor a 0, mostramos los productos
            if(desicion == '1' and len(products) > 0):
                print('')    
                print('*** LISTA DE PRODUCTOS ***')
                print('')
                print('---------------------------')
                print('*** PRODUCTOS EN INVENTARIO ***')
                print('---------------------------')
                # Recorremos la lista de productos y mostramos su información
                for product in products:
                    # Mostrar la información de cada producto
                    print(f"Nombre del producto: {product['name']}")
                    print(f"Precio del producto: {product['price']}")
                    print(f"Cantidad del producto: {product['quantity']}")
                    print(f"Costo total aproximado del inventario: {product['total']}")
                    print('---------------------------')
                # En caso de que la opcion es 1 pero no haya productos en la lista, lanzamos una excepción IndexError
            elif(desicion == '1'):
                # Lanzamos una excepción IndexError si no hay productos
                raise IndexError
            # Si la opción es 2, solicitamos los datos del nuevo producto
            elif(desicion == '2'):
                print('')
                print('*** AGREGAR PRODUCTO ***')
                print('---------------------------')
                # Solicitar el nombre del producto
                name = input('Ingrese el nombre del producto: ')
                # Solicitar el prcio del producto
                price = float(input('Ingrese el precio del producto: '))
                # Solicitar la cantidad del producto
                quantity = int(input('Ingrese la cantidad del producto: '))
                # Inicializamos un ciclo while para validar que el precio sea mayor a 0
                while price <= 0:
                    print('---------------------------')
                    print('El precio debe ser un número positivo y mayor a 0.')
                    print('---------------------------')
                    # Almacenamos el nuevo valor del precio
                    price += float(input('Ingrese el precio del producto: '))
                    # Validamos si el precio y la cantidad son mayores a 0 para salir del ciclo
                    if(price > 0 and quantity > 0):
                        # En caso de que la cantidad sea válida, mostramos un mensaje de confirmación
                        print('Precio aceptada.')
                        # Cerramos el subciclo
                        break
                # Inicializamos un ciclo while para validar que la cantidad sea mayor a 0
                while quantity <= 0:     
                    print('---------------------------')
                    print('La cantidad debe ser un número positivo y mayor a 0.')
                    print('---------------------------')
                    # Almacenamos el nuevo valor de la cantidad
                    quantity += int(input('Ingrese la cantidad del producto: '))
                    # Validamos si el precio y la cantidad son mayores a 0 para salir del ciclo
                    if(price > 0 and quantity > 0):
                        # En caso de que la cantidad sea válida, mostramos un mensaje de confirmación
                        print('Cantidad aceptada.')
                        # Cerramos el subciclo
                        break
                # Validamos si el precio y la cantidad son mayores a 0 para agregar el producto a la lista
                if(price > 0 and quantity > 0):
                    # Creamos un diccionario para almacenar la información del producto
                    product = {
                        'name': name,
                        'price': price,
                        'quantity': quantity,
                        'total': price * quantity
                    }
                    # Agregamos el producto a la lista de productos
                    products.append(product)
                    # Imprimimos un mensaje de confirmación
                    print('---------------------------')
                    print(f'Producto {name} agregado exitosamente al inventario.')
                    print('---------------------------')
            # Si la opción es 9, salimos del programa
            elif(desicion == '9'):
                # Imprimimos un mensaje de despedida
                print('')
                print('Saliendo del programa. ¡Hasta luego!')
                print('')
                # Salimos del bucle principal
                break
            # Si la opcion no cumple con ninguna de las anteriores, mostramos un mensaje de error
            else:
                # Mensaje de error para opción inválida
                print('')
                print('Lo sentimos esa opción no es válida. Intente de nuevo.')
                print('')
                # Devolvemos al usuario al inicio del ciclo donde se encuentra el menú
                continue
        # Manejo de excepción IndexError para cuando no hay productos en la lista
        except IndexError:
            # Mensaje de error para cuando no hay productos en el inventario
            print('')
            print('No hay productos en el inventario.')
            print('')
            # Devolvemos al usuario al inicio del ciclo donde se encuentra el menú
            continue
