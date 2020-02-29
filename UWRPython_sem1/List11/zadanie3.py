import re

def URL(filename):
    with open(filename) as plik:
        content = plik.read()
    plik.close()

    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    return url
