def iloczyn(lista):
    Iloczyn = 1
    for i in lista:
        Iloczyn*=i
    return(Iloczyn)

def suma(lista):
    Suma = 0
    for i in lista:
        Suma+=i
    return(Suma)

lista = [1,2,3,4,5]
warunek = 1
while 1:
    if warunek==1:
        warunek = input('Policz dla zadanej tablicy:\nM - mnozenie\nD - dodawanie\nO - Oba!\n')
    if warunek == 'M':
        print('Iloczyn = ',iloczyn(lista))
        break
    elif warunek == 'D':
        print('Suma = ',suma(lista))
        break
    elif warunek == 'O':
        print('Iloczyn = ',iloczyn(lista))
        print('Suma = ',suma(lista))
        break
    else :
        warunek = input('Wybierz z opcji ponizej:\nM - mnozenie\nD - dodawanie\nO - Oba!\n')