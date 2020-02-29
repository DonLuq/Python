import random as R
import time as T

#SORTOWANIE BABELKOWE
def Bombelek_sort(A):
    for i in range(len(A) - 1, 0, -1):
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    
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
Bombelek_sort(L1)
print('Czas dla sortowania L1 = {0:.4} ms'.format((T.time()-clock1)*1000))

clock2 = T.time()
Bombelek_sort(L2)
print('Czas dla sortowania L2 = {0:.4} ms'.format((T.time()-clock2)*1000))

clock3 = T.time()
Bombelek_sort(L3)
print('Czas dla sortowania L3 = {0:.4} ms'.format((T.time()-clock3)*1000))

