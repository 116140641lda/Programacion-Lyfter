from actions import StudentAdmin
from data import CsvAdmin


class Menu:
    def __init__(self,BASE_DIR,DOC,code,info_students):
        self.admin = StudentAdmin(BASE_DIR,DOC,code,info_students)
        self.csv = CsvAdmin(self.admin.total_info)

    def menu (self,code):
        
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
                self.admin.Info_estudiantes(code)
                
            elif option == '2' :
                self.admin.show_all_students()
                
                
            elif option == '3' :
                self.admin.show_3_top()
        

            elif option == '4' :
                result = self.admin.show_general_prom()
                # print(result)
            
            elif option == '5' :
                self.csv.export_csv()


            elif option == '6' :
                self.admin.total_info = self.csv.import_file()

            elif option == '7' :
                print("Muchas gracias")
                break
            else:
                print('elija una opcion correcta') 