"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

IMPORTANTE:  
	Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código; 
"""

def isfibo(number:int):
    x = 0
    y = 1
    while True:
        f = x + y
        x = y
        y = f
        if(f == number or number in (0,1)):
            print("o valor se encontra na sequencia")
            break
        else:
            if(f > number):
                print("o valor não se encontra na sequencia")
                break      

def filtro(texto:int):
    while True:     
        num = input(texto).strip()
        if not (num.isnumeric()):
            print("Somente Números São Aceitos")
            continue
        return int(num)
    

def main():
    numero = filtro("Digite Um número: ")
    isfibo(numero)
    

if __name__ == "__main__":
    main()