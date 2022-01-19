def ficha(n='<desconhecido>',g=' '):
    if n != ' ' and g != ' ':
        return print(f'o jogador {n} marcou {g} gols no campeonato')
    if g == ' ' and n == ' ':
        return print(f'o jogador <desconhecido> marcou <desconhecido> gols no campeonato')
    elif n == ' ':
        return print(f'o jogador <desconhecido> marcou {g} gols no campeonato')
    elif g == ' ':
        return print(f'o jogador {n} marcou <desconhecido> gols')
#nome = str(input('nome do jogador: '))
#gol = str(input('Quantos gols: '))
ficha('carlos',3)
