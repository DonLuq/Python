class Converter:
    
    def __init__(self,dlugosc,jednostka):
        self.dl = dlugosc
        self.jd = jednostka
        self.przeliczniki = {'cal':0.0254,'stopa':0.3048,'jard':0.9144,'mila':1609.344,'km':1000,'m':1,'cm':0.01,'mm':0.001}
    
    def cal(self):
        if self.jd in self.przeliczniki:
            ile_m = self.przeliczniki[self.jd] * self.dl
        return ile_m/self.przeliczniki['cal']
    def stopa(self):
        if self.jd in self.przeliczniki:
            ile_m = self.przeliczniki[self.jd] * self.dl
        return ile_m/self.przeliczniki['stopa']
    def jard(self):
        if self.jd in self.przeliczniki:
            ile_m = self.przeliczniki[self.jd] * self.dl
        return ile_m/self.przeliczniki['jard']
    def mila(self):
        if self.jd in self.przeliczniki:
            ile_m = self.przeliczniki[self.jd] * self.dl
        return ile_m/self.przeliczniki['mila']
    def km(self):
        if self.jd in self.przeliczniki:
            ile_m = self.przeliczniki[self.jd] * self.dl
        return ile_m/self.przeliczniki['km']
    def m(self):
        if self.jd in self.przeliczniki:
            ile_m = self.przeliczniki[self.jd] * self.dl
        return ile_m/self.przeliczniki['m']
    def mm(self):
        if self.jd in self.przeliczniki:
            ile_m = self.przeliczniki[self.jd] * self.dl
        return ile_m/self.przeliczniki['mm']
    def cm(self):
        if self.jd in self.przeliczniki:
            ile_m = self.przeliczniki[self.jd] * self.dl
        return ile_m/self.przeliczniki['cm']
    
    def __add__(self, other):
        self.dl = self.dl + (other.przeliczniki[other.jd] * other.dl)/other.przeliczniki[self.jd]
        self.jd = self.jd
        return Converter(self.dl,self.jd)
    
c = Converter(9,'stopa')
d = Converter(9,'cal')
#print(d.cal())

e = c + d
print(e.dl)
print(e.jd)