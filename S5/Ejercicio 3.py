list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
print(employee)

for element in list_of_keys:
    if element in employee.keys():
        employee.pop(element)