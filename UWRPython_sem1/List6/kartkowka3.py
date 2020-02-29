#import sys

# def f(X:list):
#     a=1
#     b=2
#     c=3
#     if not X[0]:
#         print('Wartosc arguentu a to:',a)
#     elif X[0]:
#         print('Wartosc arguentu a to:',X[0])
#     if not X[1]:
#         print('Wartosc arguentu b to:',b)
#     elif X[1]:
#         print('Wartosc arguentu a to:',X[1])
#     if not X[2]:
#         print('Wartosc arguentu c to:',c)
#     elif X[2]:
#         print('Wartosc arguentu a to:',X[2])
#     for i in range(3,len(X)):
#         print('Przekazano nieuzywany argument: ',i)
#  
# N= list(input('sdadas\n'))
# f(N)


#PROGRAM PONIZEJ

def f(a=1,b=2,c=3,*therest):
    print('Wartosc arguentu a to:',a)
    print('Wartosc arguentu b to:',b)
    print('Wartosc arguentu c to:',c)
    #print(*therest)
    for i in therest:
        print('Przekazano nieuzywany argument: ',i)
        
        
        
        
f(1,4,3,2,4,5)