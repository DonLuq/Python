L = [1,2,3]
#for i in range(len(L)):
    
def perm(L, x = 0):
    if x==len(L):
        print(L)
    else:
        for i in range(x, len(L)):
            L[i], L[x] = L[x], L[i]
            perm(L,x+1)
            L[i], L[x] = L[x], L[i]
   
perm(L)