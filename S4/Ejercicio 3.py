import random
var_number = random.randint (1,10)
while True :
    secret_number = int(input ("Ingrese un numero del 1 al 10\n"))
    if secret_number == var_number :
        print ("haz adivinado el numero")
        break #
    else :
        print ( "intenta con otro numero")