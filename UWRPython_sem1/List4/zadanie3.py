import math

def convert(value,typ=''): # typ czyli na co chcemy zamienic
    'Wprowadz do funkcji wartosc kata(rad/sto) oraz rodzaj jednostek na ktore chcesz aby zostaly zamienione.'
    if typ=='':
        typ = input('Przeliczamy na radiany czy na stopnie?(rad/sto):\n')
    if typ == 'rad':
        print("Przeliczamy: {} stopni to {} radianow!".format(value,round(value*math.pi/180,4)))
    if typ == 'sto':
        print("Przeliczamy: {} radianow to {} stopni!".format(value,round(value/math.pi*180,0)))
        
x = float(input('Wprowadz wartość:\n'))
convert(x,'rad')