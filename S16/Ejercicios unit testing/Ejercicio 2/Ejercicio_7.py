def order_words (words):
    words_list = words.split('-')
    words_list.sort ()
    return "-" .join(words_list)


new_string = order_words("ola-mar-arena")

print(new_string)