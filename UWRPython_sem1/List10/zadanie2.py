import itertools as IT

#L = ['s','a','b','o']
L = [1,2,3]# ma dac  [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

class Lista:
    
    def __init__(self,lista):
        self.lista = lista
        
    def podlisty(self):
        i = len(self.lista)
        new_L = []
        while i>-1:
            A = list(IT.combinations(self.lista,i))
            for j in range(len(A)):
                new_L.append(list(A[j]))
            i = i - 1 
        return new_L
            
            

cokolwiek = Lista(L)
print(cokolwiek.podlisty())
#print(Lista.podlisty(L)) jak zrobic zeby cos takiego dzialalo? c: jak ustawic argument skierowany do funkcji nie bedacy argumentem obiektu tej klasy?