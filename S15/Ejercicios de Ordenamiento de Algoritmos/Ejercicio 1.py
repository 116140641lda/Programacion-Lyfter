def bubble_sort (sort_list):

    for i in range(0,len(sort_list)-1 ):
            actual_element = sort_list[i]
            next_element = sort_list[i+1]
            
            print(f"Esta es la iteraciòn # {i}, el elemento actual es el: {actual_element} y el siguiente elemento de la lista es el {next_element}")

    

Main_list = [1,4,8,9]
bubble_sort(Main_list)

print(Main_list)