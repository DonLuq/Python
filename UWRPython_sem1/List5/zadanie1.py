# 1 do 59

Dict = {"jeden":1, "dwa":2, "trzy":3, "cztery":4, "pięć":5, "sześć":6,

           "siedem":7, "osiem":8, "dziewięć":9, "dziesięć":10, "jedenaście":11,

           "dwanaście":12, "trzynaście":13, "czternaście":14, "piętnaście":15,

           "szesnaście":16, "siedemnaście":17, "osiemnaście":18,

         "dziewiętnaście":19, "dwadzieścia":2, "trzydzieści":3,

         "czterdzieści":4, "pięćdziesiąt":5}

def liczba(S:str='czterdzieści cztery'):
    Suma=0
    slova = S.split(' ')
    #print(slova)
    for i in range(len(slova)):
        if slova[i] in Dict:
            slova[i]=str(Dict[slova[i]])
            #print(slova[i])
        else:
            return 'Błąd, błędny zapis!'
    Suma = ('').join(slova)
    return Suma


S = input('Wprowadz slownie liczbe z przedzialu od 1 do 59:\n')
print(liczba(S))