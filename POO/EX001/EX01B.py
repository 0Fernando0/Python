class Escritor:
    def __init__(self,nome):
        self.__nome = nome
        self.__ferramenta = None

    #getter
    @property
    def nome(self):
        return self.__nome

    #getter
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    #setter
    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self.__ferramenta = ferramenta
    
class Caneta:
    def __init__(self,marca):
        self.__marca = marca

    #getter
    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print('caneta está escrevendo')

class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina está escrevendo')

    
