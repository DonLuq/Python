import random as R
import time as T

#SORTOWANIE PZEZ WSTAWIANIE
def Insert_sort(A):
    for i in range(1,len(A)):
        klucz = A[i]
        j = i - 1
        while j>=0 and A[j]>klucz:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz
    
L1 = []
L2 = []
L3 = []

for i in range(100): #L1
    L1.append(R.randint(0,20))
    
for i in range(200): #L2
    L2.append(R.randint(0,20))
    
for i in range(300): #L3
    L3.append(R.randint(0,20))

clock1 = T.time()
Insert_sort(L1)
print('Czas dla sortowania L1 = {0:.4} ms'.format((T.time()-clock1)*1000))

clock2 = T.time()
Insert_sort(L2)
print('Czas dla sortowania L2 = {0:.4} ms'.format((T.time()-clock2)*1000))

clock3 = T.time()
Insert_sort(L3)
print('Czas dla sortowania L3 = {0:.4} ms'.format((T.time()-clock3)*1000))

