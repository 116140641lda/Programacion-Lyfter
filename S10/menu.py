import actions
import data



def menu (total_info):
    total_info = []
    while True:
        print('1. Ingresar nuevo estudiante')
        print('2. Ver estudiantes')
        print("3. Ver mejores 3 promedios")
        print("4. Ver promedio Total de Notas")
        print("5. Exportar Datos")
        print("6. Importar datos")

        print('7.Salir')

        option = input('\nElige una de las opciones\n >')

        if option == '1' :
            actions.Info_estudiantes(total_info)
            
        elif option == '2' :
            actions.show_students(total_info)
            
            
        elif option == '3' :
            actions.show_3_top(total_info)
    

        elif option == '4' :
            result = actions.show_general_prom(total_info)
            print(result)
        
        elif option == '5' :
            data.export_csv(total_info)


        elif option == '6' :
            data.import_file()

        elif option == '7' :
            print("Muchas gracias")
            break
        else:
            print('elija una opcion correcta') 