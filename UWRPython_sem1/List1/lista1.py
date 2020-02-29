Python 3.7.4 (default, Sep  7 2019, 18:27:02) 
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.


ZADANIE 1

>>> a=input()
2
>>> b=input()
2
>>> a+b
'22'
>>> suma=a+b
>>> print(suma)
22
>>> 
//input w pythonie przyjmuje wartosci z klawiatury ktore domyslnie sa typu string, jezeli dodajemy string do stringa to je scalamy.


ZADANIE 2

>>> import math
>>> a=3
>>> b=4
>>> alpha=47
>>> Pole=a*b*math.sin(alpha/180*math.pi)/2
>>> print(Pole)
4.388122209715023
>>> 


ZADANIE 3

>>> import math
>>> a= float(input())
5
>>> b= float(input())
5
>>> alpha= float(input())
60
>>> alpha= float(input())
60
>>> Pole= a*b*math.sin(alpha/180*math.pi)
>>> print(Pole)
21.650635094610966
>>> 

ZADANIE 4

>>> import builtins
>>> dir()
>>> dir('__buildins__')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(print)
>>> print("Ala ma kota")
Ala ma kota
>>> print(2+2)
4
>>> print("{}\t{}\t{}\t{}".format(str(2**5),str(35//2),str(35/2),str(35%2)))
32	17	17.5	1
>>> print("{}\n{}\n{}\n{}".format(str(2**5),str(35//2),str(35/2),str(35%2)))
32
17
17.5
1
>>>

ZADANIE 5

>>> import math
>>> 5//3
1
>>> round(5/3)
2
>>> 5/3
1.6666666666666667
>>> math.floor(5/3)
1

//Dzielenie bez reszty ucina nam reszte nie wazne jaka jest, round zaokralga dla do blizszej wartosci calkowitej, w przypadku 1.5 przyjmujemy zaokraglenie w do 1 czyli w dol. 
Funkcja math.floor() powoduje zaokrąglenie do dołu.

ZADANIE 6

>>> (-17)**(1/2)
(2.5246740534795566e-16+4.123105625617661j)
>>> 

ZADANIE 7

>>> a= 2 
>>> b= 30
>>> a + b 
32
>>> _
32
>>> a + 10 
12
>>> _
12
>>> "cokolwiek"
'cokolwiek'
>>> _
'cokolwiek'
>>> input()
2
'2'
>>> _
'2'
>>> 

//pełni role separatora slow w funkcjach oraz ostatniego outputa tzw. Ans, wyniku działania.

ZADANIE 8

>>> "ZALOZENIE: b<a"
'ZALOZENIE: b<a'
>>> a = float(input())
8
>>> b = float(input())
5
>>> Z = b%a
>>> print(Z)
5.0
>>> Z*=Z+3
>>> print(Z)
40.0
>>> 

ZADANIE 9

>>> import cmath
>>> z = complex(input())
2+4j
>>> type(z)
<class 'complex'>
>>>cmath.polar(z)
(4.47213595499958, 1.1071487177940904) #(|z|,arg)
>>>import numpy
>>> numpy.conjugate(z)
(2-4j)
>>> z
(2+4j)
>>> 

ZADANIE 10

>>> z=(0+1j)
>>> cmath.sin(z).real
0.0
>>> cmath.sin(z).imag
1.1752011936438014
>>> cmath.cos(z).real
1.5430806348152437
>>> cmath.cos(z).imag
-0.0
>>> (cmath.sin(z))**2+(cmath.cos(z))**2
(1.0000000000000002+0j) #Spelnione tylko program ma swoje przyblizenia i dlatego wyrzuca jakies tam dodatki na ostatnim miejscu po przecinku ;)


