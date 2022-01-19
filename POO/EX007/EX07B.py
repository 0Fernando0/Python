from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def fala(self,msg):pass

class B(A):
    def fala(self,msg):
        print(f'B está falando {msg}')

class C(B):
    def fala(self,msg):
        print(f'C está falando {msg}')
