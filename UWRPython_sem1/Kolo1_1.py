#distance

def dis(x1,y1,x2,y2):
    Odl = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    print('Odległość = ',Odl)
    
    
X1 = float(input('Wprowadz pierwsze współrzędne:\nx1 = '))
Y1 = float(input('y1 = '))

X2 = float(input('Wprowadz drugie współrzędne:\nx2 = '))
Y2 = float(input('y2 = '))


dis(X1,Y1,X2,Y2)