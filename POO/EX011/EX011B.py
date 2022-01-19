from os import close

class Arquivo:
    def __init__(self,arquivo,modo):
        self.arquivo = open(arquivo,modo)
    
    def __enter__(self):
        print('retornando arquivos')
        return self.arquivo
    
    def edit(self,msg):
        self.arquivo.write(msg)
    
    def __exit__(self):
        self.arquivo.close()
    

    