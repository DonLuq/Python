import glob as G

def kontr_liczb(pesel):
    Ostat_liczba = 9*int(pesel[0])+ 7*int(pesel[1]) + 3*int(pesel[2]) + 1*int(pesel[3]) + 9*int(pesel[4]) + 7*int(pesel[5]) + 3*int(pesel[6]) + 1*int(pesel[7]) + 9*int(pesel[8]) + 7*int(pesel[9])
    if Ostat_liczba%10 == int(pesel[10]):
        return(True)
    else:
        return(False)

def data_urodz(pesel):
    A = pesel[:6]
    if pesel[0]=='0':
        pesel[2] = str(int(pesel[2])-2)
        data = A[4:]+'-'+A[2]+A[3]+'-20'+A[:2]
    else:
        data = A[4:]+'-'+A[2]+A[3]+'-19'+A[:2]
    return(data)
def plec(pesel):
    A = int(pesel[9])
    if A%2 == 0:
        return('żeńska')
    if A%2 == 1:
        return('męska')

path = G.glob('./*PESEL.txt*')
if not path == '':
    plik = open(path[0],'r')
    F = open('PESEL_ID.txt','w+')
    while 1:
        tresc = list(plik.readline())
        tresc = ('').join(tresc[:-1])
        if tresc == '' or tresc =='\n':
            break
        if kontr_liczb(tresc): 
            F.write('nr PESEL: '+tresc+' jest prawidłowy.\n')
            F.write('Data urodzenia: '+data_urodz(tresc)+'\tpłeć: '+plec(tresc)+'\n')
    plik.close()
    F.close();

    
    


