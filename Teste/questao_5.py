"""
5) Escreva um programa que inverta os caracteres de um string. 

IMPORTANTE: 

	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 

	b) Evite usar funções prontas, como, por exemplo, reverse; 
"""

# não usei função pronta como reverse
def inverter_string(palavra:str):
    print(palavra[::-1])

# mais vou criar outra função para não usar manipulação de string ok?
def inverter_string2(texto:str):
    total = len(texto)
    while total > 0:
        print(texto[total-1],end="")
        total -= 1        

if __name__ == "__main__":
    inverter_string2("dia")