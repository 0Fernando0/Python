from teste import *
from arquivo import *

arq = 'lista_de_pessoas.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Novas Pessoas','Sair Do Programa'])
    if resposta == 1:
        #opção para listar conteudo de arquivos
        ler_arq(arq)
    elif resposta == 2:
        #opção para adicionar novos conteudos ao arquivo
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome , idade)
    elif resposta == 3:
        #opção para sair do programa
        print('Saindo Do Sistema... Até logo')
        break
    else:
        print('Opção Invalida')
 