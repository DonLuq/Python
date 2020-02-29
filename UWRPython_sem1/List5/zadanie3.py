#Rzymskie na arabskie

N = input('Wprowadz liczbe z czasów świetności imperium:\n')

Dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def Rzym(N:str):
    L=list(N)
    for i in range(len(L)):
        L[i]=Dict[L[i]]
    Arab = 0
    i = len(L)-1
    while i>-1:
        if i==0:
            Arab+=L[i]
            break
        elif L[i]>L[i-1]:
            WSP=L[i]
            while L[i]>=L[i-1]:
                WSP-=L[i-1]
                i=i-1
            Arab+=WSP
            i=i-1
        elif L[i]<=L[i-1]:
            Arab+=L[i]
            i=i-1
    return Arab

   
print(Rzym(N))




#     for i in range(len(N_lista)-1,-1,-1):
#         if(i==0):
#             Arab+=N_lista[i]
#         elif(N_lista[i] <= N_lista[i-1]):
#             Arab+=N_lista[i]
#         elif(N_lista[i] > N_lista[i-1]):
#             #Arab-=N_lista[i-1]
#             WSP=N_lista[i]
#             while(WSP>N_lista[i-1]):
#                 WSP-=N_lista[i-1]
#                 i=i-1
#             Arab+=WSP