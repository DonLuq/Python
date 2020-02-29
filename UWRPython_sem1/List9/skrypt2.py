import os, sys


#if not sys.argv[1:]:
 #   print('Wprowadzono niepoprawny argument.')
  #  sys.exit()
N = 0
for param in sys.argv[1:]:
    N = param

#Skr1 = open('skrypt1.py')               
#sys.stdout = Skr1
#Skr1.close()
#print(sys.stdout)

for i in range(3):
    sys.stdout.write('Dive in')