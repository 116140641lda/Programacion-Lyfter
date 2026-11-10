name = input("ingrese su nombre")
last_name = input("ingrese su apellido")
Age = int(input("ingrese su edad"))
if Age <= 2 :
    print (f"{name}{last_name} es un bebe")
elif Age > 2 and Age <= 10 :
    print(f"{name}{last_name} es un niño")
elif Age > 10 and Age <= 15 :
    print (f"{name}{last_name} es un preadolescente")
elif Age > 15 and Age <= 17 :
    print(f"{name}{last_name} es un adolescente")
elif Age > 17 and Age <= 25 :
    print(f"{name}{last_name} es un adulto joven")
elif Age > 25 and Age <= 65 :
    print(f"{name}{last_name} es un adulto")
elif Age > 65 :
    print (f"{name}{last_name} es un adulto mayor")