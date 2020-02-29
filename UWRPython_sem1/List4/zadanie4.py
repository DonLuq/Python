def funkcja(n,a = 1,q = 2):
    value = a*q**(n-1)
    return value

x = int(input('Wprowadz n dla ciągu:\n'))
print(funkcja(x,4,3))