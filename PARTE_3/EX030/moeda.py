#função para acrecentar em porcentagem de acordo com o valor inserido
def aumentar(n,n1):
    s = ((n/100) * n1) + n
    return s

#função para reduzir em porcentagem de acordo com o valor inserido
def reduzir(n,n1):
    s = n - ((n/100) * n1)

#função para dobrar o valor inserido
def dobro(n):
    s = n * 2
    return s

#função reduzir pela metade do valor inserido
def metade(n):
    s = n / 2
    return s 

#função para aparecer valor em forma de dinheiro(R$)
def moeda(n=0,moeda = 'R$'):
    return f'{moeda}{n:>4.2f}'.replace('.',',')

def resumo(n=0,aum=10,red=5):
    s1 = n + ((n/100) * aum)
    s2 = n - ((n/100) * red)
    print('='*30)
    print('RESUMO DO VALOR'.center(30))
    print('='*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do Preço: \t{moeda(dobro(n))}')
    print(f'A Metade do valor: \t{moeda(metade(n))}')
    print(f'Aumento de {aum}%: \t{moeda(s1)}')
    print(f'Reduzindo {red}%:  \t\t{moeda(s2)}')
    print('='*30)

