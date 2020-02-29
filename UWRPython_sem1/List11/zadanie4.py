text = 'Napisz program, aby który w podanym tekście odnajduje ala amaeryka wszystkie słowa  ebola zaczynające się od „a” lub „e”.'

import re

def slova(text):
    words = re.findall(r'\b[aAeE]\w+', text)
    print(words)
    return words

slova(text)