'Aby uruchomic z argumentami z terminal line podaj w formie NAZWA_SKRYPTU(zadanie1.py) PLIK.TXT(:str) PRZESUNIECIE(:int)'
import sys
import SzyfrCezara as S
import datetime as T


if not sys.argv[1:]:
    sciezka = input('Wprowadz sciezke do pliku:\n')
    n = int(input('O ile liter chcesz przesunąć?:\n'))
else:
    sciezka = sys.argv[1]
    n = sys.argv[2]
    
plik = open(sciezka,'r')
if plik.mode == 'r':
    tekst = plik.read()
plik.close()
    

#%Y%m%d format czasu
czas = T.datetime.now()
czas = czas.strftime('%Y-%m-%d')

Tajne = S.szyfruj(tekst,n)

#print('Po szyfrowaniu:\n',Tajne)

plik = open('plik_zaszyfrowany_'+str(n)+'_'+str(czas)+'.txt',"w+")
if plik.mode == 'w+':
    plik.write(Tajne)
plik.close()

