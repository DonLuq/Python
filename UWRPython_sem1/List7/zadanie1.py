import time as T
N = int(input('Wprowadz ktora liczba fib:\n'))

def fib(N:int):
    if N==1:
        return 0
    elif N==2:
        return 1
    else:
        return fib(N-1)+fib(N-2)


def fibiter(N:int):
    a, b = 0, 1
    print(a)
    print(b)
    for i in range(1, N - 1):
        a, b = b, a + b
        print(b)
           


clock1 = T.time()
for i in range(1,N+1):
    print(fib(i))
clock2 = T.time()

print('')

clock3 = T.time()
fibiter(N)
clock4 = T.time()

print('Czas dla rekurencji: {0:.4f} ms'.format((clock2 - clock1)*1000))
print('Czas dla iteracji: {0:.4f} ms'.format((clock4 - clock3)*1000))
    