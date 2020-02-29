#!/usr/bin/env python3
import os, sys#,bs4, re
import pandas as pd
import numpy as np
from urllib.parse import quote, unquote
#from urllib.request import urlopen

"Program przyjmuje jako prawidłowe argumenty pliki wynikowe programu orca z dowolnym rozszerzeniem(preferowane rozszerzenie .out)"


if not sys.argv[1:]:
    print('Wprowadzono niepoprawny argument.')
    sys.exit()
dane = {}
E = {}
metody = set()
for plik in sys.argv[1:]:
    sciezka = os.path.splitext(plik) # odrzuc rozszerzenie i zostaw sciezke
    nazwa = os.path.split(plik)[1] # odrzuc sciezke
    nazwa = os.path.splitext(nazwa)[0]  # odrzuc rozszerzenie
    W = nazwa.split('_')
    part = W[-1]  # A, B lub AB
    nrid = W[0] # numer katalogowy dimeru
    metoda = unquote(W[-2])
    metody.add(metoda)
    if nrid not in dane:
        dane[nrid] = {}
    if metoda not in dane[nrid]:
        dane[nrid][metoda] = {}
    dane[nrid][metoda][part] = nazwa
    Energie = 'E_'+str(W[-1])
    Czas = 'T_'+str(W[-1])
    A = open(str(sciezka[0])+'.out')
    while 1: 
        line = A.readline()
        if line == '': 
            break
        if line.find('FINAL SINGLE POINT ENERGY') !=-1: 
            line_splited=line.split()
            dane[nrid][metoda][Energie] = float(line_splited[4])
        if line.find('TOTAL RUN TIME') !=-1: 
            line_splited=line.split()
            dane[nrid][metoda][Czas] = float(line_splited[3])*86400+float(line_splited[5])*3600+float(line_splited[7])*60+float(line_splited[9])+float(line_splited[11])/1000 #jednostka to sekundy

wyniki = {'3957': '-6.493', '3958': '-5.006', '3959': '-4.745', '3960': '-4.581', '3961': '-3.137', '3962': '-1.654', '3963': '-0.765', '3964': '-0.663', '3965': '-4.554', '3966': '-2.557', '3967': '-1.621', '3968': '-1.524', '3969': '-1.374', '3970': '-1.09', '3971': '-0.502', '3972': '-1.485', '3973': '-0.827', '3974': '-0.607', '3975': '-0.533', '3976': '-0.405', '3977': '-0.364', '3978': '0.821', '3979': '0.934', '3980': '1.115'}

#w kolumnie 1. nr indexu , w 2. nazwa kompleksu w 3. wynik bazowy dokladny, kolejne kolumny to wyniki kolejnych metod
table3 = pd.DataFrame([[0.0]*len(metody)],index=('Suma',),columns=sorted(metody))
table = pd.DataFrame(index=dane.keys(), columns=['NAZWA KOMPLEKSU'] + ['Wynik dokladny'] + sorted(metody))
for nrid in dane:
    for metoda in dane[nrid]:
        table.loc[nrid,"NAZWA KOMPLEKSU"] = (dane[nrid][metoda]['A']).split('_')[1]
        table.loc[nrid, 'Wynik dokladny'] = float(wyniki[nrid])
        wsp = (dane[nrid][metoda]['E_AB']-dane[nrid][metoda]['E_B']-dane[nrid][metoda]['E_A'])*627.5
        table.loc[nrid, metoda] = wsp
        table3.loc['Suma',metoda] += sum([dane[nrid][metoda][k] for k in ('T_A', 'T_B', 'T_AB')])
print(table)
table.to_excel('Energie.xlsx', sheet_name='Sheet1')
 
print(table3)

from matplotlib import pyplot as plt

table2 = pd.DataFrame(index=['MUE']+['MSE']+['STD'],columns=sorted(metody))
for metoda in sorted(metody):
    blad = table.loc[:,metoda] - table.loc[:,'Wynik dokladny']
    table2.loc['MUE',metoda] = np.mean(np.abs(blad)) 
    table2.loc['MSE',metoda] = np.mean(blad)
    table2.loc['STD',metoda] = np.std(blad)
    
table2.to_excel('Wartosci_bledow.xlsx', sheet_name='Sheet1') 

table3.to_excel('Wartosc_czas.xlsx', sheet_name='Sheet1')
print(table2)
MUE = plt.figure(0,figsize=(10,5))
MUE = plt.subplots_adjust(left=0.39)
MUE = plt.barh(list(sorted(metody)),table2.loc['MUE'], align='center')
MUE = plt.xlabel('MUE - średni błąd bezwględny [kcal/mol]')
MUE = plt.ylabel('Metody')
MUE = plt.title('Zależność błędu od metody:')
MUE = plt.savefig('figure0.png', dpi=200, transparent=True)
MSE = plt.figure(1,figsize=(10,5))
MSE = plt.subplots_adjust(left=0.39)
MSE = plt.barh(list(sorted(metody)),table2.loc['MSE'], align='center')
MSE = plt.xlabel('MSE - średni błąd ze znakiem [kcal/mol]')
MSE = plt.ylabel('Metody')
MSE = plt.title('Zależność błędu od metody:')
MSE = plt.savefig('figure1.png', dpi=200, transparent=True)

STD = plt.figure(2,figsize=(10,5))
STD = plt.subplots_adjust(left=0.39)
STD = plt.barh(list(sorted(metody)),table2.loc['STD'], align='center')
STD = plt.xlabel('STD - odchylenie standardowe wartości błędów [kcal/mol]')
STD = plt.ylabel('Metody')
STD = plt.title('Odchylenie standardowe błędów w zależności od metody:')
STD = plt.savefig('figure2.png', dpi=200, transparent=True)

CZAS = plt.figure(0,figsize=(10,5))
CZAS = plt.subplots_adjust(left=0.39)
CZAS = plt.barh(list(sorted(metody)),table3.loc['Suma'], align='center')
CZAS = plt.xlabel('t - czas [s]')
CZAS = plt.ylabel('Metody')
CZAS = plt.title('Zależność czasu wykonywania od metody:')
CZAS = plt.savefig('ftime.png', dpi=200, transparent=True)

plt.show(MUE)
plt.show(MSE)
plt.show(STD)
plt.show(CZAS)




"Poniżej znajduje się skrypt do wyciągania danych wyników dokładnych ze storny bazy BEGDB"

#inp = urlopen('http://www.begdb.com/index.php?action=oneDataset&id=34&state=show&order=ASC&by=name_m&method=')
#re_id = re.compile('id=(\d+)')
#html = inp.read()
#bs = bs4.BeautifulSoup(html)
#thead = bs.find('thead')
#ncol = 0
#for cell in thead.find_all('th'):
#  szukana = cell.find('div', attrs={'id':'lib'})
#  if szukana: break
#  ncol += 1
#  
#wyniki = {}
#tbody = thead.parent.find('tbody')
#for row in tbody.find_all('tr'):
#  for i, cell in enumerate(row.find_all('td')):
#      if i==0:
#          link = cell.find('a')
#          szuk_id = re_id.search(link['href'])
#          setid = szuk_id.groups()[0]
#      if i==2:
#          wyn = cell.text
#          wyniki[setid] = wyn
#          break
        