import menu


def add_list (total_info, info_students):
    total_info.append(info_students)
    return total_info

def valid_note(note):
    while True:
        try:
            if 0 < int(note) <= 100:
                return True
            return False
        except ValueError:
            print('ingrese un numero válido')
            
            
def valid_code (code,total_info):
    while True:
        if len(str(code)) <= 4 and all(est["code"] != code for est in total_info):
            return True
        return False

def calc_prom (spanish, english, social, science):
    prom = spanish + english + social + science
    return prom / 4

def show_students(total_info):

        if not total_info:
            print("No hay estudiantes ingresados")
            return

        for i, est in enumerate(total_info, 1):
            print(f"\nEstudiante #{i}")
            for k, v in est.items():
                print(f"{k.capitalize()}: {v}")
        
            
def show_3_top (total_info):
        if len(total_info) < 1:
            print("No hay estudiantes suficientes para mostrar el top 3.")
            return
        top = sorted(total_info, key=lambda x: x["prom_total"], reverse=True)[:3]
        print("\n--- TOP 3 ESTUDIANTES ---")
        for i, est in enumerate(top,1):
            print(f"{i}. {est['name']} - prom: {est['prom_total']:.2f}")


def show_general_prom (total_info):

        if not total_info:
            print("No hay estudiantes para calcular el promedio general.")
            return
        total = sum(i ['prom_total'] for i in total_info)
        prom = total / len(total_info)
        print(f"Promedio general de todos los estudiantes: {prom:.2f}")




def Info_estudiantes (total_info):
        # total_info = []
    while True:
        try:
            quantity = int(input("Ingrese la cantidad de estudiantes\n"))
            print(quantity)
            for i in range (quantity):
                print(f"\nIngrese el estudiante # {i+1}")
                while True:
                    try:
                        code = int(input('Ingrese el código de 4 dígitos del estudiante\n'))
                        if not valid_code(code,total_info):
                            print("El código debe ser de 4 dígitos o menos o ya se encuentra en la lista")
                        else:
                            break  
                    except ValueError:
                        print("Debe ingresar un número válido.")

                name = input("Ingrese el nombre del estudiante\n")
                section = input("Ingrese su seccion\n")
                    

                while True:
                    try:
                        
                        spanish = int(input ("Ingrese su nota de español\n"))
                        while valid_note(spanish) == False :
                                spanish = int(input('Ingrese una nota correcta, entre 0 y 100\n'))

                        english = int(input("Ingrese su nota de inglés\n"))
                        while valid_note(english) == False :
                                english = int(input('Ingrese una nota correcta, entre 0 y 100\n'))
                            

                        social = int(input("Ingrese su nota de Sociales\n"))
                        while valid_note(social) == False :
                            social = int(input('Ingrese una nota correcta, entre 0 y 100\n'))
                            
                        science = int(input("Ingrese su nota de Ciencias\n"))
                        while valid_note(science) == False :
                            science = int(input('Ingrese una nota correcta, entre 0 y 100\n'))
                        
                        prom_total = int(calc_prom(spanish, english, social, science))

                        info_students = {
                                "code": code,
                                "name": name,
                                "section": section,
                                "spanish": spanish,
                                "english": english,
                                "social": social,
                                "science": science,
                                "prom_total": prom_total

                        }
                        total_info = add_list(total_info,info_students)
                        break
                    except ValueError:
                        print("Ingrese una nota válida")
                        print("Ingrese nuevamente las notas")
            return total_info
        except ValueError:
            print("La información ingresada es incorrecta")
                    

                    