




print ("hello" + "world")
number = (1+1+1)
print (f"hello + {number}")
print (f"{number} + hello world")
my_list = [1,2,3,4,5,6,7,8,9,10]
Unpair_list =  [3,5,7,9]
print (my_list + Unpair_list)
print (f"esta es la lista  {my_list}")
number_1 = float (number // 5)
number_2 = (3*3)
print ( zip,{number_1},{number_2})
verdadero = True
falso = False
resultado = 2<1
if resultado:
    print("la condicion es verdadera")
else:
    print("la condicion es falsa")

print (bool(0),bool(10))

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


import random
var_number = random.randint (1,10)
while True :
    secret_number = int(input ("Ingrese un numero del 1 al 10\n"))
    if secret_number == var_number :
        print ("haz adivinado el numero")
        break #
    else :
        print ( "intenta con otro numero")

number_one = int(input("ingrese el primer numero"))
main_number = 0
number_two = int(input("ingrese el segundo numero"))
number_three = int(input ("ingrese el tercer numero"))
if number_one > number_two and number_one > number_three :
    main_number = number_one
elif number_two > number_one and number_two > number_three :
    main_number = number_two
else :
    main_number = number_three

print (f"el numero mayor es: {main_number}")

note_counter = 1
approved_notes = 0
disapproved_notes = 0
prom_approved_notes = 0
prom_disapproved_notes = 0
prom_notes = 0
total_notes = int(input("ingrese la cantidad de notas"))
while note_counter <= total_notes :
        actual_note = int(input(f"ingrese la nota numero {note_counter}"))
        if actual_note < 70 :
            disapproved_notes = disapproved_notes + 1
            prom_disapproved_notes = actual_note + prom_disapproved_notes
            note_counter = note_counter + 1
        else :
            approved_notes = approved_notes + 1
            prom_approved_notes = actual_note + prom_approved_notes
            note_counter = note_counter + 1
prom_notes = ( prom_approved_notes + prom_disapproved_notes ) / total_notes
if disapproved_notes != 0 :
    prom_disapproved_notes = prom_disapproved_notes / disapproved_notes
else:
    prom_disapproved_notes = 0

if approved_notes != 0 :
    prom_approved_notes = prom_approved_notes / approved_notes
else:
    prom_approved_notes = 0
print (f"el estudiante tiene {approved_notes} notas aprobadas")
print (f"el promedio de notas aprobadas es de {prom_approved_notes}")
print (f"el estudiante tiene {disapproved_notes} notas no aprobadas")
print (f"el promedio de notas no aprobadas es de {prom_disapproved_notes}") 
print (f"el promedio de notas total es de {prom_notes}")