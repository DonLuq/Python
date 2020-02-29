#text = 'Ala ma kota'


def fun1(slovo):
    samo = ['a', 'ą', 'e', 'ę', 'i', 'o','u', 'y','A','Ą','E','Ę','I','O','U','Y']
    licz_samo = 0
    for lit in list(slovo):
        if lit in samo:
            licz_samo += 1
    #print(licz_samo)
    if licz_samo == 0:
        return 0
    if licz_samo %2 == 0:
        return 2
    else:
        return 1
    
def fun2(zdanie):
    licznik = 0
    zdania = zdanie.split(' ')
    for slovo in zdania:
        licznik += fun1(slovo)
    return licznik
    
    
text = input('TEXT: ')

print(fun2(text))