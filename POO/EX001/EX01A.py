from EX01B import Escritor
from EX01B import Caneta
from EX01B import MaquinaDeEscrever

'''
ASSOCIAÇÃO - POO
'''

escritor = Escritor('fernando')
caneta = Caneta('bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
