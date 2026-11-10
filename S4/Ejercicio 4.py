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