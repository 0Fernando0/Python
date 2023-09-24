#Faça um programa que leia dados do teclado e mostre seus informações.


barra = lambda : print("-" * 38)

def exibirTipos(tipos: str, comparacao) -> None:
    barra()
    print(f"|{tipos.title()}: {str(comparacao).rjust(34-len(tipos))}|")

algo = input("digite algo no teclado: ")
exibirTipos("tipo primivo",type(algo))
exibirTipos("alpha númerico",algo.isalnum())
exibirTipos("númerico",algo.isalnum())
exibirTipos("letras",algo.isalpha())
exibirTipos("minuscula",algo.islower())
exibirTipos("maiuscula",algo.isupper())
exibirTipos("so tem espaços",algo.isspace())
barra()