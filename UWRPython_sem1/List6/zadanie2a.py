#jaki cel jest rozdzielania programu szyfrujacego i deszyfrujacego skoro chodzi o pokazania dzialania kodu?
import SzyfrCezara as S

Z = input('Wprowadz co chcesz za szyfrowac: \n')

Tajne = S.szyfruj(Z)
print('Po szyfrowaniu:\n',Tajne)
