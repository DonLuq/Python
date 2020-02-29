Python 3.7.4 (default, Sep  7 2019, 18:27:02)
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.


ZADANIE 1

>>> a=1.2*10**3+34.5
>>> print((str(a)+";")*20)
1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;1234.5;

ZADANIE 2

>>> pewien_napis=input()
HELLO WORLD!
>>> print((pewien_napis+"\n")*30)
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!
HELLO WORLD!

ZADANIE 3 

>>> # ZAKLADAM ZE WPROWADZONY WYRAZ ma >= 4 litery
pewien_napis=input()
HELLO WORLD!
>>> pewien_napis
'HELLO WORLD!'
>>>new_word=pewien_napis[0]+pewien_napis[1]+pewien_napis[len(pewien_napis)-2]+pewien_napis[len(pewien_napis)-1]
>>> new_word
'HED!'
>>> new_word=pewien_napis[0]+pewien_napis[1]+pewien_napis[-2]+pewien_napis[-1]
>>> new_word
'HED!'

ZADANIE 4

>>> wyraz = input()
RABARBAR
>>> new_wyraz=wyraz[0]+wyraz[1:].replace(wyraz[0],"$")
>>> new_wyraz
'RABA$BA$'
>>>


ZADANIE 5

>>> letter=input()
MATEUSZ
>>> new_letter= letter[:(len(letter)//2)] + "PYTHON" + letter[(len(letter)//2):]
>>> new_letter
'MATPYTHONEUSZ'

ZADANIE 6

>>> lista = ['Kasia', 'Basia', 'Marek', 'Darek']
>>> lista.append('Jozek')
>>> lista
['Kasia', 'Basia', 'Marek', 'Darek', 'Jozek']
>>> lista.extend(['Basia', 'Ania'])
>>> lista
['Kasia', 'Basia', 'Marek', 'Darek', 'Jozek', 'Basia', 'Ania']
>>> lista.sort()
>>> lista
['Ania', 'Basia', 'Basia', 'Darek', 'Jozek', 'Kasia', 'Marek']
>>> lista[3]
'Darek'
>>> lista[:2]
['Ania', 'Basia']
>>> lista[-2:]
['Kasia', 'Marek']
>>> lista.remove('Basia')
>>> lista
['Ania', 'Basia', 'Darek', 'Jozek', 'Kasia', 'Marek']
>>> lista.remove('Basia')
>>> lista
['Ania', 'Darek', 'Jozek', 'Kasia', 'Marek']
>>> len(lista)
5
>>> lista = tuple(lista)
>>> lista
('Ania', 'Darek', 'Jozek', 'Kasia', 'Marek')

ZADANIE 7

>>> lista = [(2,8),(5,5),(9,3),(1,0),(3,2),(6,4),(1,9),(10,3),(2,3),(1,7)]
>>> lista
[(2, 8), (5, 5), (9, 3), (1, 0), (3, 2), (6, 4), (1, 9), (10, 3), (2, 3), (1, 7)]
>>> SORTED_LIST= sorted(lista,key = lambda x:x[1])
>>> SORTED_LIST
[(1, 0), (3, 2), (9, 3), (10, 3), (2, 3), (6, 4), (5, 5), (1, 7), (2, 8), (1, 9)]
>>>


ZADANIE 8

>>> lista_znakow = ['P','y','t','h','o','n']
>>> lista_znakow
['P', 'y', 't', 'h', 'o', 'n']
>>> ('').join(lista_znakow)
'Python'
>>> NAPIS =  ('').join(lista_znakow)
>>> NAPIS
'Python'

ZADANIE 9

>>> import itertools
>>> L = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
>>> Wynik = list(itertools.chain(*L))
>>> Wynik
[2, 4, 3, 1, 5, 6, 9, 7, 9, 0]


ZADANIE 10


>>> B = []
>>> for i in range(0,100,3):
...     B.append(i)
...
>>> print(B)
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
>>> for i in range(4,23,2):
...     del B[i]
...
>>> B
[0, 3, 6, 9, 15, 18, 24, 27, 33, 36, 42, 45, 51, 54, 60, 63, 69, 72, 78, 81, 87, 90, 96, 99]
>>>





