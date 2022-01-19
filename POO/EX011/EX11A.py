'''
from datetime import datetime
dia = datetime.now().day

from EX011B import *
data = Arquivo('DiaHoje.txt','w')
data.__enter__()
data.edit(f'hoje e dia {dia}')
data.__exit__()
'''
from contextlib import contextmanager

@contextmanager
def abrir(arquivo,modo):
    try:
        arquivo = open(arquivo,modo)
        print('abrindo arquivo...')
        yield arquivo
    finally:
        print('fechando arquivo...')
        arquivo.close()
        
with abrir('abc.txt','w') as arquivo:
    arquivo.write('um arquivo qualquer\n')
    arquivo.write('pagina 1\n')
    arquivo.write('pagina 2\n') 
