my_dictionary = {
        'nombre' : 'Hilton',
        'numero_de_estrellas' : 5 , 
        'Habitaciones' : [
        ['1' , 'piso1' , '50'],
        ['2' , 'piso1' , '50'],
        ['3' , 'piso2' , '60'],
        ['4' , 'piso2' , '60'],
        ], 
    }

print (my_dictionary['Habitaciones'])

list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']
dictionary = dict(zip(list_a,list_b))
print (dictionary)

list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
print(employee)

for element in list_of_keys:
    if element in employee.keys():
        employee.pop(element)


sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

upc_sales = {

}
for sale in sales:
    for item in sale['items']:
        upc = item['upc']
        unite_price = item['unit_price']

        if upc in upc_sales:
            upc_sales[upc] += unite_price
        else:
            upc_sales[upc] = unite_price

print(upc_sales)
