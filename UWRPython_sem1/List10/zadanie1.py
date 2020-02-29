import math as M

class Kolo:
    
    def __init__(self,r):
        self.rap = r
        
    def pole(self):
        return M.pi*self.rap**2
    def obw(self):
        return 2*M.pi*self.rap
        
        
kolo_1 = Kolo(7)
kolo_2 = Kolo(4)


print('Pole kola o r =',kolo_2.rap,'wynosi:',kolo_2.pole())
print('Obwod kola o r =',kolo_2.rap,'wynosi:',Kolo.pole(kolo_2))


