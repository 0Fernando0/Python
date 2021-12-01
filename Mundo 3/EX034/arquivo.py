from os import close
from teste import *

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ocorreu um erro na criação do arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso')
def ler_arq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo')
    else:
        cabeçalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()
def cadastrar(arq,nome='Desconhecido', idade=0):
    try:
        a = open(arq,'at')
    except:
        print('houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'novo registro de {nome} adicionado')
            a.close()
    
            
