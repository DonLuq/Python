

class Student:
    
    def __init__(self,imie,indeks):
        self.imie = imie
        self.id = indeks
        self.oceny = {}
        
    def dodaj_ocene(self,A,B):
        self.oceny[A] = B
        
    def drukuj_indeks(self):
        print("Student",self.imie,"->",self.id)
        print("Oceny:")
        for ocena in self.oceny.keys():
            print(ocena,"->",self.oceny[ocena])
        
    
    
    
    
s = Student("Jan",123)
s.dodaj_ocene("Matematyka","db")
s.dodaj_ocene("fizyka","bdb")

s.drukuj_indeks()