L1 = [1,2,3,4,5,6,7,8,9,10]

plik = open('wynik.txt','w+')
for i in range(len(L1)):
    plik.write(str(L1[i])+'\n')
plik.close()