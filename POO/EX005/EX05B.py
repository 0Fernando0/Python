class Eletronico:
    def __init__(self,nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return f'{self._nome} já está ligado!'
        self._ligado = True
        return f'{self._nome} foi ligado'
    
    def desligar(self):
        if not self._ligado:
            return f'{self._nome} já está desligado!'
        self._ligado = False
        return f'{self._nome} foi desligado'



'''
class A:
    def falar(self):
        print('falando...estou em A')

class B(A):
    def falar(self):
        print('falando...estou em B')

class C(A):
    def falar(self):
        print('falando...estou em C')

class D(C,B):
    pass
'''