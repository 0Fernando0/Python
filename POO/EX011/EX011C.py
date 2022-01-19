'''
            Context mananger
criando e usadn o gerenciador de contexto
'''

'''
#metodo antigo
arquivo = open('abc.txt','w')
arquivo.write('hoje é 06/01/2022')
arquivo.close()
'''

#novo metodo!!!
'''
with open('abc.txt','w') as arquivo:
    arquivo.write('hoje e 06/01/2022')
'''