def dziel(N:int,M:int):
    D = []
    for n in range(1,max(N,M)):
        if N%n == 0:
            for x in range(1,M):
                if M%x==0 and x==n:
                    D.append(x)
    #print(D)
    return(max(D))
n = int(input('Liczby:\n'))
m = int(input(''))

print('Wynik: ', dziel(n,m))
#print(dziel(15,9))