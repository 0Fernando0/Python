import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('Deu Erro')
else:
    print('Deu Bom')
    print(site.read())