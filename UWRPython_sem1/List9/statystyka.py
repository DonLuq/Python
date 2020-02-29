import numpy as np
import os, sys

W = []
for line in sys.argv[1:]:
    W.append(float(line))
#print(W)


if os.fstat(sys.stdin.fileno()).st_size != 0:
    for line in sys.stdin.read():
        if line.strip() != "":
            W.append(float(line))
        elif line.strip() ==" ":
            break
            
  
#print(W)

wariancje = np.var(W)
odch_stand = np.std(W)
sred_arytm =  np.mean(W)
print("Wariacja:",round(wariancje,2))
print("Odchylenie standardowe:",round(odch_stand,2))
print("Srednia arytmetyczna:",round(sred_arytm,2))
#statystyka()
