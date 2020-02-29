Python 3.7.4 (default, Sep  7 2019, 18:27:02)
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>

ZADANIE 1

>>> litera = input()
k
>>> samogloski = ["a","e","i","o","u"]
>>> if litera in samogloski:
...     print("Twoja literka jest samogloska :)")
... else :
...     print("Twoja literka jest spolgloska :D")
...
Twoja literka jest spolgloska :D

ZADANIE 2

>>> h = int(input())
5
>>> if (h%2==0):
...     print("Liczba jest parzysta!")
... else:
...     print("Liczba jest nieparzysta!")
...
Liczba jest nieparzysta!
>>>


TUTAJ NAPISAC BEZ IF 
#print(a==b)
#'' = 0 = false
#'cokolwiek' = 1 = true;
>>> h = int(input())
4
>>> print('Twoja liczba jest nieparzysta!' and h%2 or 'Twoja liczba jest parzysta')
Twoja liczba jest parzysta
>>>

ZADANIE 3

#ax2+bx+c=0
A = float(input('Wprowadz kolejno mnożniki a,b,c dla rownania Ax^2+bx+c=0\nA = '))
if A==0:
    while(A==0):
        A = float(input('Wprowadz a rozne od 0: '))
B = float(input('\nB = '))
C = float(input('\nC = '))
Delta = B**2-4*A*C
if Delta == 0:
    print('Pierwiastek jest jeden i wynosi: ',-1*B/2/A)
if Delta < 0:
    print('Brak pierwiastkow rzeczywistych!')
if Delta > 0:
    print('\nDla rownania ',A,'x^2 + (',B,')x + (',C,') = 0')
    print('\nPierwiastki wyniosly: ',(B*(-1)-(Delta)**(1/2))/2/A,' oraz ',(-1*B+(Delta)**(1/2))/2/A,' !!')
    

ZADANIE 4

print("""
*            *        ****
*           * *       *   *
*          *   *      *   *
*         *******     ****
*        *       *    * *
*       *         *   *  *
*****  *           *  *   *

""")

ZADANIE 5

import re

while 1:
    name = input('Wprowadz slowo zawierajace a-z,A-Z,0-9 oraz jeden znak z $,#,@:\n')
    if re.search('[a-z]+',name):
        if re.search('[A-Z]+',name):
            if re.search('[a-z,A-Z,0-9]+',name):
                if re.search('[$#@]+',name):
                    if re.search('[a-z,A-Z,0-9,$#@]+',name):
                        if len(name)>6 and len(name)<16:
                            print('Haslo spelnia zadane warunki!!\nDONE!')
                            break

ZADANIE 6

i = int(input('Wprowadz liczbe:\n'))

for x in range(1,i+1):
    ij=[]
    for j in range(1,11):
        ij.append(x*j)
    print(ij)

ZADANIE 7

N=int(input('Wprowadz N do ktorego zostana wypisane liczby fibonnaciego:\n'))
a=0
b=1
for x in range(0,N+1,1):
    if x==0:
        print('For N = ',x,'\t\tFibonnaci number =\t',0)
    elif x==1:
        print('For N = ',x,'\t\tFibonnaci number =\t',1)
    elif x>1:
        fib = a + b
        a = b
        b = fib
        print('For N = ',x,'\t\tFibonnaci number =\t',fib)

ZADANIE 8

for i in range(1,10,1):
print(str(i)*i)

ZADANIE 9

n=int(input('Wprowadz ilosc kolumn (n):\n')) #kolumny
m=int(input('Wprowadz ilosc wierszy (m):\n')) #wiersze
tab = [[0 for x in range(n)] for k in range(m)]
for i in range(0,m):
    for j in range(0,n):
        tab[i][j]=i*j
print(tab)

ZADANIE 10

wyniki= []
for i in range(100,402,2):
    a = str(i)
    if int(a[0])%2==0 and int(a[1])%2==0:
        b = int(i)
        wyniki.append(b)
print(wyniki)

>>> %Run zadanie10.py
[200, 202, 204, 206, 208, 220, 222, 224, 226, 228, 240, 242, 244, 246, 248, 260, 262, 264, 266, 268, 280, 282, 284, 286, 288, 400]
>>>






