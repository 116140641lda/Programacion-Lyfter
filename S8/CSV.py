# import csv

# def append_dictionary (information, keys, value):
#     information[keys] = value

# def request_info (information, headers):
#     while True:
#         name = input('ingrese el nombre del videojuego\n')
#         gender = input('ingrese el genero del videojuego\n')
#         designer = input('ingrese el desarrollador del video juego\n')
#         clasification = input('ingrese la clasificacion ESRB\n')
#         append_dictionary(information, headers[0], {name})
#         append_dictionary(information, 'gender' , {gender} )
#         append_dictionary(information, 'designer' , [designer] )
#         append_dictionary(information, 'clasification' , {clasification})
#         write_file('games.txt',information, headers)
          
        
      

# def write_file (path, information, headers):
#     with open (path, 'w', encoding= 'utf-8') as file:
#         writer = csv.DictWriter(file, headers)
#         writer.writeheader()
#         writer.writerows(information)

import csv

def append_dictionary (information, keys, value):
    information[keys] = value
  

def request_info (information, headers):
    while True:
        name = input('ingrese el nombre del videojuego\n')
        gender = input('ingrese el genero del videojuego\n')
        designer = input('ingrese el desarrollador del video juego\n')
        clasification = input('ingrese la clasificacion ESRB\n')
        append_dictionary(information, 'name', name)
        append_dictionary(information, 'gender', gender)
        append_dictionary(information, 'designer' , designer )
        append_dictionary(information, 'clasification' , clasification)
        write_file('games.csv',information, headers)
          

def write_file (path, information, headers):
    with open (path, 'a', encoding= 'utf-8') as file:
        writer = csv.DictWriter(file, headers)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(information)




def main ():
    information = {}
    headers = ['name', 'gender','designer', 'clasification']
    information = request_info(information, headers)


main()





# def main ():
#     information = []
#     headers = ['name', 'gender','designer', 'clasification']
#     information = request_info(information, headers)


# main()
    