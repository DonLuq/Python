def look(S):
    E=[]
    i = 0
    while i < len(S):
        count = 1
        while i + 1 < len(S) and S[i] == S[i + 1]:
            i+=1
            count+=1
        E.append(str(count)+S[i])
        i +=1
    return ''.join(E)

def look_and_say(N):
    S='1'
    N = N
    for i in range(N-1):
        S = look(S)
    return S

N = int(input('Wprowadz N:\n'))
print(look_and_say(N))

