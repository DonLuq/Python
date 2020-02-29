

def szereg(N:int):
    SUMA = 0
    for i in range(1,N+1):
        SUMA = SUMA + 1/i
    return SUMA

N = 20
print(szereg(N))