def mult_numbers():
    print("this is multiple")

def calc_numbers():
    print ("this is calculator")
    mult_numbers()

calc_numbers()
   

    
def call_var (var):
    for index, number in enumerate(var):
        var[index] = number * 5


def call_outside ():
    var = [80,50,100]
    call_var(var)
    print(var)


call_outside()

const_var = 10

def change_const_var (const_var):
    const_var = const_var + 1
    print(const_var)


change_const_var (const_var)




my_list = [1,5,10,25,60]

def sum_numbers (my_list):
    return sum(my_list)

sum_num = sum_numbers(my_list)
print (sum_num)

def revere_string ():
    my_string = 'Hola Mundo'
    my_string_reverse = my_string[::-1]
    print(my_string_reverse)

revere_string()


def count_may_min (text):
    upper = 0
    lower = 0
    for lett in text:
        if 'A' <= lett <= 'Z':
            upper +=1
        elif 'a' <= lett <= 'z':
            lower +=1
    return upper, lower

text = 'Esta Es Mi Oracion'
uuper, loower = count_may_min(text)

print(f'la cantidad de mayúsculas es: {uuper}')
print (f'la cantidad de minúsculas es: {loower}')

def order_words ():
    my_string = 'papel-lapiz-lapicero-tajador-borrador-pizarra'
    my_list = my_string.split('-')
    my_list.sort ()
    new_string = "-" .join(my_list)
    return new_string

new_string = order_words()
print(new_string)

def get_prime (number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0 :
            return False
    return True


def create_list ():
    my_list = [1,4,6,7,13,9,67]
    sec_list = []
    for number in my_list:
        if get_prime(number):
            sec_list.append(number)
    return sec_list

sec_list = create_list()
print(sec_list)

