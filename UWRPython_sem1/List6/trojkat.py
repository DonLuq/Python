#trojkat.py

def obw(a,b,c):
    P = float(a)+float(b)+float(c)
    return P
    

def pole(a,b,c):
    p = obw(a,b,c)/2
    P = (p*(p-a)*(p-b)*(p-c))**(1/2)
    return P

def kind(a,b,c):
    if a==b and a==c:
        return 'równoboczny'
    if a==b or a==c or b==c:
        return 'równoramienny'
    else:
        return 'różnoboczny'

def radkind(a,b,c):
    if pole(a,b,c)<= 0:
        return 'TO NIE JEST TROJKAT!'
    MAX = max(a,b,c)
    if MAX  == a:
        if a**2==b**2+c**2:
            return 'prostokątny'
        if a**2>b**2+c**2:
            return 'rozwartokątny'
        if a**2<b**2+c**2:
            return 'ostrokątny'
    if MAX  == b:
        if b**2==a**2+c**2:
            return 'prostokątny'
        if b**2>a**2+c**2:
            return 'rozwartokątny'
        if b**2<a**2+c**2:
            return 'ostrokątny'
    if MAX  == c:
        if c**2==b**2+a**2:
            return 'prostokątny'
        if c**2>a**2+b**2:
            return 'rozwartokątny'
        if c**2<a**2+b**2:
            return 'ostrokątny'
    
