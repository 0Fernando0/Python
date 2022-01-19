class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')

class Cliente:
    def comprar(self):
        print(f'{self.classe} comprando...')
    def falar(self):
        print(f'estou em cliente')

class ClienteVip:
    def __init__(self,nome,idade,sobrenome):
        Pessoa.__init__(self,nome,idade)
        self.sobrenome = sobrenome