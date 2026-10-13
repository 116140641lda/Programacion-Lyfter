def order_words ():
    my_string = 'papel-lapiz-lapicero-tajador-borrador-pizarra'
    my_list = my_string.split('-')
    my_list.sort ()
    new_string = "-" .join(my_list)
    return new_string

new_string = order_words()
print(new_string)