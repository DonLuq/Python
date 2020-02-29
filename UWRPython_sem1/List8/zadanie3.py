import random as R 

#pesel ma 11 cyfr

def pesel():
    pesel = []
    for i in range(2):
        pesel.append(int(R.random()*10))
    pesel.append(int(R.random()*100)%2)
    if pesel[2]=='0':
        pesel.append(int(R.random()*100)%10)
    else:
        pesel.append(int(R.random()*100)%2+1)
    pesel.append(int(R.random()*100)%2)
    if pesel[4]=='0':
        pesel.append(int(R.random()*100)%10)
    else:
        pesel.append(int(R.random()*100)%3)
    for i in range(4):
        pesel.append(int(R.random()*100)%10)
    if pesel[0]==0:
        pesel[2]+=2
    Ostat_liczba = 9*pesel[0]+ 7*pesel[1] + 3*pesel[2] + 1*pesel[3] + 9*pesel[4] + 7*pesel[5] + 3*pesel[6] + 1*pesel[7] + 9*pesel[8] + 7*pesel[9]
    pesel.append(Ostat_liczba%10)
    Pesel = ''
    for nr in pesel:
        Pesel+=str(nr)
    return(Pesel)


lista_pesel = []
for i in range(10):
    lista_pesel.append(pesel())

f = open('PESEL.txt','w+')
for i in range(len(lista_pesel)):
    #f.write('cokolwiek')
    f.write(lista_pesel[i]+'\n')
f.close()
