
def silnia(N:int):
    iloczyn = 1
    for i in range(N,0,-1): 
        #print(i)
        if N==0:
            return 1
        else:
            x = i
            iloczyn *= x
    return iloczyn

N = int(input('Podaj N!(N):\n'))
print(silnia(N))