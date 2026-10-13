def bubble_sort_right (sort_list):
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
                print(sort_list)

        if not changes_on:
            return
        # On2 
        
def bubble_sort_left(sort_list):
    
    for out_i in range (len(sort_list)-1):
        changes_on = False
        iteration = 1

        for i in range(len(sort_list)-1,out_i,-1):
                actual_element = sort_list[i]
                prev_element = sort_list[i-1]
                
                print(f"Esta es la iteraciòn # {iteration}, el elemento actual es el: {actual_element} y el anterior elemento de la lista es el {prev_element}")

                if actual_element > prev_element:
                    print("Este elemento es mayor al anterior, vamos a cambiarlo....")
                    sort_list [i] = prev_element
                    sort_list [i-1] = actual_element
                    changes_on = True
                    
                else:
                    print("El elemento es menor al anterior, se mantiene el lugar")

                print(sort_list)
                iteration += 1

            # On2


        if not changes_on:
            return sort_list
        
    return sort_list
    

# Main_list = [1,8,-12,4,-30]
# bubble_sort_right(Main_list)

Main_list_left = [3,-5,-20,50,-50]
bubble_sort_left(Main_list_left)

