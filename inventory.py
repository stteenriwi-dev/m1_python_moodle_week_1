
name = input('Nombre del producto: ')
desicion = 0
price = 0
quantity = 0
products = {
            'name': '',
            'price': '',
            'quantity': '',
            'total': ''
            }
while True:
        if(name == ""):
            print(f'Porfavor diligencie un nombre para el producto')
            name = input('Nombre del producto: ')

        if(price == 0 and quantity == 0):
            price = float(input('Precio del producto: '))
            quantity = int(input('Cantidad en stock del producto: '))
            
            if(price <= 0):
                print(f'Debe diligenciar un precio mayor a: 0')
                price = float(input('Precio del producto: '))   

            if(quantity <= 0):
                print(f'Debe diligenciar una cantidad mayor a: 0') 
                quantity = float(input('Cantidad del producto: '))  

        else:
            cost_total = price * quantity
            print(f'Nombre del producto: {name} | Precio: {price} | Cantidad: {quantity}')
            print(f'El total a pagar es: {cost_total}')
            print('')
            update = input('¿Desea actualizar el producto? S/N: ').lower()
                
            if(name != "" and update == "s"):
                name = input('Nombre del producto: ')
                price = float(input('Precio del producto: '))
                quantity = int(input('Cantidad en stock del producto: '))
                if(price <= 0):
                    print(f'Debe diligenciar un precio mayor a: 0')
                    price = float(input('Precio del producto: '))   

                if(quantity <= 0):
                    print(f'Debe diligenciar una cantidad mayor a: 0') 
                    quantity = float(input('Cantidad del producto: '))  
            else:
                print('')
                print('')
                print('*** BIENVENIDO AL MENU DE INGRESO DE INVENTARIO ***')
                print('')
                print('1. Ver Productos')
                print('2. Agregar Producto')
                print('3. Salir')
                print(' ')
                desicion = int(input('¿Que desea hacer?: '))

                if(desicion == 1):
                    print(f'Nombre del producto: {name} | Precio: {price} | Cantidad: {quantity}')
                    print(f'El total a pagar es: {cost_total}')
                    print('')
                    print('')
                    print('')
                    print('*** BIENVENIDO AL MENU DE INGRESO DE INVENTARIO ***')
                    print('¿Que deseas hacer?')
                    print('')
                    print('1. Ver Productos')
                    print('2. Agregar Producto')
                    print('3. Salir')
                    print(' ')
                    desicion = int(input('¿Que desea hacer?: '))

                elif(desicion == 2):
                    name = ""
                    price = 0
                    quantity = 0

                elif(desicion == 3):
                    break

                else:
                    print('')
                    print('!!! VALOR NO VALIDO INGRESE UN NUMERO VALIDO !!!')
                    print('')
                    print('')
                    print('')
                    print('*** BIENVENIDO AL MENU DE INGRESO DE INVENTARIO ***')
                    print('¿Que deseas hacer?')
                    print('')
                    print('1. Ver Productos')
                    print('2. Agregar Producto')
                    print('3. Salir')
                    print('')
                    desicion = int(input('¿Que desea hacer?: '))
