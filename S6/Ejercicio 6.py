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