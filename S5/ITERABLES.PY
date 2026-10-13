
First_list = ['red' ,
              'yellow', 
              'blue',
             'orange',
			 'green'
             ]
second_list = ['apple', 'flower', 'snapple', 'orange', 'lettuce']
for index in range(len(First_list)):
	print(First_list[index], second_list[index])

my_string = 'arroz y frijoles'
my_string_reverse = my_string[::-1]
for string in my_string_reverse:
    print (string)



lista1 = ['5','21','6','8','9','12']
Lista2 = ['9','4','5','60','15','10']

lista1[0], lista1[-1] =  lista1[-1], lista1 [0]
print ("Lista 1 nueva:", lista1)
print ("Lista 2 nueva:", Lista2)


my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,20]
lista_pares = []
for index in my_list:
    if index % 2 == 0:
     lista_pares.append (index)

print(lista_pares)


numbers = []
for index in range(10):
    number = int( input (f"ingrese el numero {index+1}: "))
    numbers.append(number)
    bigger_number = max(numbers)

print (f"{numbers} el mas alto de todos fue el" , bigger_number)