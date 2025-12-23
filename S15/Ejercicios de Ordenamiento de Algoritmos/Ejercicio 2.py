def bubble_sort (sort_list):
    for out_i in range (0,len(sort_list)-1):
        changes_on = False
        for i in range(0,len(sort_list)-1 - out_i):
            actual_element = sort_list[i]
            next_element = sort_list[i+1]
            
            print(f"Esta es la iteraciòn # {i}, el elemento actual es el: {actual_element} y el siguiente elemento de la lista es el {next_element}")

            if next_element < actual_element:
                print("Este elemento es mayor al anterior, vamos a cambiarlo....")
                sort_list [i] = next_element
                sort_list [i+1] = actual_element
                changes_on = True
                print(Main_list)

        if not changes_on:
            return 
    

Main_list = [1,8,-12,4,-30]
bubble_sort(Main_list)

print(Main_list)