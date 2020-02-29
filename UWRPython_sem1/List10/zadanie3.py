import itertools as IT

class Cyferki:
    
    def __init__(self, n):
        self.n = n
        
    def tri_elementy(self):
        TaB = []
        TaA = IT.combinations(self.n,3)
        for h in TaA:
            if h[0]+h[1]+h[2]==0:
                TaB.append(list(h))
        return TaB
    
n = [1,-2,-3,4,-5,6,-7,8,9]

print(Cyferki(n).tri_elementy())

