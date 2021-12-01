def aumentar(n):
    s = ((n/100) * 10) + n
    return s

def dobro(n):
    s = n * 2
    return s

def metade(n):
    s = n / 2
    return s 

def moeda(n=0,moeda = 'R$'):
    return f'{moeda}{n:>4.2f}'.replace('.',',')