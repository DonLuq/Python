def szyfruj(T:str = 'to jest moj tekst '):
    klucz = {'a' : 'y', 'e' : 'i', 'i' : 'o', 'o' : 'a', 'y' : 'e'}
    letter = list(T)
    #print(letter)
    for i in range(len(T)):
        if letter[i] in klucz:
            letter[i] = klucz[letter[i]]
    return ('').join(letter)

def deszyfruj(T:str = 'ta jist maj tikst '):
    klucz = {'y' : 'a', 'i' : 'e', 'o' : 'i', 'a' : 'o', 'e' : 'y'}
    letter = list(T)
    #print(letter)
    for i in range(len(T)):
        if letter[i] in klucz:
            letter[i] = klucz[letter[i]]
    return ('').join(letter)


print(szyfruj())
print(szyfruj('maksymylian sznatko uczący sie na izotopy'))
print(szyfruj('dawno dawn temu python jes\zyk 123124 !@#!# 4#@$@'))

print(deszyfruj(szyfruj()))
print(deszyfruj(szyfruj('maksymylian sznatko uczący sie na izotopy')))
print(deszyfruj(szyfruj('dawno dawno temu python jezyk 123124 !@#!# 4#@$@')))