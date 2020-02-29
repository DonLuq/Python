

class Kursy:
    
    def __init__(self,sciezka):
        self.sciezka = str(sciezka)
        self.Dict = self.kursy() # mozna stworzyc tylko na self wywolaniu bez self nie dziala ani z wywolaniem klasy// jaki wogole cudem to dziala?! dlaczego nie wyrzuca bledu?
        
    
    def show_me(self,A,B,ile):
        'Z A na B'
        if A in self.Dict.keys() and B in self.Dict.keys():
            a = float(self.Dict[A])
            b = float(self.Dict[B])
        else:
            print("Błąd, złe kody walut.")
        wart_B = ile*a/b
        return wart_B
      
    def kursy(self):
        nazwy = []
        wartosci = []
        A = open(self.sciezka,'r')
        while 1:
            line = A.readline()
            if line == '':
                break
            if line.find('<kod_waluty>') != -1:
                nazwy.append(line[12:15])
            if line.find('<kurs_sredni>') != -1:
                wartosci.append(line[13:18].replace(",","."))
            else:
                pass
        nazwy.append('PLN')
        wartosci.append(1.000)
        slow = dict(zip(nazwy,wartosci))
        #self.Dict = slow
        return slow

    def konwr_PLN(self,ile,rodz):
        if rodz in self.Dict.keys():
            A = self.Dict[rodz]
            wynik = ile/float(A)
        else:
            print("Błędny kod kraju")
            
        return wynik
    
    
    
kursy = Kursy("./plik.xml")

#print(kursy.Dict) # zmienna klasy w ktorej trzymane sa zczytane kursy dla obiektu

'Wypisanie słownika:'
for i in kursy.kursy():
    print(i,kursy.kursy()[i])

'Konwersja z PLN na dowolną walute'
print("Konwersja przykładowa z PLN(1000) na USD: ",kursy.konwr_PLN(1000,'USD'))

'Konwersja z pierwszego argumnetu na drugi, trzeci argument to liczność argumentu pierwszego'
print("Konwersja przykładowa z USD(1000) na EUR: ",kursy.show_me('USD','EUR',1000))



