'''
Herança Multipla - POO
'''

from EX05B import *

class Smartphone(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False
    
    def conectar(self):
        if not self._ligado:
            return f'{self._nome} não está ligado'
        if self._conectado:
            return f'{self._nome} já está conectado'
        self._conectado = True
        return f'{self._nome} foi conectado'
    
    def desconectar(self):
        if not self._conectado:
            return 'já está desconectado'
        self._conectado = False
        return f'{self._nome} foi desconectado'

ap1 = Smartphone('iphone')
ap1.ligar()
print(ap1.conectar())
print(ap1.desconectar())

