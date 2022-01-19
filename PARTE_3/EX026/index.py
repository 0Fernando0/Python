from datetime import date


def voto(n):
    from datetime import time
    idade = date.today().year - n
    if idade >= 16 and idade < 18 or idade > 60:
        return print(f'com {idade} anos: VOTO OPCIONAL!')
    elif idade >= 18 and idade <= 60:
        return print(f'com {idade} anos: VOTO OBRIGATORIO!')
    else:
        return print(f'com {idade} anos: VOTO NEGADO!')
voto(int(input('Em que ano você nasceu? ')))

