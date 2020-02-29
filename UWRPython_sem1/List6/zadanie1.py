import trojkat as T

while 1:
    a = float(input('Wprowadz boki trojkata:\n'))
    b =float(input(''))
    c =float(input(''))

    if a+b>c and b+c>a and c+a>b: 
        Obwod = T.obw(a,b,c)
        Pole = T.pole(a,b,c)
        Rodzaj = T.kind(a,b,c)
        Kat = T.radkind(a,b,c)
        print('Obwod wynosi: ',Obwod)
        print('Pole wynosi: ',Pole)
        print('Trojkąt jest : ',Rodzaj)
        print('Trojkat jest : ',Kat)
        break