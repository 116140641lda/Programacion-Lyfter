



def sum(actual_number):
    try:
        var = int(input('Ingrese un numero para la operación\n'))
        actual_number+=var
        print(f'el resultado es: {actual_number}')
        return actual_number

    except ValueError:
        print ('esto no es un numero')


def calculator_minus (actual_number):
    try:
        var = int(input('Ingrese un numero para la operación\n'))
        actual_number = actual_number - var
        print(f'el resultado es: {actual_number}')
        return actual_number

    except ValueError:
        print ('esto no es un numero')


def calculator_mult (actual_number):
    try:
            
        var = int(input('Ingrese un numero para la operación\n'))
        actual_number = actual_number * var
        print(f'el resultado es: {actual_number}')
        return actual_number

    except ValueError:
        print ('esto no es un numero')

def calculator_div (actual_number):
    try:
            
        var = int(input('Ingrese un numero para la operación\n'))
        
        if var != 0 :
            actual_number = actual_number / var
            print(f'el resultado es: {actual_number}')
        return actual_number

    except ValueError:
        print ('esto no es un numero')

def menu ():

    actual_number = 10

    while True: 
            
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicacion')
        print('4. Division')
        print('5.Salir')
        
    
        option = input('\nElige una de las opciones\n >')


        if option == '5':
            break
        elif option == '1' :
            actual_number = sum (actual_number)
            if actual_number is not None:
                print (actual_number)
            
            
        elif option == '2' :
            actual_number = calculator_minus (actual_number)
            if actual_number is not None:
                print (actual_number)
            
        elif option == '3' :
            actual_number = calculator_mult (actual_number)
            if actual_number is not None:
                print (actual_number)
            
        elif option == '4' :
            actual_number = calculator_div (actual_number)
            if actual_number is not None:
                print (actual_number)
        else:
            print('elija una opcion correcta')   
            

menu()

