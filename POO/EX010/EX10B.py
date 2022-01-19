class A:
    def __new__(cls,*args,**kwargs):
        
        cls.nome = 'Fernando'
        
        return super().__new__(cls)
    
    def __init__(self):
        print('inicio...')
