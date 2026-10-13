import menu

class Student:
        def __init__(self,code,name,section,spanish,english,social,science):
            self.code = code
            self.name = name
            self.section = section
            self.spanish = spanish
            self.english = english
            self.social = social
            self.science = science
            self.prom_total = (self.spanish + self.english + self.social + self.science) / 4
        

        # def create_student ():
        #     new_student = Student("code","name","section","spanish","english","social","science", "prom_total")
        #     print(f"Se ha creado un estudiante nuevo con la siguiente informacion : {code},{name},{section},{spanish},{english},{social},{science},{prom_total}")
        
        def show_info(self):
            print(f"Código: {self.code}")
            print(f"Nombre: {self.name}")
            print(f"Sección: {self.section}")
            print(f"Español: {self.spanish}")
            print(f"Inglés: {self.english}")
            print(f"Sociales: {self.social}")
            print(f"Ciencias: {self.science}")
            print(f"Promedio: {self.prom_total:.2f}")


class StudentAdmin:
    def __init__(self,BASE_DIR,DOC,code,info_students):
        self.total_info = []
        self.BASE_DIR = BASE_DIR
        self.DOC = DOC
        self.code = code
        self.info_students = info_students



    def add_list (self,info_students):
        self.total_info.append(info_students)

    def Info_estudiantes (self,code):
        # total_info = []
        try:
            quantity = int(input("Ingrese la cantidad de estudiantes\n"))
            print(quantity)
        except ValueError:
            print("información inválida")

        for i in range (quantity):

            print(f"\nIngrese el estudiante # {i+1}")

            while True:
                try:
                    code = int(input('Ingrese el código de 4 dígitos del estudiante\n'))
                    if not self.valid_code(code):
                        print("El código debe ser de 4 dígitos o menos o ya se encuentra ingresado.")
                    else:
                        break  
                except ValueError:
                    print("Debe ingresar un número válido.")
                


            name = input("Nombre:\n")


            section = input("Seccion:\n")

            spanish = self.valid_note("Español")

            english = self.valid_note("Inglés")

            social = self.valid_note("Sociales")
                
            science = self.valid_note("Ciencias")
            
            self.info_students = Student(code,name,section,spanish,english,social,science)
            
            self.add_list(self.info_students)
            
            print(f"\n El estudiante {name} ha sido agregado correctamente")


    def valid_note(self,subject):
        while True:
            try:
                note = int(input(f"Ingrese la nota de {subject}: "))
                if 0 < note <= 100:
                        return note
                else:
                    print("La nota debe estar entre 1 y 100.")
            except ValueError:
                    print("Ingrese un número válido.")
                
    def show_all_students(self):

        if not self.total_info:
            print("No hay estudiantes registrados.")
            return

        for i, info_students in enumerate(self.total_info, 1):
            print(f"\nEstudiante #{i}")
            info_students.show_info()

    def show_3_top (self):
        if len(self.total_info) < 1:
            print("No hay estudiantes suficientes para mostrar el top 3.")
            return
        top = sorted(self.total_info, key=lambda x: ["prom_total"], reverse=True)[:3]
        print("\n--- TOP 3 ESTUDIANTES ---")
        for i, info_students in enumerate(top,1):
            print(f"{i}. {info_students.name} - promedio: {info_students.prom_total:.2f}")


    def valid_code (self,code):
        while True:
            if len(str(code)) > 4:
                return False
        
            for student in self.total_info:
                if student.code == code:
                    return False
            return True
                
    def show_general_prom (self):

        if not self.total_info:
            print("No hay estudiantes para calcular el promedio general.")
            return
        total = sum(info_students.prom_total for info_students in self.total_info)
        prom = total / len(self.total_info)
        print(f"Promedio general de todos los estudiantes: {prom:.2f}")


        
            








                
                
           
        

        
            # add_list(total_info,info_students)
            # print(info_students)
            # print (total_info)
      

            