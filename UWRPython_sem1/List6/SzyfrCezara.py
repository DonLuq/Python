
# TEN TYP FOR NIE PODMIENIA WARTOSCI TYLKO DZIALA NA KOPII REFERENCJE?
# def szyfruj(A:str):
#     B = list(A)
#     for b in B:
#         if ord(b)>=65 and ord(b)<=90:
#             b=ord(b)+4
#             if b>90:
#                 b-=25
#             b=chr(b)
#             print(b)
#         elif ord(b)>=97 and ord(b)<=122:
#             b = ord(b)+4
#             if b>122:
#                 b-=25
#             b=chr(b)
#             #print(b)
#     print(('').join(B))



def szyfruj(A:str):
    'Przesuwa podane literki o 4 miejsca w prawo'
    B = list(A)
    for i in range(len(B)):
        b = B[i]
        if ord(b)>=65 and ord(b)<=90:
            b=ord(b)+4
            if b>90:
                b-=26
            b=chr(b)
            B[i]=b
            #print(b)
        elif ord(b)>=97 and ord(b)<=122:
            b = ord(b)+4
            if b>122:
                b-=26
            b=chr(b)
            B[i]=b
            #print(b)
    return ('').join(B)

def deszyfruj(A:str):
    'Przesuwa podane literki o 4 miejsca w lewo'
    B = list(A)
    for i in range(len(B)):
        b = B[i]
        if ord(b)>=65 and ord(b)<=90:
            b=ord(b)-4
            if b<65:
                b+=26
            b=chr(b)
            B[i]=b
            #print(b)
        elif ord(b)>=97 and ord(b)<=122:
            b = ord(b)-4
            if b<97:
                b+=26
            b=chr(b)
            B[i]=b
            #print(b)
    return ('').join(B)
