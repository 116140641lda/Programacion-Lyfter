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