import sys
import SzyfrCezara as S
import datetime as T
import glob as G
import os

def funkcja(sciezka,n,czas):    
    plik = open(sciezka,'r')
    if plik.mode == 'r':
        tekst = plik.read()
    plik.close()

    
    Tajne = S.deszyfruj(tekst,n)

    #print('Po deszyfrowaniu:\n',Tajne)

    plik = open('plik_deszyfrowany_'+str(n)+'_'+str(czas)+'.txt',"w+")
    if plik.mode == 'w+':
        plik.write(Tajne)
    plik.close()

if not sys.argv[1:]:
    sciezka = input('Wprowadz sciezke do katalogu:\n')
    #sciezka = "/Users/lukaszbajsarowicz/Desktop/UWRPython/List8/"
    #sciezka = 'plik_do_szyfrowania.txt'
    
else:
    sciezka = sys.argv[1]

lista_path = G.glob(sciezka + "*plik_zaszyfrowany*.txt")

for path in lista_path:
    P = os.path.splitext(path)[0]
    P = os.path.split(P)[1]
    L = P.split('_')
    funkcja(path,L[2],L[3])

#Nazwa pliku nie ma zmienionej daty bo po dluzszym rozwazaniu stwierdzilem ze nie mialoby to sensu.
    