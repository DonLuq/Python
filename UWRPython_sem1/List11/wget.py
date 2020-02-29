import urllib.request
import urllib.response

adres = input("Podaj adres strony: ")

def geturl(url):
    u = urllib.parse.urlsplit(url)
    if url[-1] == '/':
        name = 'index.html'
    else:
        name = u.netloc.split('.')[0] + '.html'

    html = urllib.request.urlopen(url)
    text = html.read()

    f = open(name, 'wb')
    f.write(text)
    f.close()
    

geturl(adres)