from menu import Menu

def main(BASE_DIR,DOC,code,info_students):
    print("Bienvenido al sistema de ingreso de estudiantes")
    app = Menu(BASE_DIR,DOC,code,info_students)
    app.menu(code)

if __name__ == "__main__":
    main(0,"","","")

