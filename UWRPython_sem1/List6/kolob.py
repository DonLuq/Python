#python2.7
SUMA = 0
N = 100.43 #kwota ktora zbieramy
while 1:
    kwota= float(input('Pytam o kwote: '))
    SUMA+=kwota
    if SUMA >= N:
        print 'Gratulacje uzbierałeś: ',SUMA,'zł'
        break
    else:
        A = N-SUMA
        print 'Brakuje jeszcze: %.2f zł'%A

            print ('Brakuje jeszcze: {0:.2f} zł'.format((N-SUMA)))