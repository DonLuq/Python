import re

def zdan(N:str):
    N_list=list(N)
    letter_list = []
    for letter in N_list:
        if re.search('[a-zA-Z]',letter):
            letter_list.append(letter.upper())
    if len(set(letter_list))==26:
        print('Jest pantogramem!')
    else:
        print('NIE JEST pantogramem!')

 
    


#N = 'The $$$$ quick brown fox jumps over the lazy dog. False, I see false, this exam I may pass.'
N = input('Podaj zdanie:\n')
zdan(N)