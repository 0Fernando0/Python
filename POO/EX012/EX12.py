#Herança Simples
'''
Biblioteca -> chama_interface
    Interface(Biblioteca) -> metodo_interface
        metodo_da_interface

main -> interface
'''
from EX12C import Interface

i1 = Interface()
i1.chama_metodo_da_interface()

'''
Animal -> respirar
    lobo(Animal) -> respirar / uivar
    (é um lobo e um animal)
    cachorro(lobo) -> respirar / uivar / latir
    (cachorro é um cachorro, também é um lobo() e um animal())
########################################
Familia -> alto
    avô(Familia) -> alto / -> ruivo
    pai(avô) -> alto / -> ruivo / -> inteligente
    neto(pai) -> alto / -> ruivo / -> inteligente
'''
